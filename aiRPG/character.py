

class character(object):
    def __init__(self,grid_world):
        self.x = 0
        self.y = 9
        self.id = 3
        self.grid = grid_world

    def update(self):
        print("Updating")
        if self.y > 1:
            self.y -= 1
            print(self.y)

