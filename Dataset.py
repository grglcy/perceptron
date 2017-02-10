from Data import Data


class Dataset(object):

    def __init__(self, p_input, p_target):
        self.inputs = {}

        for index, item in enumerate(p_input):
            input1 = float(p_input[index].split(',')[0].strip())
            input2 = float(p_input[index].split(',')[1].strip())
            if p_target[index] == "1":
                output = 1
            else:
                output = -1
            self.inputs[index] = Data(input1, input2, output)
