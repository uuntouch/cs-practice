import os
from tablestats import read_rows, count_types, total_minutes, to_csv

def main():
    filename = input().strip()
    path = filename

    with open(path, encoding='utf-8') as table:
        rows = read_rows(table)

    counts = count_types(rows)

    total_records = len(rows)

    unique_types = len(counts)

    error_minutes = total_minutes(rows, 'ошибка')

    print(total_records)
    print(unique_types)
    print(error_minutes)

    csv_summary = to_csv(counts)

    with open('summary.csv','w',encoding='utf-8') as out:
        out.write(csv_summary)

if __name__ == '__main__':
    main()