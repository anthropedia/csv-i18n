import csv


class Translator:
    def __init__(self, filename):
        reader = open(filename, 'r')
        self.content = tuple(csv.reader(reader))
        reader.close()

    def translate(self, sentence, **kwargs):
        for row in self.content:
            if row[0] == sentence:
                for key, value in kwargs.items():
                    row[1] = row[1] % {key: value}
                return row[1]
