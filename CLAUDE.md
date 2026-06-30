# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **LLM Universe** (动手学大模型应用开发), an educational tutorial from Datawhale that teaches beginners how to build LLM-powered applications. The course project is building a **Personal Knowledge Base Assistant** (RAG application). Target audience: developers with basic Python, no AI/ML background required.

## Repository structure and dual-source system

This repo maintains **two parallel content trees** that must stay in sync:

- `notebook/` — **Source of truth** for course content. Jupyter notebooks (`.ipynb`) organized by chapter (C1–C7). This is where editing happens.
- `docs/` — Mirror of notebook content as standalone Markdown (`.md`), served via Docsify at `datawhalechina.github.io/llm-universe/`. When notebook content changes, corresponding docs/ markdown should be updated too.

Other key directories:
- `data_base/knowledge_db/` — Source documents for the RAG knowledge base (multiple formats: PDF, Markdown, JSON, TXT, SRT, VTT)
- `data_base/vector_db/chroma/` — Pre-built Chroma vector store (SQLite)
- `figures/` — Images shared across notebooks and docs

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit RAG app
cd "notebook/C4 构建 RAG 应用" && streamlit run streamlit_app.py

# For advanced RAG notebooks (C7), use its own requirements
pip install -r "notebook/C7 高级 RAG 技巧/requirements.txt"
```

There is no build step, test suite, or linting configuration in this project.

## Key patterns

### Custom LangChain wrappers for Chinese LLM providers

The project wraps Chinese LLM APIs to match LangChain's interfaces so they can be used interchangeably with OpenAI:

- `notebook/C3 搭建知识库/zhipuai_embedding.py` — Custom ZhipuAI embeddings class for LangChain
- `notebook/C3 搭建知识库/sparkai_embedding.py` — Custom iFlytek Spark embeddings class for LangChain
- `notebook/C4 构建 RAG 应用/zhipuai_llm.py` — Custom ZhipuAI chat model for LangChain (with streaming support)

When adding a new LLM provider, follow this pattern: implement the relevant LangChain base class (e.g., `BaseLLM`, `BaseChatModel`, `Embeddings`).

### Multi-provider API abstraction

`.env` holds API keys for all supported providers: OpenAI, Baidu Qianfan (ERNIE), iFlytek Spark, ZhipuAI GLM. Code samples in notebooks typically show how to call all four, with the user enabling whichever they have keys for. This means notebooks often contain if/else branches or commented-out sections for different providers.

### Chapter flow

Part 1 (C1–C5, complete): C1 is a `.md` file (theory), C2–C5 are `.ipynb` notebooks that build toward the RAG app incrementally. Each chapter depends on concepts from the previous one.

Part 2 (C7, in progress): Advanced RAG techniques — data processing, retrieval optimization. Uses separate `requirements.txt`.

## User notes

The user maintains personal Obsidian notes for this course at `/mnt/e/Obsidian/obsidian/AI/动手学大模型应用开发/`. These are Markdown files organized by chapter (e.g., `C2_LLM API开发.md`). When the user asks to organize or create notes, write to this path.
