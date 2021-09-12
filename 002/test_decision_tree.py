from decision_tree import *

points = [
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 2, 'y': 1, 'class': 0},
    {'x': 3, 'y': 1, 'class': 0},
    {'x': 1, 'y': 2, 'class': 0},
    {'x': 2, 'y': 2, 'class': 1},
    {'x': 3, 'y': 2, 'class': 1},
    {'x': 2, 'y': 3, 'class': 1}
]

# y=3      1
# y=2  0   1   1
# y=1  0   0   0
#     x=1 x=2 x=3

decision_tree = DecisionTree()
decision_tree.fit(points)

# prediction = decision_tree.predict({'x': 3, 'y': 3})
# print(prediction) # should be 1

'''
python 002/test_decision_tree.py
'''