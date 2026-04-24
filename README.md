## Author

Built by **Dhiraj Rupnawar**

# Intellexa AI — Research Intelligence Platform

> A multi-agent AI pipeline that searches, scrapes, writes, and critiques research reports — fully automated.

---

## Overview

Intellexa AI is a Streamlit-based web application powered by a LangChain multi-agent pipeline. Given any research topic, four specialized AI agents collaborate in sequence to produce a polished, peer-reviewed research report in minutes.

```
Search Agent → Reader Agent → Writer Chain → Critic Chain → Final Report
```

---

## Features

- **4-Agent Pipeline** — each agent has a focused, isolated role
- **Live Web Search** — search agent retrieves real-time, reliable information
- **Deep Content Extraction** — reader agent scrapes and parses top sources
- **Structured Report Generation** — writer produces a clean, well-formatted markdown report
- **AI-Powered Critique** — critic scores and reviews the report for quality and accuracy
- **Download as Markdown** — export any report with one click
- **Professional UI** — editorial light-mode design with real-time pipeline status

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Agent Framework | LangChain |
| LLM | OpenAI / Anthropic (configurable) |
| Web Search | Tavily / SerpAPI (configurable) |
| Scraping | LangChain document loaders |
| Language | Python 3.10+ |

---

## Project Structure

```
intellexa-ai/
├── app.py               # Main Streamlit UI
├── agents.py            # Agent and chain definitions
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── README.md
```

---

## Agents

### 1. Search Agent
Uses a web search tool to find recent, reliable information about the given topic. Returns a summarized list of findings with source references.

### 2. Reader Agent
Takes the top URL from the search results, scrapes the page, and extracts structured content — going deeper than the search snippet alone.

### 3. Writer Chain
Combines the search results and scraped content into a comprehensive research report. The report includes an introduction, key findings, analysis, and conclusion.

### 4. Critic Chain
Reviews the writer's report and returns structured feedback: a quality score, strengths, weaknesses, and suggestions for improvement.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/intellexa-ai.git
cd intellexa-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your API keys:

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Requirements

```
streamlit>=1.35.0
langchain>=0.2.0
langchain-openai>=0.1.0
langchain-community>=0.2.0
tavily-python>=0.3.0
python-dotenv>=1.0.0
```

---

## Usage

1. Open the app in your browser
2. Enter a research topic in the input field (e.g. *"Quantum computing breakthroughs in 2025"*)
3. Click **Run Research Pipeline**
4. Watch each agent complete its task in real time via the pipeline status panel
5. Read the final report and critic feedback in the results section
6. Download the report as a `.md` file if needed

---

## Configuration

You can swap out the underlying LLM or search tool by editing `agents.py`:

```python
# Change the LLM
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

# Change the search tool
from langchain_community.tools.tavily_search import TavilySearchResults
search_tool = TavilySearchResults(max_results=5)
```

---

## Roadmap

- [ ] Multi-URL reader (scrape top 3 sources, not just 1)
- [ ] Export report as PDF
- [ ] Save and browse past reports
- [ ] Support for local LLMs via Ollama
- [ ] Configurable agent parameters from the UI

---

## License

MIT License. See `LICENSE` for details.

---



---

*Intellexa AI · LangChain Multi-Agent Pipeline · Powered by Streamlit*
