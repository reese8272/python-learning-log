#!/usr/bin/env python3
"""Render a tailored jobs/<role>/resume.md into a PDF that matches the
canonical Reese_Ludwick_Resume.docx style (Georgia->Gelasio, uppercase
ruled section headers, right-aligned dates, bullet lists).

Usage: python .build_resume.py <role-folder> [<role-folder> ...]
       python .build_resume.py --all
Compiles with tectonic. Writes <role>/resume.tex and <role>/resume.pdf.
"""
import os, re, sys, subprocess, glob

FONTDIR = "/home/reese/.local/share/fonts/gelasio/"
HERE = os.path.dirname(os.path.abspath(__file__))

PREAMBLE = r"""\documentclass[10pt]{article}
\usepackage[letterpaper,left=0.625in,right=0.625in,top=0.5in,bottom=0.5in]{geometry}
\usepackage{fontspec}
\setmainfont{GelasioStatic}[
  Path=%FONTDIR%,
  Extension=.ttf,
  UprightFont=*-Regular, BoldFont=*-Bold,
  ItalicFont=*-Italic, BoldItalicFont=*-BoldItalic]
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.4pt}
\pagestyle{empty}
\titleformat{\section}{\normalsize}{}{0pt}{\MakeUppercase}[{\vspace{-3pt}\titlerule[0.6pt]}]
\titlespacing*{\section}{0pt}{2pt}{1pt}
\setlist[itemize]{leftmargin=1.35em,itemsep=0.2pt,topsep=0.4pt,parsep=0pt,label=\textbullet,before=\vspace{-2.5pt}}
\newcommand{\entrygap}{\vspace{2.5pt}}
\newcommand{\dentry}[4]{\noindent\textbf{#1}\hfill{#2}\\{#3}\hfill{#4}\par}
\newcommand{\sentry}[2]{\noindent\textbf{#1}\hfill{#2}\par}
\begin{document}
"""

def esc(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'),
                 ('^', r'\textasciicircum{}'), ('$', r'\$')]:
        s = s.replace(a, b)
    return s

def link_text(s):
    """markdown [text](url) -> text"""
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)

def strip_emph(s):
    return s.replace('**', '').replace('*', '').replace('`', '')

def inline(s):
    """links -> text, escape, then convert **bold** and *italic*."""
    s = link_text(s)
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)\*(?!\*)', r'\\textit{\1}', s)
    return s

DATE_RE = re.compile(r'\d|Present')

def parse_entry_header(text):
    """plain header (emphasis stripped) -> (title, company, location, dates).
    Handles: 'Title — Company (Remote) · Dates', 'Title — Company (Remote, Dates)',
    'Title — Company, Remote — Dates', 'Title — Company'."""
    text = text.strip()
    for d in (' — ', ' – '):
        if d in text:
            title, company = text.split(d, 1)
            break
    else:
        title, company = text, ''
    company = company.strip()
    loc, dates = '', ''
    m = re.search(r'\(([^)]*)\)', company)
    if m:
        inside = m.group(1).strip()
        company = (company[:m.start()] + company[m.end():]).strip()
        if ',' in inside:
            a, b = inside.split(',', 1)
            if DATE_RE.search(b):
                loc, dates = a.strip(), b.strip()
            else:
                loc = inside
        elif DATE_RE.search(inside):
            dates = inside
        else:
            loc = inside
    for sep in (' · ', ' — ', ' – ', ', '):
        if sep in company:
            head, tail = company.rsplit(sep, 1)
            tail = tail.strip()
            if DATE_RE.search(tail) and not dates:
                dates, company = tail, head.strip()
            elif sep == ', ' and not loc and not DATE_RE.search(tail):
                loc, company = tail, head.strip()
    company = re.sub(r'\s*,\s*', ', ', company).strip(' ·—–,')
    return title.strip(), company, loc, dates

def is_header(s):
    return s.startswith('### ') or s.startswith('**')

def split_sections(md):
    """return (header_lines, [(title, [body_lines]), ...])"""
    lines = md.splitlines()
    header, sections, cur, curname = [], [], None, None
    in_header = True
    for ln in lines:
        if ln.startswith('## '):
            in_header = False
            if cur is not None:
                sections.append((curname, cur))
            curname, cur = ln[3:].strip(), []
        elif ln.startswith('# '):
            header.append(ln[2:].strip())          # name
        elif in_header:
            if ln.strip() and not ln.strip().startswith('---'):
                header.append(ln.strip())
        else:
            if ln.strip().startswith('---'):
                continue
            cur.append(ln)
    if cur is not None:
        sections.append((curname, cur))
    return header, sections

def _bullets(out, bullets):
    if bullets:
        out.append(r'\begin{itemize}')
        out.extend(r'  \item ' + inline(b) for b in bullets)
        out.append(r'\end{itemize}')
        bullets.clear()

def render_experience(body):
    out, bullets = [], []
    for ln in body:
        s = ln.strip()
        if not s:
            continue
        if s.startswith('- '):
            bullets.append(s[2:].strip())
        elif is_header(s):
            _bullets(out, bullets)
            raw = s[4:] if s.startswith('### ') else s
            title, company, loc, dates = parse_entry_header(strip_emph(link_text(raw)))
            out.append(r'\dentry{%s}{%s}{%s}{%s}' % (
                esc(title), esc(loc), esc(company), esc(dates)))
        else:
            bullets.append(s)
    _bullets(out, bullets)
    return out

def render_projects(body):
    out, bullets = [], []
    for ln in body:
        s = ln.strip()
        if not s:
            continue
        if s.startswith('- '):
            bullets.append(s[2:].strip())
        elif s.startswith('### '):
            _bullets(out, bullets)
            h = s[4:]
            if ' — ' in h:
                name, rest = h.split(' — ', 1)
                out.append(r'\noindent\textbf{%s} --- %s\par' % (
                    esc(strip_emph(name)), inline(rest)))
            else:
                out.append(r'\noindent\textbf{%s}\par' % esc(strip_emph(h)))
        elif s.startswith('**'):
            _bullets(out, bullets)
            out.append(r'\noindent ' + inline(s) + r'\par')
        else:
            _bullets(out, bullets)
            out.append(r'\noindent\textit{%s}\par' % esc(strip_emph(link_text(s))))
    _bullets(out, bullets)
    return out

def render_plain(body):
    """skills / education / certifications: each line as its own paragraph."""
    out = []
    for ln in body:
        s = ln.strip()
        if not s:
            continue
        if s.startswith('- '):
            s = s[2:].strip()
        out.append(r'\noindent ' + inline(s) + r'\par')
    return out

def render_summary(body):
    para = ' '.join(l.strip() for l in body if l.strip())
    return [r'\noindent ' + inline(para) + r'\par']

def build(role):
    folder = os.path.join(HERE, role) if not os.path.isabs(role) else role
    md = open(os.path.join(folder, 'resume.md')).read()
    header, sections = split_sections(md)
    name = header[0]
    contact_raw = ' | '.join(header[1:])
    contact_raw = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\2', contact_raw)  # [text](url)->url
    contact_raw = contact_raw.replace('LinkedIn: ', '').replace('GitHub: ', '')
    contact = esc(contact_raw)
    tex = [PREAMBLE.replace('%FONTDIR%', FONTDIR)]
    tex.append(r'\begin{center}')
    tex.append(r'{\fontsize{14}{16}\selectfont\bfseries %s}\\[1pt]' % esc(name))
    tex.append(r'{\fontsize{9}{11}\selectfont %s}' % contact)
    tex.append(r'\end{center}')
    tex.append(r'\vspace{-2pt}')
    for title, body in sections:
        tex.append(r'\section*{%s}' % esc(title))
        low = title.lower()
        if low.startswith('summary'):
            tex += render_summary(body)
        elif low.startswith('experience'):
            tex += render_experience(body)
        elif low.startswith('project'):
            tex += render_projects(body)
        else:
            tex += render_plain(body)
    tex.append(r'\end{document}')
    texpath = os.path.join(folder, 'resume.tex')
    open(texpath, 'w').write('\n'.join(tex))
    r = subprocess.run(['tectonic', '-o', folder, texpath],
                       capture_output=True, text=True)
    ok = r.returncode == 0 and os.path.exists(os.path.join(folder, 'resume.pdf'))
    print(('OK  ' if ok else 'FAIL') + ' ' + role)
    if not ok:
        print(r.stderr[-1500:])
    return ok

if __name__ == '__main__':
    args = sys.argv[1:]
    if args == ['--all']:
        args = sorted(d for d in os.listdir(HERE)
                      if os.path.isdir(os.path.join(HERE, d))
                      and os.path.exists(os.path.join(HERE, d, 'resume.md')))
    ok = all(build(a.rstrip('/')) for a in args)
    sys.exit(0 if ok else 1)
