import json
import os


class Compare:

    def load_profile(self, filename):

        if not os.path.exists(filename):
            return None

        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def compare(self, old_profile, new_profile):

        if old_profile is None:
            print("No previous data found.")
            return

        print("=" * 40)

        for key in new_profile:

            old_value = old_profile.get(key)
            new_value = new_profile.get(key)

            print(f"\n{key}")

            if old_value == new_value:

                print(f"Current : {new_value}")
                print("Status  : No change")

            else:

                print(f"Previous : {old_value}")
                print(f"Current  : {new_value}")

                if isinstance(old_value, (int, float)) and isinstance(new_value, (int, float)):
                    diff = new_value - old_value

                    if diff >= 0:
                        print(f"Change   : +{diff}")
                    else:
                        print(f"Change   : {diff}")

                else:
                    print("Status   : Changed")

        print("=" * 40)