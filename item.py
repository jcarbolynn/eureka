class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.fixed = False
        self.moved = False
        self.wearable = False
        self.concealed = False
