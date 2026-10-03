import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "HallucinationDetectionProject/1.0 (student project)"
}


def retrieve_wikipedia_evidence(claim, max_results=3):

    # --------------------------------
    # Step 1: Search Wikipedia API
    # --------------------------------

    search_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": claim,
        "srlimit": max_results
    }

    response = requests.get(
        search_url,
        params=params,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("query", {}).get("search", [])

    evidence = []

    # --------------------------------
    # Step 2: Retrieve page content
    # --------------------------------

    for result in results:

        title = result["title"]

        page_url = (
            "https://en.wikipedia.org/wiki/"
            + title.replace(" ", "_")
        )

        page_response = requests.get(
            page_url,
            headers=HEADERS,
            timeout=10
        )

        page_response.raise_for_status()

        soup = BeautifulSoup(
            page_response.text,
            "html.parser"
        )

        paragraphs = soup.find_all("p")

        text = " ".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

        evidence.append({
            "title": title,
            "url": page_url,
            "content": text[:3000]
        })

    return evidence


# --------------------------------
# Test
# --------------------------------

claim = "The Eiffel Tower was completed in 1889."

results = retrieve_wikipedia_evidence(claim)

print("\nRetrieved Evidence:\n")

for i, result in enumerate(results, 1):

    print("\n" + "=" * 60)
    print(f"Evidence {i}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("\nContent:")
    print(result["content"][:1000])