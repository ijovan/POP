import csv
import os


class CSVFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def exists(self):
        return os.path.isfile(self.file_path)

    def write(self, rows):
        with open(self.file_path, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in rows:
                writer.writerow(row)

    def append(self, rows):
        with open(self.file_path, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in rows:
                writer.writerow(row)

    def read(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            return [row for row in reader]
