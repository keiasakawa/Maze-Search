class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'left': True, 'bottom': True, 'right': True}
        self.visited = False

    def __str__(self):
        return f'Cell({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Cell({self.x}, {self.y})'