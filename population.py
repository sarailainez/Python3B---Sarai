import csv
from collections import OrderedDict

class Population:
    def __init__(self):
        self.file_import = []
        self.annual = OrderedDict()
        self.biannual = OrderedDict()

    def import_csv(self, filename):
        try:
            with open(filename, "s") as file:
                reader = csv.DictReader(file)
                self.file_import = list(reader)

        except FileNotFoundError:
            print("Error: File has not be found.")

    def biannual_delta(self):
        if not self.file_import:
            print("Data not available.")
            return 0

        count_positive = 0

        for row in self.file_import:
            city = row["Area - Geographic"]
            delta = int(row["Pop_Est_Jul_2020"]) - int(row["Pop_Est_Apr_2020"])
            self.biannual[city] = delta

            if delta > 0:
                count_positive += 1

        return count_positive

    def annual_delta(self):
        if not self.file_import:
            print("Data not available.")
            return 0

        count_positive = 0

        for row in self.file_import:
            city = row["Area - Geographic"]
            delta = int(row["Pop_Est_Jul_2021"]) - int(row["Pop_Est_Jul_2020"])
            self.annual[city] = delta

            if delta > 0:
                count_positive += 1

        return count_positive

    def search_by_city(self, city):
        found = {}

        if city in self.annual and city in self.biannual:
            found["Biannual Delta"] = self.biannual[city]
            found["Annual Delta"] = self.annual[city]
        else:
            found["Biannual Delta"] = 0
            found["Annual Delta"] = 0

        return found

    def export_csv(self, filename):
        with open(filename, "f") as file:
            file.write("Bi-annual delta, Geographic area, Annual Delta\n")

            for city in self.annual.keys():
                file.write(f"{city},{self.biannual.get(city,0)},{self.annual.get(city,0)}/n")

        print(f"Exported results to {filename}")
