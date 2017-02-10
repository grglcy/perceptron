from Input import Input

class Perceptron(object):

        def __init__(self):
            self.inputs = {}

        def print(self):
            for key in self.inputs:
                print(key + ":")
                self.inputs[key].print()

        def add_input(self, p_name, p_value, p_weight):
            self.inputs[p_name] = Input(p_value, p_weight)

        def set_weight(self, p_input, p_weight):
            self.inputs[p_input].weight = p_weight

        def _sum_inputs(self):
            total = 0
            for key, value in self.inputs.items():
                total += value.output()
            return total

        def activation(self):
            input = self._sum_inputs()
            print("Total = %f" % input)

            if input > 0:
                return 1
            else:
                return -1

        def guess(self, p_desired):
            prediction = float(self.activation())
            return p_desired - prediction

