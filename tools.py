from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup


def web_search(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)

        output = ""
        for r in results:
            output += f"{r['title']} - {r['href']}\n"

        return output


def scrape_article(url):

    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs])

        return text[:2000]

    except Exception as e:
        return str(e)