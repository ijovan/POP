import csv


class CSV:
    @staticmethod
    def write(file_name, rows):
        with open(file_name, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

            for row in rows:
                writer.writerow(row)
