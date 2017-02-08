from Input import Input


class Perceptron(object):

        def __init__(self):
            self.inputs = {}

        def print(self):
            for key, value in self.inputs:
                print("%s - )") % key
                value.print()

        def addinput(self, p_name, p_value, p_weight):
            self.inputs[p_name] = Input(p_value, p_weight)

        def setweight(self, p_input, p_weight):
            self.inputs[p_input].weight = p_weight
