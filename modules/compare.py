import json
import os


class Compare:

    def load_profile(self, filepath):

        if not os.path.exists(filepath):
            return None

        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    def compare(self, old_profile, new_profile):

        print("\n" + "=" * 60)
        print("PROFILE COMPARISON")
        print("=" * 60)

        if old_profile is None:

            print("First run. No previous profile found.")
            print("=" * 60)

            return

        for key in new_profile:

            if key == "source":
                continue

            old_value = old_profile.get(key)
            new_value = new_profile.get(key)

            print(f"\n{key.upper()}")

            print(f"Previous : {old_value}")
            print(f"Current  : {new_value}")

            if old_value == new_value:

                print("Status   : No Change")

            elif isinstance(old_value, (int, float)) and isinstance(new_value, (int, float)):

                diff = new_value - old_value

                if diff > 0:

                    print(f"Change   : +{diff}")

                elif diff < 0:

                    print(f"Change   : {diff}")

                else:

                    print("Status   : No Change")

            else:

                print("Status   : Changed")

        print("=" * 60)

    def get_changes(self, old_profile, new_profile):

        """
        Dashboard və Report modulu üçün dəyişiklikləri qaytarır.
        """

        changes = {}

        if old_profile is None:
            return changes

        for key in new_profile:

            if key == "source":
                continue

            old_value = old_profile.get(key)
            new_value = new_profile.get(key)

            if (
                isinstance(old_value, (int, float))
                and isinstance(new_value, (int, float))
            ):

                changes[key] = new_value - old_value

            else:

                if old_value == new_value:
                    changes[key] = 0
                else:
                    changes[key] = None

        return changes