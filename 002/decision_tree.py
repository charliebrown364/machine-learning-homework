import math

def calc_entropy(points):

    num_class_0 = sum([point['class'] == 0 for point in points])
    num_class_1 = sum([point['class'] == 1 for point in points])
    
    if num_class_0 == 0 or num_class_1 == 0:
        return 0
    
    p0 = num_class_0 / len(points)
    p1 = num_class_1 / len(points)
    
    return - p0 * math.log(p0) - p1 * math.log(p1)

class Split:
    def __init__(self, dim, points, midpoint):
        self.dim = dim
        self.points = points
        self.midpoint = midpoint
        self.children = self.set_children()

    def set_children(self):

        divided_points = [[], []]

        for point in self.points:
            if point[self.dim] < self.midpoint:
                divided_points[0].append(point)
            else:
                divided_points[1].append(point)
        
        return [Node(points) for points in divided_points]

    def get_weighted_avg(self):
        less_than_points, greater_than_points = [node.points for node in self.children]
        less_than_weight    = len(less_than_points)    * calc_entropy(less_than_points)
        greater_than_weight = len(greater_than_points) * calc_entropy(greater_than_points)
        return (less_than_weight + greater_than_weight) / len(self.points)

    def calc_entropy(self, input_points):

        num_class_0 = sum([point['class'] == 0 for point in input_points])
        num_class_1 = sum([point['class'] == 1 for point in input_points])

        if num_class_0 == 0 or num_class_1 == 0:
            return 0

        p0 = num_class_0 / len(input_points)
        p1 = num_class_1 / len(input_points)

        return - p0 * math.log(p0) - p1 * math.log(p1)

class Node:
    def __init__(self, points):
        self.points = points
        self.splits = self.set_splits()
    
    def set_splits(self):

        splits = []

        for key in self.points[0].keys():
            if key != 'class':

                values = list(set([point[key] for point in self.points]))
                for i in range(len(values) - 1):
                    midpoint = (values[i] + values[i + 1]) / 2
                    split = Split(key, self.points, midpoint)
                    splits.append(split)
        
        return splits

    def find_best_split(self):
        weighted_avgs = [split.get_weighted_avg() for split in self.splits]
        return self.splits[weighted_avgs.index(min(weighted_avgs))]

    def check_if_pure(self):
        return calc_entropy(self.points) == 0

class DecisionTree:
    def __init__(self):
        self.root = None
        self.leaf_nodes = None

    def fit(self, points):
                
        self.root = Node(points)
        self.leaf_nodes = [self.root]

        while len(self.leaf_nodes) != 0:
            
            current_node = self.leaf_nodes[0]
            best_split = current_node.find_best_split()

            for node in best_split.children:
                if not node.check_if_pure():
                    self.leaf_nodes.append(node)
                    
            for node in self.leaf_nodes:
                if node.check_if_pure():
                    self.leaf_nodes.remove(node)

        print('\ndone')

    def predict(self, point):
        pass