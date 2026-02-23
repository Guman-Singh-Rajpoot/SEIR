import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 2:
        print("Usage: python project1.py <URL>")
        return

    url = sys.argv[1]

    
    if not url.startswith("http"):
        url = "https://" + url

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    
    title = soup.title.string if soup.title else "No Title"
    print("TITLE:\n", title)

    
    body_text = soup.get_text(separator="\n", strip=True)
    print("\nBODY TEXT:\n", body_text)
    print("\nLINKS:")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)

if __name__ == "__main__":
    main()