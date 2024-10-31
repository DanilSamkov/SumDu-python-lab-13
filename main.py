import csv
import json

# Частина коду написана студентом КН-32/2 Самковим Данилом Олександровичем
# Генерація CSV файлу
def generate_csv(filename):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["first_name", "last_name", "age", "course", "average_score"])
            writer.writerow(["Царук", "Науменко", 20, 2, 4.5])
            writer.writerow(["Яснолик", "Улинець", 19, 1, 4.7])
            writer.writerow(["Романа", "Ничипоренко", 21, 3, 4.3])
        print(f"CSV файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при записі CSV файлу: {e}")

# Конвертація CSV у JSON
def convert_csv_to_json(csv_filename, json_filename):
    data = {"students": []}
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data["students"].append(row)
        with open(json_filename, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
        print(f"JSON файл '{json_filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при роботі з файлами: {e}")

def main():
    csv_filename = "students.csv"
    json_filename = "students.json"

    generate_csv(csv_filename)
    convert_csv_to_json(csv_filename, json_filename)

if __name__ == "__main__":
    main()


