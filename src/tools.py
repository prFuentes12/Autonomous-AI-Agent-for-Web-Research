from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from datetime import datetime
from langchain.tools import Tool
from ddgs import DDGS


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

def run_ddgs_search(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query)
        summaries = []
        for r in results:
            summaries.append(f"{r['title']}: {r['body']} ({r['href']})")
        return "\n".join(summaries[:3])  # limita a 3 resultados

search_tool = Tool(
    name="search",
    func=run_ddgs_search,
    description="Search the web using DDGS"
)

api_wrapper = WikipediaAPIWrapper (top_k_results=2, doc_content_chars_max=1000)
wiki_tool= WikipediaQueryRun(api_wrapper=api_wrapper)

