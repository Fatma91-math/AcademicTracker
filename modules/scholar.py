import requests
from bs4 import BeautifulSoup


class ScholarScraper:

    def __init__(self):
        self.url = "https://scholar.google.com/citations?user=dg2nm6MAAAAJ&hl=en"

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

    def download(self):
        response = requests.get(
            self.url,
            headers=self.headers
        )

        return BeautifulSoup(response.text, "html.parser")

    def get_name(self):
        soup = self.download()

        name = soup.find("div", id="gsc_prf_in")

        return name.text.strip()

    def get_articles(self):
        soup = self.download()

        articles = soup.find_all("a", class_="gsc_a_at")

        article_list = []

        for article in articles:
            article_data = {
                "title": article.text.strip()
            }

            article_list.append(article_data)

        return article_list