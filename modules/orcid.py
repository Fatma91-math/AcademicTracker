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

        try:

            response = requests.get(
                self.url,
                headers=self.headers,
                timeout=15
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException:

            return None

    def get_name(self):

        if self.data is None:
            return "Connection error"

        try:

            given = self.data["person"]["name"]["given-names"]["value"]

            family = self.data["person"]["name"]["family-name"]["value"]

            return f"{given} {family}"

        except:

            return "Unknown"

    def get_orcid_id(self):

        return self.orcid_id

    def get_works(self):

        if self.data is None:
            return 0

        try:

            return len(
                self.data["activities-summary"]["works"]["group"]
            )

        except:

            return 0

    def get_profile(self):

        return {

            "source": "ORCID",

            "name": self.get_name(),

            "orcid_id": self.get_orcid_id(),

            "works": self.get_works()

        }

    def show_profile(self):

        profile = self.get_profile()

        print("=" * 40)
        print("ORCID")
        print("=" * 40)

        print("Name      :", profile["name"])
        print("ORCID ID  :", profile["orcid_id"])
        print("Works     :", profile["works"])

        print("=" * 40)