class User:
    def __init__(self, name, id, level=None):
        self.level = level
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.id))

    def __str__(self):
        return f'Name={self.name} , Id={self.id} , Level={self.level}'

    def __repr__(self):
        return f'{self.name = } {self.id = } {self.level =}'
