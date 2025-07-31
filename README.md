# 🧠 Autonomous AI Agent for Web Research

This project implements an **autonomous AI research assistant** that leverages language models (LLMs), web search tools, and Wikipedia to answer user queries and automatically save structured results to a text file.

---

## 🚀 What It Does

This system allows a user to ask a research question in natural language. Then:

1. The agent interprets the query.
2. It uses tools such as:
   - 🔍 Web search (via DuckDuckGo using `ddgs`)
   - 📚 Wikipedia lookups
   - 💾 Automatic saving of the results to a `.txt` file
3. It returns a structured response including:
   - Topic
   - Summary
   - Sources used
   - Tools invoked

---

## 🧰 Technologies Used

| Tool/Library            | Description |
|-------------------------|-------------|
| [LangChain](https://github.com/langchain-ai/langchain) | Framework for building autonomous agents and toolchains |
| `langchain_openai`      | Integration with OpenAI models (e.g., GPT-4o-mini) |
| `ddgs`                  | DuckDuckGo search library (privacy-friendly web search) |
| `WikipediaAPIWrapper`   | Wrapper for fetching content from Wikipedia |
| `Pydantic`              | Ensures structured response validation |
| `dotenv`                | Loads environment variables like API keys |
| Standard Python         | Used for file handling, timestamps, and core logic |
