# constructing the class raw_data
class raw_data():
    def __init__(self, *args) -> None:
        """Input a series of int or float values to construct a raw data.
        Use the unpacking operator * if your data is a list or tuple.
        Example: x1, x2, x3,... xn or *[x1, x2, x3, ... x4] or *([x1, x2, x3, ... x4)"""
        self.values = [ i for i in args if type(i) in [float, int]]

        # Validation
        if len(self.values) != len(args): print("TypeError: data was not handled correctly!")
    
    def unique_elements(self):
        return set(self.values)
    
    def count(self):
        return len(self.values)
    
    def frequency_distribution(self):
        pass

    def grouped_frequency_distribution(self):
        pass



class discrete_data():
    def __init__(self, *args) -> None:
        '''Input a tuple of the value of x and their corresponding frequencies, f.
        Example: (x1, f1), (x2, f2), ... (xn, fn) or [x1, f1], [x2, f2], ... [xn, fn]'''
        self.values = {i[0] : i[1] for i in args}

class continuous_data():
    def __init__(self, *args) -> None:
        self.values = {[i[0], i[1]] : i[2] for i in args} 
