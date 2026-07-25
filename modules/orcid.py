import requests


class OrcidScraper:

    def __init__(self):
        self.orcid_id = "0009-0001-9214-8357"

        self.url = f"https://pub.orcid.org/v3.0/{self.orcid_id}"

        self.headers = {
            "Accept": "application/json"
        }

        self.data = self.download()

    def download(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("ORCID məlumatları yüklənmədi.")
            return None

    def get_name(self):
        try:
            given = self.data["person"]["name"]["given-names"]["value"]
            family = self.data["person"]["name"]["family-name"]["value"]
            return f"{given} {family}"
        except:
            return "Unknown"

    def get_orcid_id(self):
        return self.orcid_id

    def get_profile(self):
        profile = {
            "name": self.get_name(),
            "orcid_id": self.get_orcid_id()
        }

        return profile