from Input import Input


class Perceptron(object):

        def __init__(self):
            self.inputs = {}

        def print(self):
            for key in self.inputs:
                print(key + ":")
                self.inputs[key].print()

        def input(self, p_input1, p_input2):
            self.inputs['1'].value = float(p_input1)
            self.inputs['2'].value = float(p_input2)

        def add_input(self, p_name, p_value, p_weight):
            self.inputs[p_name] = Input(p_value, p_weight)

        def set_weight(self, p_input, p_weight):
            self.inputs[p_input].weight = p_weight

        def _sum_inputs(self):
            total = 0
            for key in self.inputs:
                total += self.inputs[key].output()
            return total

        def activation(self):
            input = self._sum_inputs()
            print("Sum of inputs = %f" % input)

            if input > 0:
                return 1
            else:
                return -1

        def guess(self, p_desired, p_learning_constant):
            prediction = float(self.activation())
            error = p_desired - prediction
            for key in self.inputs:
                self.inputs[key].weight += error * self.inputs[key].value * p_learning_constant
            return error
