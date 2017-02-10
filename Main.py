from Perceptron import Perceptron
from random import Random
from Dataset import Dataset

rand = Random()
data = Dataset(open("input.txt").read().split('\n'), open("target.txt").read().split('\n'))


for key in data.inputs:
    i = data.inputs
    print("v1: ", i[key].value1, "v2: ", i[key].value2, "target: ", i[key].target)
    p = Perceptron()
    p.add_input("1", i[key].value1, rand.uniform(-1, 1))
    p.add_input("2", i[key].value2, rand.uniform(-1, 1))
    p.add_input("bias", 1, rand.uniform(-1, 1))
    print("%f" % p.guess(i[key].target))
