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

        self.soup = self.download()

    def download(self):

        try:

            response = requests.get(
                self.url,
                headers=self.headers,
                timeout=15
            )

            response.raise_for_status()

            return BeautifulSoup(response.text, "html.parser")

        except requests.RequestException:

            return None

    def get_name(self):

        if self.soup is None:
            return "Connection error"

        name = self.soup.find("div", id="gsc_prf_in")

        return name.text.strip() if name else "Unknown"

    def get_statistics(self):

        stats = {
            "citations": 0,
            "h_index": 0,
            "i10_index": 0
        }

        if self.soup is None:
            return stats

        values = self.soup.find_all("td", class_="gsc_rsb_std")

        try:
            stats["citations"] = int(values[0].text.replace(",", ""))
            stats["h_index"] = int(values[2].text)
            stats["i10_index"] = int(values[4].text)
        except (IndexError, ValueError):
            pass

        return stats

    def get_article_count(self):

        if self.soup is None:
            return 0

        return len(self.soup.find_all("a", class_="gsc_a_at"))

    def get_profile(self):

        stats = self.get_statistics()

        return {
            "source": "Google Scholar",
            "name": self.get_name(),
            **stats,
            "article_count": self.get_article_count()
        }

    def show_profile(self):

        profile = self.get_profile()

        print("=" * 40)
        print("GOOGLE SCHOLAR")
        print("=" * 40)

        print("Name         :", profile["name"])
        print("Citations    :", profile["citations"])
        print("h-index      :", profile["h_index"])
        print("i10-index    :", profile["i10_index"])
        print("Articles     :", profile["article_count"])

        print("=" * 40)