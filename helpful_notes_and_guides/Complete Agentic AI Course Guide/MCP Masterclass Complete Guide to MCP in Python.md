Why does MCP exist?
5:15
Course Tips
0:44
History and benefits of MCP
8:19
What is MCP?
3:53
What is this course?
3:20
Course roadmap
5:34
About the instructor
1:10
Keys to success
2:08
Ways to reach out
0:53
Leave a rating
0:56
Watch in 1080p
0:50
MCP architecture deep dive with agents and LLMs
9:23
MCP server deep dive with tools
3:05
Full MCP client and server workflow chain
6:18
Other MCP primitives (resources and prompts)
8:02
FastMCP vs. lowlevel server
5:14
Local vs. Remote MCPs - Stdio vs. Streamable HTTP
9:37
Environment setup
9:16
Resources
3:33
Simple Claude and Airbnb MCP example
9:21
Create a simple MCP Server 1
9:13
Create a simple MCP Server 2
15:42
Connect an MCP Client to an MCP Server locally built
15:05
Connect an MCP Client to an MCP Server using NPX
6:28
MCP Server and local files 1
10:27
MCP Server and local files 2
4:22
Using MCP Servers to interact with your desktop
9:42
Using MCP Servers to make API calls
12:52
Using MCP Servers with other AI models or web search
13:46
Complex inputs with MCP Servers
11:05
Introduction to MCP Resources and Prompts
6:29
Prompts deep dive
12:42
Resources deep dive
12:50
Resources deep dive with inputs
11:26
Introduction to MCP deployment
10:03
Create and package an MCP Server
8:08
Deploy MCP Server to package manager like Git
14:05
Introduction to remote MCP servers with Streamable HTTP
4:45
Create and host a Streamable HTTP MCP Server in a virtual machine
8:08
Connect MCP Client to Streamable HTTP MCP Server
5:05
Put MCP Server in virtual machine
14:40
Connect to MCP Server Streamable HTTP with MCP Inspector
2:46
Connect to MCP Server Streamable HTTP with MCP Client
7:49
Introduction to MCP Clients
4:08
MCP Client session class
3:46
Listing and calling tools from MCP clients to MCP servers
12:10
Listing and calling resources from MCP clients to MCP servers
12:41
Listing and calling prompts from MCP clients to MCP servers
4:35
Process query in MCP Client - Connect LLMs and MCP Servers 1
13:02
Process query in MCP Client - Connect LLMs and MCP Servers 2
9:44
MCP Server Build Memory Tracker 1
11:12
MCP Server Build Memory Tracker 2
12:15
MCP Server Build Chess Stats 1
14:17
MCP Server Build Chess Stats 2
4:25
MCP Client Build Multi MCP Server Example 1
19:51
MCP Client Build Multi MCP Server Example 2
4:29
Conclusion and certificate
0:58
Bonus
2:38
Requirements
Basic understanding and familiarity with Python
Basic understanding and familiarity with how APIs work is helpful but not needed
Basic understanding and familiarity of Git and GitHub
Windows or Mac
Description
What makes this course different than others?

Complete Guide: this is not a bootcamp or "crash" course - this is the only complete guide that takes you from knowing nothing about MCPs, to understanding the architecture and protocol, to an MCP expert building MCP Servers and Clients. You get ~8 hours of content!

Focus on Python: the SDK we use here is completely in Python (instead of Javascript or Typescript). However, since all the SDKs are similar, what you learn here will be applicable to all SDKs.

Up to date: this course incorporates all the latest updates and technologies, including the new Streamable HTTP transport

From Theory to Build: this course starts on the theory and architecture behind MCPs, why they exist, how they work, their history so that you get a solid understanding. After that, we focus on the features around MCP Servers and Clients and applying it as we build with MCP

MCP Servers and Clients: this course builds both MCP servers and clients (most content just stops at servers)

Build 4+ MCP Servers and Clients: we build several MCP servers and clients from scratch



MCPs are taking over the world because they solve a critical problem. LLM applications are great at generating content but they lack taking action. Tools and Function Calling were meant to address this, but LLM frameworks apply this differently and many developers had to "reinvent the wheel" every single time they started building an LLM application.



Consensus was needed and MCP was born. 



Since then, MCP has taken off, being adopted fully by Microsoft, OpenAI, Anthropic, and so much more. Thousands of companies have built their own MCP servers, and tens of thousands of developers have built MCP servers that interact with an API or compute some process locally. In fact, MCP was one of the highest search terms in Q1-Q2 2025 (after AI Agents).



This course is all about taking you from knowing nothing about MCPs to becoming an MCP master. By the end of this course, you will be able to build your own MCP Servers and Clients from scratch, deploy them locally or on a virtual machine, distribute them using GitHub or NPM, and learn / master all of MCPs architecture and features.



Note that we focus on the Python SDK when building MCP Servers and Clients.



What's MCP?

MCP is a standardized mechanism (i.e., protocol) for AI systems (like LLMs, agents, etc.) to interact with external systems (like APIs, tool logic, local processes, etc.). Think of it as a universal USB-C connector for AI systems and everything that needs to connect to AI systems.



Why MCP?

One word: standardization. Once you build an MCP Server, it can easily connect to thousands of different applications / LLMs / Agents that contain an MCP Client. Similarly, if you build an MCP Client, it can easily connect to tens of thousands of MCP Servers.



What is this course all about?

This course has one goal - to taking you from knowing nothing about MCPs to becoming an MCP master. Ultimately, this means going through MCPs vast set of features and learning how to apply them into your own applications. We will build MCP Servers and Clients from scratch and deploy / distribute them both locally and remotely.

This course is hands-on, practical, and tailored for enthusiasts / developers seeking how to build real-world MCP Servers and MCP Clients. Note that the SDK we use is Python in Windows/Mac and the MCP Hosts we use in this course are VS Code and Anthropic Claude.



What will you learn?

Understand MCP architecture - learn how MCP Clients and MCP Servers interact with each other in detail

Learn, master, and apply all MCP features - deep dive into all of MCP features, including tools, resources, prompts, transport protocol, STDIO, streamable https, and so much more

Build MCP Servers and Clients - build several real-world practical MCP Servers and Clients from scratch, and combine them with LLMs to create powerful LLM applications

Publish, and host your own MCP Server or MCP Client - distribute and publish your own MCP Servers and MCP Clients



Why choose this course?

Complete guide - this is the 100% start to finish, zero to hero, basic to advanced guide on building MCP Servers and Clients. There is no other course like it that teaches you everything from start to finish. It contains ~8 hours of instructional content!

Structured to succeed - this course is structured to help you succeed by learning the theory and actually applying it. We also focus on both architecture, servers, clients, and deployment.

Fully instructional - we not only go through important concepts, but also apply them as we are building our application so that we can solidify them. This is not only a walkthrough of the all the features and theoretical concepts, but a course that actually uses real-life examples and integrations

Step by step - we go through every single concept one-by-one. This improves your probabilities of learning MCP rather than going haphazardly through each feature

Teacher response - if there's anything else you would like to learn, or if there's something you cannot figure out, I'm here for you! Look at the ways to reach out video

Resources - you get access to all the code and slides in this course, plus several notes and guides



Course Overview

MCP Introduction – Understand why MCP exists, its origins, what it enables, and a breakdown of the full course roadmap.

MCP Architecture Overview – Dive into how MCP works with agents and LLMs, the client-server workflow, server primitives like resources/prompts, and the difference between FastMCP, Stdio, and Streamable HTTP setups.

MCP Environment Setup – Get your local development environment ready with Claude, Python, Git, and VS Code, and access key course resources.

MCP Quickstart – Build your first working MCP system (both Server and Client) with Claude and a simple tool (like an Airbnb example), covering both local and NPX-based setups.

MCP Server Deep Dive - Tools – Learn how MCP servers interact with your local files, APIs, external models, and how to structure more complex inputs.

MCP Server Deep Dive - Resources and Prompts – Explore how to expose reusable resources and prompts from your MCP server, and how to structure them for input-output handling.

MCP Server Deep Dive - Deployment and Publishing – Package your MCP server for reuse and publish it to platforms like GitHub to share or deploy in real-world scenarios.

MCP Server Deep Dive - STDIO vs. Streamable HTTP – Understand remote server options, how to build and host Streamable HTTP servers, and connect clients using MCP Inspector and virtual machines.

MCP Client Deep Dive – Go under the hood of MCP Clients, how they manage sessions, call tools/resources/prompts, and integrate with LLMs for full processing flows.

MCP End-to-End Builds – Build real-world projects like a memory tracker and chess stats server, and create MCP Clients that connect to multiple servers.

MCP Conclusion and Certificate – Wrap up your MCP journey, celebrate your accomplishment, and learn how to access your course certificate.

Who this course is for:
Developers and engineers who are building agentic AI applications or LLM-powered tools
Automation professionals and tech enthusiasts who are looking to connect AI with external tools or APIs
AI builders who’ve hit limits with their current tools and want to build MCP Servers and Clients
Founders or indie hackers exploring AI-native apps and toolchains
Anyone who loves clean protocols, open standards, and the phrase “build once, run everywhere"
AI Enthusiasts who want to start building with MCPs