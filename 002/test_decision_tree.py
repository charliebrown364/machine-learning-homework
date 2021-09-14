from decision_tree import *

def draw_points(points):
    
    map_to = {(i, j): '-' for i in range(1, 5) for j in range(1, 5)}

    for point in points:
        point_list = (point['x'], point['y'])
        map_to[point_list] = str(point['class'])

    print('y=4  ' + map_to[(1, 4)] + '   ' + map_to[(2, 4)] + '   ' + map_to[(3, 4)] + '   ' + map_to[(4, 4)])
    print('y=3  ' + map_to[(1, 3)] + '   ' + map_to[(2, 3)] + '   ' + map_to[(3, 3)] + '   ' + map_to[(4, 3)])
    print('y=2  ' + map_to[(1, 2)] + '   ' + map_to[(2, 2)] + '   ' + map_to[(3, 2)] + '   ' + map_to[(4, 2)])
    print('y=1  ' + map_to[(1, 1)] + '   ' + map_to[(2, 1)] + '   ' + map_to[(3, 1)] + '   ' + map_to[(4, 1)])
    print('    x=1 x=2 x=3 x=4\n')

def tree_structure(input_node, num=''):
    
    print("structure of tree after iteration {}\n".format(num))
    draw_points(input_node.points)
    
    if not input_node.is_pure():
    
        for split in input_node.splits:
            print('split at ' + str(split.dim) + '=' + str(split.midpoint) + ':', '\n')
            for node in split.children[::-1]:
                draw_points(node.points)
    
    else:
        print("node is pure\n")

def best_split(input_node, num=''):
    print("\nbest split after iteration {}".format(num))
    split = input_node.find_best_split()
    print(str(split.dim) + '=' + str(split.midpoint), '\n')

points = [
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 2, 'y': 1, 'class': 0},
    {'x': 3, 'y': 1, 'class': 0},
    {'x': 1, 'y': 2, 'class': 0},
    {'x': 2, 'y': 2, 'class': 1},
    {'x': 3, 'y': 2, 'class': 1},
    {'x': 2, 'y': 3, 'class': 1},
]

'''
points = [
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 2, 'y': 1, 'class': 0},
    {'x': 3, 'y': 1, 'class': 0},
    {'x': 1, 'y': 2, 'class': 0},
    {'x': 2, 'y': 2, 'class': 0},
    {'x': 3, 'y': 2, 'class': 1},
    {'x': 2, 'y': 3, 'class': 0},
    {'x': 3, 'y': 3, 'class': 1},
    {'x': 4, 'y': 3, 'class': 1},
    {'x': 2, 'y': 4, 'class': 1},
    {'x': 3, 'y': 4, 'class': 1},
    {'x': 4, 'y': 4, 'class': 1}
]
'''

decision_tree = DecisionTree()

# decision_tree.root = Node(points)

# tree_structure(decision_tree.root, 1)
# tree_structure(decision_tree.root.find_best_split().children[0], 2)
# tree_structure(decision_tree.root.find_best_split().children[1], 2)

# best_split(decision_tree.root, 1)
# best_split(decision_tree.root.find_best_split().children[0], 2)
# best_split(decision_tree.root.find_best_split().children[1], 2)

decision_tree.fit(points)

print('')
draw_points(points)

# assert decision_tree.predict({'x': -1, 'y': -1}) == 0
# assert decision_tree.predict({'x': 4, 'y': 2}) == 1
# assert decision_tree.predict({'x': 1, 'y': 3}) == 0

assert decision_tree.predict({'x': 3, 'y': 3}) == 1
assert decision_tree.predict({'x': -1, 'y': -1}) == 0
assert decision_tree.predict({'x': 4, 'y': 1}) == 0

print('done')