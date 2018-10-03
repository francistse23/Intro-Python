class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        if len(self.name.split()) > 1:
            return 'Item name should be one word only.'
        else:
            return f'{self.name}: {self.description}'