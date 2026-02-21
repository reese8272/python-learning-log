# Curated Learning Path: From LangChain to Production AI Engineering

> **Target audience:** Junior Python Developer → Senior AI/ML Engineer
> **Total videos:** 71 (Udemy) + LangSmith Academy (external, free) | **Estimated time:** ~18 hours of focused content
> **Strategy:** Cherry-picked across 7 Udemy courses + 1 free external course, ordered by dependency, zero filler

---

## Course Abbreviations

| Abbreviation | Full Course Name |
|---|---|
| **Eden Marco** | LangChain - Develop AI Agents with LangChain & LangGraph (Eden Marco) |
| **Ultimate RAG** | Ultimate RAG Bootcamp Using LangChain, LangGraph & LangSmith |
| **Hands-On RAG** | Hands-On RAG with LangChain Build Real-World Projects |
| **MCP Masterclass** | MCP Masterclass Complete Guide to MCP in Python |
| **Gen AI Masters** | Gen AI Masters 2026 - From Python to Gen AI |
| **RAG-LLM Evals** | RAG-LLM Evals & Test Automation for Beginners |
| **LLM Masterclass** | LLM Engineering, RAG, & AI Agents Masterclass [2026] |

---

## Stage 1: Foundations

### Phase 1: LangChain Core (~50 min)

*Get productive with LangChain's abstractions: prompts, chains, models, memory.*

- [ ] [LangChain] **"What is LangChain? LangChain Under 6 Minutes"** — *Eden Marco* (6:00)
- [ ] [LangChain] **"LangChain Fundamentals: Prompt Templates, ChatModels, and Chains"** — *Eden Marco* (5:55)
- [ ] [LangChain] **"Building a LangChain Chain to Summarize Text"** — *Eden Marco* (11:12)
- [ ] [LangChain] **"Using Local Open-Weights Models with LangChain and Ollama"** — *Eden Marco* (6:20)
- [ ] [LangChain] **"LangChain Token Limitation Handeling Strategies"** — *Eden Marco* (11:29)
- [ ] [LangChain] **"LangChain Memory Theory Deepdive (LangGraph)"** — *Eden Marco* (8:31)

### Phase 2: Prompt & Context Engineering (~54 min)

*Master the prompting patterns that drive agent and RAG quality.*

- [ ] [Prompt Eng] **"Few Shot Prompting"** — *Eden Marco* (8:26)
- [ ] [Prompt Eng] **"Chain of Thought Prompting"** — *Eden Marco* (8:33)
- [ ] [Prompt Eng] **"ReAct Prompting"** — *Eden Marco* (7:18)
- [ ] [Prompt Eng] **"Prompt Engineering Quick Tips"** — *Eden Marco* (8:59)
- [ ] [Prompt Eng] **"Context Engineering"** — *Eden Marco* (5:20)
- [ ] [Prompt Eng] **"Context Engineering a System Prompt"** — *Eden Marco* (10:20)

### Phase 3: Agents, Tool Calling & LangSmith (~100 min)

*Understand how agents reason, call tools, and produce structured output. Set up tracing.*

- [ ] [LangChain] **"[Theory] The Gist of ReACT"** — *Eden Marco* (7:02)
- [ ] [LangChain] **"Defining LangChain Tools and Initializing Chat Models"** — *Eden Marco* (9:02)
- [ ] [LangChain] **"Tool Binding and Defensive Prompting for LangChain Agents"** — *Eden Marco* (5:28)
- [ ] [LangChain] **"Understanding the ReAct Agent Loop in Langchain"** — *Eden Marco* (11:26)
- [ ] [LangChain] **"[Theory] Understanding Function Calling for LLMs"** — *Eden Marco* (7:04)
- [ ] [LangChain] **"[Theory] Function Calling Vs ReAct"** — *Eden Marco* (5:04)
- [ ] [LangChain] **"Upgrading ReAct Agents with Tool Calling"** — *Eden Marco* (15:25)
- [ ] [LangChain] **"Reliable Structured Output with LangChain's .with_structured_output()"** — *Eden Marco* (12:36)
- [ ] [LangSmith] **"Integrating LangSmith for LangChain Application Tracing"** — *Eden Marco* (7:18)
- [ ] [LangSmith] **"Tracing a LangChain Agent's Tool Call Execution with LangSmith"** — *Eden Marco* (3:15)

### Phase 3.5: LangSmith Deep Dive (~2 hrs, external)

*Go beyond basic tracing: experiment tracking, dataset management, annotation queues, evaluation workflows.*

> **⚠️ External resource (not Udemy):** Complete the free [LangSmith course on LangChain Academy](https://academy.langchain.com/). This is required, not optional — everything from Phase 4 onward should be traced and evaluated in LangSmith.

- [ ] [LangSmith] **LangChain Academy — LangSmith Course** (free, ~2 hrs)
  - Tracing and observability for chains and agents
  - Creating and managing evaluation datasets
  - Running experiments and comparing results
  - Annotation queues for human-in-the-loop feedback
  - Online evaluation with automations

> **Milestone:** You can build LangChain chains with memory, call tools via agents, prompt with CoT/ReAct, and trace, evaluate, and experiment in LangSmith.

---

## Stage 2: Intermediate

### Phase 4: RAG Pipelines (~2 hrs)

*Build end-to-end Retrieval-Augmented Generation: loading, chunking, embedding, retrieval, generation.*

- [ ] [RAG] **"Introduction to Retrieval Augmentation Generation (RAG)"** — *Eden Marco* (7:46)
- [ ] [RAG] **"Prompt Engineering Vs FineTuning Vs RAG"** — *Ultimate RAG* (20:31)
- [ ] [RAG] **"Document Structure In LangChain"** — *Ultimate RAG* (11:22)
- [ ] [RAG] **"Text Splitting Techniques"** — *Ultimate RAG* (18:20)
- [ ] [RAG] **"Introduction To Embeddings And Vector Databases"** — *Ultimate RAG* (17:16)
- [ ] [RAG] **"Vector Stores Vs Vector Databases"** — *Ultimate RAG* (9:38)
- [ ] [RAG] **"Building Tradition RAG With ChromaDb Vector Store-Part 1"** — *Ultimate RAG* (25:36)
- [ ] [RAG] **"Building Traditional RAG With ChromaDB Vector Store-Part 2"** — *Ultimate RAG* (15:48)
- [ ] [RAG] **"Building RAG Pipeline Using LCEL(Langchain Expression Language)"** — *Ultimate RAG* (14:29)
- [ ] [RAG] **"Advanced RAG Techniques-Conversational Memory"** — *Ultimate RAG* (17:25)

### Phase 5: LangGraph (~1.5 hrs)

*Stateful agent workflows: nodes, edges, state management, tool nodes, and debugging.*

- [ ] [LangGraph] **"What is LangGraph?"** — *Eden Marco* (4:56)
- [ ] [LangGraph] **"Why LangGraph? LangGraph VS LangChain"** — *Eden Marco* (16:42)
- [ ] [LangGraph] **"LangGraph Core Components"** — *Eden Marco* (5:17)
- [ ] [LangGraph] **"[Hands On] Coding the Agent's Brain: Implementing the ReAct Runnable"** — *Eden Marco* (8:28)
- [ ] [LangGraph] **"[Hands On] Building Blocks: Defining Your Agent's Nodes in LangGraph"** — *Eden Marco* (5:52)
- [ ] [LangGraph] **"[Hands On] Bringing Your ReAct Agent to Life: Connecting Nodes into a Graph"** — *Eden Marco* (7:21)
- [ ] [LangGraph] **"[IMPORTANT] Building Modern LLM Agents: From History to LangGraph v1.0"** — *Eden Marco* (8:49)
- [ ] [LangGraph] **"Tools And Tools Node Integration-Part 1"** — *Ultimate RAG* (28:48)
- [ ] [LangSmith] **"Debugging Wiht LangGraph Studio And Langsmith"** — *Ultimate RAG* (20:39)

> **Milestone:** You can build a full RAG pipeline and create stateful LangGraph agents with tool integration. You could ship a document Q&A chatbot to your team.

---

## Stage 3: Advanced

### Phase 6: Advanced RAG Techniques (~2 hrs)

*Hybrid search, re-ranking, semantic chunking, query transformation, and production caching/metadata patterns.*

- [ ] [RAG] **"Semantic Chunking With RAG"** — *Ultimate RAG* (16:17)
- [ ] [RAG] **"Vector Index Types (Flat, IVFFlat, HNSW, Disk-Based)"** — *Hands-On RAG* (3:09)
- [ ] [RAG] **"Index Code Walkthrough"** — *Hands-On RAG* (2:36)
- [ ] [RAG] **"Create Index"** — *Hands-On RAG* (5:11)
- [ ] [RAG] **"Combining Dense And Sparse Retriever With Langchain"** — *Ultimate RAG* (14:59)
- [ ] [RAG] **"Reranking Hybrid Search Statergy"** — *Ultimate RAG* (8:41)
- [ ] [RAG] **"Reranking Hybrid Statergy Implementation"** — *Ultimate RAG* (22:04)
- [ ] [RAG] **"Query Expansion Technique Implementation"** — *Ultimate RAG* (15:55)
- [ ] [RAG] **"HyDE Technique And Implementation"** — *Ultimate RAG* (22:27)
- [ ] [RAG] **"Re-Ranking Implementation"** — *Hands-On RAG* (3:55)
- [ ] [RAG] **"Semantic Cache In Action"** — *Hands-On RAG* (4:44)
- [ ] [RAG] **"Use Metadata Filtering"** — *Hands-On RAG* (1:33)

### Phase 7: Agentic RAG (~1.5 hrs)

*Self-RAG, Corrective RAG, Adaptive RAG, and multi-agent RAG orchestration.*

- [ ] [RAG] **"Traditional RAG Vs Agentic RAG"** — *Ultimate RAG* (13:01)
- [ ] [RAG] **"Corrective RAG Detailed Explanation"** — *Ultimate RAG* (7:13)
- [ ] [RAG] **"Corrective RAG Detailed Implementation"** — *Ultimate RAG* (13:55)
- [ ] [RAG] **"Adaptive RAG Theoretical Understanding"** — *Ultimate RAG* (11:54)
- [ ] [RAG] **"Adaptive RAG Implementation"** — *Ultimate RAG* (17:02)
- [ ] [RAG] **"Self Reflection Understanding and Implementation"** — *Ultimate RAG* (13:59)
- [ ] [LangGraph] **"Multi Agents Network With RAG"** — *Ultimate RAG* (11:34)

### Phase 8: MCP — Model Context Protocol (~1.75 hrs)

*Architecture, building MCP servers and clients in Python, transport protocols, LangChain integration.*

- [ ] [MCP] **"Why does MCP exist?"** — *MCP Masterclass* (5:15)
- [ ] [MCP] **"MCP architecture deep dive with agents and LLMs"** — *MCP Masterclass* (9:23)
- [ ] [MCP] **"FastMCP vs. lowlevel server"** — *MCP Masterclass* (5:14)
- [ ] [MCP] **"Local vs. Remote MCPs - Stdio vs. Streamable HTTP"** — *MCP Masterclass* (9:37)
- [ ] [MCP] **"Create a simple MCP Server 1"** — *MCP Masterclass* (9:13)
- [ ] [MCP] **"Create a simple MCP Server 2"** — *MCP Masterclass* (15:42)
- [ ] [MCP] **"Connect an MCP Client to an MCP Server locally built"** — *MCP Masterclass* (15:05)
- [ ] [MCP] **"Process query in MCP Client - Connect LLMs and MCP Servers 1"** — *MCP Masterclass* (13:02)
- [ ] [MCP] **"Bridging the Gap: The LangChain MCP Adapter Explained"** — *Eden Marco* (4:23)
- [ ] [MCP] **"LangChain's MultiServerMCPClient from the LangChain MCP Adapter"** — *Eden Marco* (8:37)

> **Milestone:** You can build advanced RAG systems (corrective, adaptive, agentic) and create MCP servers/clients that connect LLMs to external tools. You could design a multi-agent research assistant.

---

## Stage 4: Production

### Phase 9: Evals & Validation (~2.5 hrs)

*RAGAS metrics, n-gram metrics, BERTScore, Pytest-based eval automation, LLM-as-a-judge.*

- [ ] [Evals] **"Introduction to RAG Evaluation"** — *Gen AI Masters* (7:54)
- [ ] [Evals] **"N-gram Metrics (BLEU)"** — *Gen AI Masters* (14:08)
- [ ] [Evals] **"Model-based Metrics (BARTScore vs BERTScore)"** — *Gen AI Masters* (13:36)
- [ ] [Evals] **"RAGAS Framework (RAG Assessment)"** — *Gen AI Masters* (58:57)
- [ ] [Evals] **"End to end -Evaluate LLM for ContextPrecision metric with SingleTurn Test data"** — *RAG-LLM Evals* (20:38)
- [ ] [Evals] **"Evaluate LLM for Context Recall Metric with RAGAS Pytest Test example"** — *RAG-LLM Evals* (13:22)
- [ ] [Evals] **"Build Pytest fixtures to isolate OpenAI and LLM Wrapper common utils from test"** — *RAG-LLM Evals* (7:56)
- [ ] [Evals] **"Factual Correctness - Build a single Test to evaluate multiple LLM metrics"** — *RAG-LLM Evals* (12:02)
- [ ] [Evals] **"Evaluation Of Chatbots- Defining Metrics LLM AS A JUDGE"** — *Ultimate RAG* (8:10)
- [ ] [Evals] **"RAG Evaluation- Build Evaluators With Metrics"** — *Ultimate RAG* (16:25)

### Phase 10: Model Selection & Fine-Tuning Concepts (~1.5 hrs)

*Model benchmarking, tokenization, context windows, quantization theory (LoRA/QLoRA), and choosing the right LLM for your use case. Does NOT cover operational inference optimization or ML explainability — see rationale document for guidance on those topics.*

- [ ] [Models] **"Task 4. Understand OpenAI API response Structure & Token Usage"** — *LLM Masterclass* (10:33)
- [ ] [Models] **"Task 2. LLM Comparison, Benchmarks, & Vellum Leaderboard"** — *LLM Masterclass* (12:27)
- [ ] [Models] **"Task 5. A Framework for Choosing the right AI Model for Your Business - Part 1"** — *LLM Masterclass* (13:56)
- [ ] [Models] **"Context Window"** — *Gen AI Masters* (10:58)
- [ ] [Models] **"PEFT and Quantization"** — *Gen AI Masters* (17:48)
- [ ] [Models] **"LoRA (Phase I - Low Rank)"** — *Gen AI Masters* (19:40)
- [ ] [Models] **"qLoRA (Quantized LoRA)"** — *Gen AI Masters* (8:10)

> **Milestone:** You can evaluate RAG systems with automated Pytest suites, benchmark models, and make informed decisions about model selection and fine-tuning approaches. You're production-ready.

---

## Skipped Videos

### Python Basics, Environment Setup & Course Intros (All Courses)

All Python fundamentals (variables, loops, OOP, Pandas, NumPy), Anaconda/VS Code installation, environment setup, course welcome/outro videos, community links, bonus lectures, resource downloads. **Why:** You already know Python. Setup is a read-the-docs task, not a video task.

**Specific skips (partial list):**
- Gen AI Masters: All Python module videos (~5 hrs), NLP module (tokenization, stemming, NER, Word2Vec, GloVe, etc.), Deep Learning module (ANN, CNN, RNN, LSTM, GRU, activation functions, backprop)
- LLM Masterclass: All Anaconda/API setup tasks, all Practice Opportunity Question/Solution pairs (self-test, not instructional), PIL/image reading basics
- Ultimate RAG: Anaconda Installation, Project Structure setup, API key setup videos
- MCP Masterclass: Environment setup, course tips, keys to success, watch in 1080p, about instructor
- RAG-LLM Evals: Python/Pytest basics sections, install Python videos
- All courses: Introduction, Conclusion/Thank You, Bonus Lecture videos

### Redundant Coverage (Picked Best Source)

| Skipped | Better Alternative in Path |
|---|---|
| Ultimate RAG: "Introduction To RAG" (13:19) | Eden Marco's RAG intro is more concise and engineer-focused |
| Ultimate RAG: "Getting Started With OPENAI Embeddings" (18:44) | Covered within ChromaDB build videos |
| Ultimate RAG: "Building a RAG System with LangChain and FAISS" (Parts 1-2, ~41 min) | ChromaDB pipeline covers same patterns; FAISS is API-similar |
| Ultimate RAG: "InMemory Vector Store" (6:59) | Trivial after learning ChromaDB |
| Ultimate RAG: "Working With Full Fledged DataStax Astra VectorDB" (20:58) | Vendor-specific; learn from docs when needed |
| Ultimate RAG: "Working With PineCone VectorStore DB" (9:08) | Same — vendor-specific |
| Ultimate RAG: All document-specific parsing (PDF, Word, CSV, Excel, JSON, SQL — ~1.5 hrs) | Format-specific loaders; reference docs when you need them |
| Ultimate RAG: "Semantic Chunking With Python" (12:46) + "Semantic Chunking With Langchain" (6:00) | "Semantic Chunking With RAG" covers the concept better |
| Ultimate RAG: "Combining Dense And Sparse Matrix" (20:16) | Theory covered by the Retriever implementation video |
| Ultimate RAG: "Benefits Of Combining Dense And Sparse Search" (7:18) | Obvious after implementation |
| Ultimate RAG: "MMR Retriever Implementation" (5:52) + MMR theory (22:15) | MMR is well-documented; re-ranking covers the concept |
| Ultimate RAG: "Query Decomposition Understanding And Implementation" (13:06) | Covered conceptually in Agentic RAG phase |
| Ultimate RAG: "MultiModal RAG Implementation" (28:07) | Specialized; learn after core path |
| Ultimate RAG: LangChain agents section (Create Agents, Invoke, Tools, Messages, Pydantic output — ~1.5 hrs) | Eden Marco covers these deeper and better |
| Ultimate RAG: LangGraph basics (Build Simple Graph, State Schema, Pydantic, Chains, Router — ~2 hrs) | Eden Marco's hands-on LangGraph section is tighter |
| Ultimate RAG: Streaming techniques (16:44 + 5:05) | Learn from docs when building UI |
| Ultimate RAG: Knowledge Graph section (Neo4j, Cypher, GraphDB — ~2.5 hrs) | Specialized topic; pursue separately if needed |
| Ultimate RAG: CAG section (~29 min) | Niche concept; not core to your 8 goals |
| Ultimate RAG: RAG With Persistent Memory (16:30 + 4:22) | Memory is covered in Phase 4; persistence is an implementation detail |
| Ultimate RAG: Final project (Streamlit app — ~1 hr) | Build your own project instead |
| Gen AI Masters: Transformer architecture section (Transformers Types, Self-Attention, Encoder/Decoder, BERT variants, GPT — ~3 hrs) | Valuable background but not in your 8 goals; read "Attention Is All You Need" instead |
| Gen AI Masters: RAG practicals and project videos (~2 hrs) | Ultimate RAG covers these more thoroughly |
| Gen AI Masters: Vector Database Practicals (30:41) | Covered in Ultimate RAG ChromaDB builds |
| Gen AI Masters: Ollama section (~1.5 hrs) | Covered briefly in Eden Marco; learn by doing |
| Gen AI Masters: Fine-Tuning theory (11:46) + LoRA Phase II/III (~21 min) | Phase I + QLoRA are the essential ones; II and III are incremental |
| Gen AI Masters: Deployment section (Flask, AWS, EC2 — ~2 hrs) | DevOps, not AI engineering; learn when deploying |
| Gen AI Masters: All project videos (~6 hrs) | Build your own projects using what you've learned |
| Gen AI Masters: Interview prep section (~1.5 hrs) | Study when preparing for interviews, not during learning |
| Gen AI Masters: N-gram Metrics (ROUGE) (7:39), (METEOR) (4:17), Intrinsic Metrics/PPL (~33 min) | BLEU + BERTScore + RAGAS covers eval needs; ROUGE/METEOR/PPL are diminishing returns |
| Gen AI Masters: RAGAS/BLEU/ROUGE/BERTScore practicals (~1.5 hrs) | RAG-LLM Evals course has better Pytest-automated versions |
| LLM Masterclass: Character AI Chatbot project (~45 min) | API basics; you already know Python |
| LLM Masterclass: AI Calorie Tracker project (~50 min) | Vision API project; not in your 8 goals |
| LLM Masterclass: Gradio/AI Tutor section (~1 hr) | UI framework; learn when needed |
| LLM Masterclass: Website generation with LLMs (~1 hr) | Demo project; not in your 8 goals |
| LLM Masterclass: Hugging Face deep dive (Pipelines, AutoTokenizer, AutoModel — ~1 hr) | Specialized HF knowledge; learn from HF docs |
| LLM Masterclass: DeepSeek reasoning section (~1.5 hrs) | Model-specific; covered conceptually by benchmarking videos |
| LLM Masterclass: RAG pipeline build (~1 hr) | Ultimate RAG covers this deeper |
| LLM Masterclass: Resume/Cover Letter project (~1.5 hrs) | Pydantic is useful but covered in Eden Marco's structured output |
| LLM Masterclass: Fine-tuning section (~1.5 hrs) | Gen AI Masters covers LoRA/QLoRA theory better |
| LLM Masterclass: AutoGen section (~45 min) | Framework-specific; not in your 8 goals |
| LLM Masterclass: LangGraph section (~1.5 hrs) | Eden Marco + Ultimate RAG cover LangGraph deeper |
| LLM Masterclass: CrewAI section (~2 hrs, includes ML regression) | Framework-specific; not in your 8 goals |
| LLM Masterclass: n8n section (~1.5 hrs) | No-code tool; not in your 8 goals |
| LLM Masterclass: MCP section (~50 min) | MCP Masterclass is comprehensive; this is surface-level |
| Hands-On RAG: PostgreSQL setup, PGAdmin, Install Requirements (~10 min) | Setup; do from docs |
| Hands-On RAG: E-Commerce Semantic Search Assignment (9:14) | Assignment walkthrough; low depth |
| Hands-On RAG: LangSmith Intro + Dashboard (~4 min) | Already covered in Eden Marco |
| Hands-On RAG: Indexing quizzes (Indexing, Indexes labels) | Quiz/assignment labels without video content; instructional videos now included in Phase 6 |
| Hands-On RAG: Evals Code Walkthrough + Return Chunks (~6 min) | Thin coverage; better in RAG-LLM Evals |
| Hands-On RAG: Metadata section (Update Schema, Ingest Metadata, Add API Support, Test — ~14 min) | "Use Metadata Filtering" captures the key concept |
| Hands-On RAG: MCP section (Project Setup through Test — ~20 min) | MCP Masterclass is the definitive source |
| MCP Masterclass: Resources/Prompts deep dives (~43 min) | Secondary MCP features; learn after core tools mastery |
| MCP Masterclass: Deployment/packaging section (~32 min) | DevOps; do when deploying |
| MCP Masterclass: Streamable HTTP VM section (~39 min) | Advanced deployment; 1 video kept for concept |
| MCP Masterclass: Server builds (Memory Tracker, Chess Stats — ~42 min) | Practice projects; build your own instead |
| MCP Masterclass: NPX connection, desktop interaction, local files (~25 min) | Supplementary tool interactions; covered by API calls video |
| RAG-LLM Evals: AI/LLM introduction videos (~27 min) | You know what LLMs are |
| RAG-LLM Evals: RAG architecture overview (~21 min) | Covered deeply in Ultimate RAG |
| RAG-LLM Evals: Practice RAG LLM demo (6:51) | Demo, not instructional |
| RAG-LLM Evals: Multi-conversation eval (~25 min) | Advanced; pursue after core evals |
| RAG-LLM Evals: Test data generation with RAGAS (~44 min) | Nice-to-have; not core |
| RAG-LLM Evals: Reusable utils video (13:18) | Covered by Pytest fixtures video |
| RAG-LLM Evals: Pytest Parameterization (10:13) | General Pytest; learn from docs |
| RAG-LLM Evals: RAGAS dashboard upload (8:21) | UI walkthrough |
| RAG-LLM Evals: Reading test data from JSON (9:58) | Python I/O; trivial |
| Eden Marco: All project-specific boilerplate/setup videos | Setup noise |
| Eden Marco: Tweet/Reflector project (defining graph, LangSmith tracing — ~26 min) | Narrow project; concepts covered in LangGraph hands-on |
| Eden Marco: Actor/Revisor agent project (~35 min) | Same patterns as ReAct hands-on |
| Eden Marco: Deep Agents section (~33 min) | Conceptually interesting but no implementation |
| Eden Marco: RAG Architecture, LangChain Hub, TextSplitting Playground, LangChain VS LlamaIndex (~15 min) | Reference material, not learning |
| Eden Marco: LLM App Sec, The Bad of Agentic Coding (~31 min) | Security/ethics; read articles instead |
| Eden Marco: MCP Inspector, LLM.txt, mcpdoc (~21 min) | Tooling walkthroughs; MCP Masterclass covers architecture better |
| Eden Marco: Tavily optional videos (Map, Extract, Crawling Deep Dive — ~42 min) | Vendor-specific; optional enrichment |
| Eden Marco: Agentic RAG boilerplate, code structure, ingestion pipeline, retrieve node (~18 min) | Setup for the agentic RAG project; concepts are in Phase 7 |

### Ambiguous Titles (Couldn't fully assess from title alone)

| Video | Course | Concern |
|---|---|---|
| "LangChain Version In Course V.1" | Eden Marco | Likely a version compatibility note, not instructional |
| "From ReAct Prompting to Modern Tool Calling" | Eden Marco | No duration listed; may be a transition slide |
| "Model Overview" | Gen AI Masters | Unclear which models; likely a general LLM overview |
| "LangChain Model Switching: Groq API Integration" | Eden Marco | No duration; may be supplementary |
| "Generative UI/UX featuring CopilotKit" | Eden Marco | Could be useful for frontend, but title is vague |
| "Connect To Vector Store / Vectorization / RAG" | Hands-On RAG | Three topics crammed into one; no duration listed |
| "Caching" (standalone) | Hands-On RAG | Duplicate section header; "Semantic Cache In Action" is the actual video |
