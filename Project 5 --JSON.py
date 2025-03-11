import csv
import json


def read_csv_file(filename):
    """csv file with netflix tv shows"""
    tv_shows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tv_show = {
                "show_id": row["show_id"],
                "title": row["title"],
                "country": row["country"],
                "date_added": row["date_added"],
                "duration": row["duration"]
            }
            tv_shows.append(tv_show)
    return tv_shows


def write_json_file(data, output_filename):
    """JSON file - Data """
    with open(output_filename, '-w-') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4) + "\n")


def main():
    input_filename = 'tv_shows.csv'
    output_filename = 'tv_shows.json'

    print("Loading CSV file:")
    tv_shows = read_csv_file(input_filename)

    print("Writing JSON file: ")
    write_json_file(tv_shows, output_filename)

    print(f" your JSON file '{output_filename}' is ready!:)")


if __name__ == "__main__":
    main()
