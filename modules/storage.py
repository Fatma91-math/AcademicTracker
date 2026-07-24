import json


class Storage:

    def save_json(self, data, filename="profile.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"{filename} uğurla yaradıldı.")