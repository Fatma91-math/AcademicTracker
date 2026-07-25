from modules.scholar import ScholarScraper
from modules.orcid import OrcidScraper
from modules.storage import Storage
from modules.compare import Compare


class AcademicTracker:

    def __init__(self):
        self.storage = Storage()
        self.compare = Compare()

    def run_source(self, scraper_class, source):

        print(f"\n========== {source.upper()} ==========")

        scraper = scraper_class()

        profile = scraper.get_profile()

        old_profile = self.compare.load_profile(
            f"data/{source}/latest.json"
        )

        self.compare.compare(old_profile, profile)

        self.storage.save_profile(profile, source)

    def run(self):

        self.run_source(OrcidScraper, "orcid")

        self.run_source(ScholarScraper, "scholar")

        print("\nAcademic Tracker finished successfully.")