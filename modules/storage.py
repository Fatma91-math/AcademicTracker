import json
import os
from datetime import datetime


class Storage:

    def save_profile(self, profile, source):
        base_folder = os.path.join("data", source)
        history_folder = os.path.join(base_folder, "history")

        os.makedirs(history_folder, exist_ok=True)

        latest_file = os.path.join(base_folder, "latest.json")

        today = datetime.now().strftime("%Y-%m-%d")

        history_file = os.path.join(history_folder, f"{today}.json")

        with open(latest_file, "w", encoding="utf-8") as file:
            json.dump(profile, file, indent=4, ensure_ascii=False)

        with open(history_file, "w", encoding="utf-8") as file:
            json.dump(profile, file, indent=4, ensure_ascii=False)

        print("Profile saved successfully.")