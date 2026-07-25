import json
import os
from datetime import datetime


class Storage:

    def __init__(self):

        self.data_folder = "data"

        os.makedirs(
            self.data_folder,
            exist_ok=True
        )

    def save_profile(self, profile, source):

        base_folder = os.path.join(
            self.data_folder,
            source
        )

        history_folder = os.path.join(
            base_folder,
            "history"
        )

        os.makedirs(
            history_folder,
            exist_ok=True
        )

        latest_file = os.path.join(
            base_folder,
            "latest.json"
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        history_file = os.path.join(
            history_folder,
            f"{timestamp}.json"
        )

        with open(
            latest_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                profile,
                file,
                indent=4,
                ensure_ascii=False
            )

        with open(
            history_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                profile,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"{source.upper()} profile saved successfully.")

    def load_latest(self, source):

        latest_file = os.path.join(
            self.data_folder,
            source,
            "latest.json"
        )

        if not os.path.exists(latest_file):

            return None

        with open(
            latest_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def load_history(self, source):

        history_folder = os.path.join(
            self.data_folder,
            source,
            "history"
        )

        if not os.path.exists(history_folder):

            return []

        history = []

        files = sorted(os.listdir(history_folder))

        for file in files:

            if not file.endswith(".json"):
                continue

            filepath = os.path.join(
                history_folder,
                file
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                profile = json.load(f)

            history.append(profile)

        return history