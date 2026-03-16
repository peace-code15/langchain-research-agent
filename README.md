# 🔍 AI Research Assistant

An AI-powered research assistant built with **LangChain** and **Ollama (LLaMA 3.1)** that autonomously searches the web and scrapes articles to answer your research topics — all through a clean **Streamlit** UI.

---

## Features

- **Web Search** — Uses DuckDuckGo to find relevant results for any topic
- **Web Scraper** — Extracts article content from URLs automatically
- **LLM Agent** — LangChain agent powered by Ollama's LLaMA 3.1 model
- **Streamlit UI** — Simple and clean interface to interact with the assistant

---

## Project Structure

```
ai-research-assistant/
├── agent.py          # LangChain agent setup with tools
├── app.py            # Streamlit frontend
├── tools.py          # Web search and scraping tools
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running locally
- LLaMA 3.1 model pulled via Ollama

```bash
# Install Ollama, then pull the model
ollama pull llama3.1
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`, enter a topic, and click **Research**!

---

## Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core agent framework |
| `langchain-ollama` | Ollama LLM integration |
| `langchain-community` | Community tools support |
| `streamlit` | Web UI |
| `duckduckgo-search` | Web search tool |
| `requests` | HTTP requests for scraping |
| `beautifulsoup4` | HTML parsing |

> **Note:** The `requirements.txt` should also include `langchain-ollama`, `duckduckgo-search`, `requests`, and `beautifulsoup4`. See the complete requirements below.

---

## Complete Requirements

```
langchain
langchain-ollama
langchain-community
streamlit
duckduckgo-search
requests
beautifulsoup4
```

---

## How It Works

```
User Input (Streamlit UI)
        ↓
  LangChain Agent (LLaMA 3.1 via Ollama)
        ↓
  ┌─────────────────────────┐
  │  Tool 1: Web Search     │  ← DuckDuckGo
  │  Tool 2: Web Scraper    │  ← BeautifulSoup
  └─────────────────────────┘
        ↓
  Final Answer → Streamlit UI
```

The agent decides autonomously which tools to use and in what order to answer the query.

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)
