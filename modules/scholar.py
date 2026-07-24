import requests
from bs4 import BeautifulSoup


class ScholarScraper:

    def __init__(self):

        self.url = "https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=dg2nm6MAAAAJ"

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

        self.soup = self.download()

    def download(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")

        return None

    def get_name(self):
        if self.soup is None:
            return "Connection error"

        name = self.soup.find("div", id="gsc_prf_in")

        if name:
            return name.text.strip()

        return "Name not found"

    def get_affiliation(self):
        if self.soup is None:
            return "Connection error"

        affiliation = self.soup.find("div", class_="gsc_prf_il")

        if affiliation:
            return affiliation.text.strip()

        return "Not found"

    def get_citations(self):
        if self.soup is None:
            return "Connection error"

        values = self.soup.find_all("td", class_="gsc_rsb_std")

        if len(values) >= 1:
            return values[0].text.strip()

        return "Not found"

    def get_h_index(self):
        if self.soup is None:
            return "Connection error"

        values = self.soup.find_all("td", class_="gsc_rsb_std")

        if len(values) >= 3:
            return values[2].text.strip()

        return "Not found"

    def get_i10_index(self):
        if self.soup is None:
            return "Connection error"

        values = self.soup.find_all("td", class_="gsc_rsb_std")

        if len(values) >= 5:
            return values[4].text.strip()

        return "Not found"

    def get_articles(self):
        if self.soup is None:
            return []

        articles = []

        titles = self.soup.find_all("a", class_="gsc_a_at")

        for title in titles:
            articles.append(title.text.strip())

        return articles

    def get_profile(self):
        profile = {
            "name": self.get_name(),
            "affiliation": self.get_affiliation(),
            "citations": self.get_citations(),
            "h_index": self.get_h_index(),
            "i10_index": self.get_i10_index(),
            "articles": self.get_articles()
        }

        return profile
    def show_profile(self):
        print("=" * 40)
        print("Google Scholar Profile")
        print("=" * 40)
        print("Name        :", self.get_name())
        print("Affiliation :", self.get_affiliation())
        print("Citations   :", self.get_citations())
        print("h-index     :", self.get_h_index())
        print("i10-index   :", self.get_i10_index())

        print("\nArticles")
        print("-" * 40)

        articles = self.get_articles()

        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article}")

        print("=" * 40)