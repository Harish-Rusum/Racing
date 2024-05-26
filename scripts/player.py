class Player:
    def __init__(self, color, size, model, selections):
        print(color,size,model)
        self.color = color
        self.model = model
        self.size = size
        self.img = selections[self.color][self.size][self.model-1]

    def render(self, x, y, surface):
        surface.blit(self.img, (x, y))
