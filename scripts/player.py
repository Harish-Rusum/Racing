class Player:
    def __init__(self, color, size, model, selections):
        self.color = color
        self.model = model
        self.size = size
        self.img = selections[self.color][self.size][self.model]

