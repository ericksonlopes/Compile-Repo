from treelib import Node, Tree

tree = Tree()
tree.create_node("Harry", "harry")
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Luis", "luis", parent="diane")
tree.create_node("Erickson", "erickson", parent="bill")
tree.create_node("Erickson", 1, parent="harry")

tree.show()
tree.save2file('tree.txt')

# print(tree.to_json())
# print(tree.to_graphviz())
# print(tree.to_dict())
