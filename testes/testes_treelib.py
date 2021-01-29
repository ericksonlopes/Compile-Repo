from treelib import Tree

tree = Tree()
tree.create_node("Pasta", "/")
tree.create_node("Pasta", "/pasta2", parent="/")
tree.create_node("Pasta", "/pasta3", parent="/")
tree.create_node("Pasta", "/pasta4", parent="/pasta3")
tree.create_node("Pasta", "/pasta5", parent="/")


tree.show()
# tree.save2file('tree.txt')

# Harry,Bill,Jane,Diane,Mary,Mark
# print(tree.to_json())
# print(tree.to_graphviz())
# print(tree.to_dict())
