import math

class DesicionTree:
    def __init__(self, points_list):
        self.points = points_list

    def run(self):
        self.do_thing(self.points)

    def do_thing(self, points):
        
        weighted_avgs = []
        splits = self.get_splits(points)
        
        for axis, midpoint in splits:

            less_than = []
            greater_than = []
            
            for point in points:

                if point[axis] < midpoint:
                    less_than.append(point)
                else:
                    greater_than.append(point)

            weighted_avg = self.calc_weighted_avg(less_than, greater_than)
            weighted_avgs.append(weighted_avg)
        
        best_split = splits[weighted_avgs.index(min(weighted_avgs))]
    
        print(weighted_avgs)
        print(best_split)        

    def get_splits(self, points):

        splits = []
        dimensions = [key for key in points[0].keys() if key != 'class']

        for dim in dimensions:

            values = list(set([point[dim] for point in points]))
            for i in range(len(values) - 1):
                midpoint = (values[i] + values[i + 1]) / 2
                splits.append([dim, midpoint])

        return splits

    def calc_weighted_avg(self, less_than, greater_than):
        
        less_than_weight    = len(less_than)    * self.calc_entropy(less_than)
        greater_than_weight = len(greater_than) * self.calc_entropy(greater_than)
        
        numerator = less_than_weight + greater_than_weight
        total = len(less_than + greater_than)
        
        return numerator / total

    def calc_entropy(self, points):

        num_0 = sum([point['class'] == 0 for point in points])
        num_1 = sum([point['class'] == 1 for point in points])
        nums = [num_0, num_1]

        if 0 in nums:
            return 0

        entropy = 0
        for n in nums:
            n /= sum(nums)
            entropy -= n * math.log(n)

        return entropy

# replace splits with node class (each bubble is a node)

points = [
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 1, 'y': 2, 'class': 0},
    {'x': 1, 'y': 3, 'class': 0},
    {'x': 2, 'y': 1, 'class': 0},
    {'x': 2, 'y': 2, 'class': 1},
    {'x': 2, 'y': 3, 'class': 1},
    {'x': 3, 'y': 2, 'class': 1}
]

desicion_tree = DesicionTree(points)
desicion_tree.run()