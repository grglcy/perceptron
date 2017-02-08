class Input(object):

    def __init__(self, p_value, p_weight):
        self.value = p_value
        self.weight = p_weight

    def print(self):
        print("value: %f\nweight: %f") % (self.value, self.weight)

    def setweight(self, p_weight):
        self.weight = p_weight