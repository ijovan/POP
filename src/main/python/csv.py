import csv


class CSV:
    def write(file_name, rows):
        with open(file_name, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in rows: writer.writerow(row)

    def append(file_name, rows):
        with open(file_name, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in rows: writer.writerow(row)

    def read(file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            return [row for row in reader]
