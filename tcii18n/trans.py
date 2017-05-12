import csv


def _(sentence, **kwargs):
    with open('test/fixtures.fr.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == sentence:
                for key, value in kwargs.items():
                    row[1] = row[1] % {key: value}
                return row[1]
