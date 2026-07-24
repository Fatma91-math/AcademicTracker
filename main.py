from modules.scholar import ScholarScraper
from modules.storage import Storage

scholar = ScholarScraper()
storage = Storage()

profile = scholar.get_profile()

storage.save_json(profile)