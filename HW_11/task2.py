class Archive:
    """Class Archive: atr - text, num, ls"""
    listArchive = []

    def __init__(self, num, text):
        self.text = text
        self.num = num
        Archive.listArchive.append(self)
        self.ls = Archive.listArchive

    def __repr__(self):
        str_ls = ', '.join(str(el) for el in Archive.listArchive)
        return f'{self.num = } {self.text = } {str_ls = }'

    def __str__(self):
        return f'число {self.num} строка {self.text}'