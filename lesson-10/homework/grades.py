import csv
from collections import defaultdict

def read_grades(filename):
    grades = []
    with open(filename, mode = 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            grades.append({
                "Name": row["Name"],
                "Subject": row["Subject"],
                "Grade": int(row["Grade"])
            })
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(list)
    for grade in grades:
        subject_totals[grade["Subject"]].append(grade["Grade"])

    averages = {}
    for subject, grades_list in subject_totals.items():
        averages[subject] = sum(grades_list) / len(grades_list)
    return averages

def write_averages(filename, averages:dict):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg_grade in averages.items():
            writer.writerow([subject, avg_grade])

if __name__ == "__main__":
    grades_csv = "grades.csv"
    with open(grades_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Subject", "Grade"])
        writer.writerows([
            ["Alice","Math","85"],
            ["Bob","Science","78"],
            ["Carol","Math","92"],
            ["Dave","History","74"]
        ])
    grades = read_grades(grades_csv)
    averages = calculate_average(grades)
    averages_csv = "average_grades.csv"
    write_averages(averages_csv, averages)
    print("Average grades written to file:", averages_csv)