class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"Drawing treen {self.name} of color {self.color} and texture {self.texture}")

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        if (name, color, texture) not in TreeFactory._tree_types:
            TreeFactory._tree_types[(name, color, texture)] = TreeType(name, color, texture)
        return TreeFactory._tree_types[(name, color, texture)]
    
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)

if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(10, 20, "Oak", "Green", "Rough")
    forest.plant_tree(10, 40, "Pine", "DarkGreen", "Smooth")
    forest.plant_tree(30, 40, "Oak", "Green", "Rough")
    forest.plant_tree(10, 60, "Pine", "DarkGreen", "Smooth")
    forest.draw("Canvas1")