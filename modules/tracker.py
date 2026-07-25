from modules.scholar import ScholarScraper
from modules.orcid import OrcidScraper
from modules.storage import Storage
from modules.compare import Compare
from modules.report import Report
from modules.dashboard import Dashboard


class AcademicTracker:

    def __init__(self):

        self.storage = Storage()
        self.compare = Compare()
        self.report = Report()
        self.dashboard = Dashboard()

    def run_source(self, scraper_class, source):

        print(f"\n========== {source.upper()} ==========")

        scraper = scraper_class()

        profile = scraper.get_profile()

        old_profile = self.compare.load_profile(
            f"data/{source}/latest.json"
        )

        self.compare.compare(
            old_profile,
            profile
        )

        self.report.create_report(
            source,
            old_profile,
            profile
        )

        self.storage.save_profile(
            profile,
            source
        )

    def run(self):

        # ORCID məlumatlarını yenilə
        self.run_source(
            OrcidScraper,
            "orcid"
        )

        # Google Scholar məlumatlarını yenilə
        self.run_source(
            ScholarScraper,
            "scholar"
        )

        # Bütün məlumatlar yeniləndikdən sonra Dashboard yarat
        self.dashboard.create_dashboard()

        print("\nDashboard created successfully.")

        print("\nAcademic Tracker finished successfully.")