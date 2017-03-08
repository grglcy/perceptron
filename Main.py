from Perceptron import Perceptron
from random import Random
from Dataset import Dataset

rand = Random()
#data = Dataset(open("input.txt").read().split('\n'),
# open("target.txt").read().split('\n'))
learn_rate = 0.01

p = Perceptron()
#i = data.inputs


def line_perceptron():
    p.add_input("1", 1, rand.uniform(-1, 1))
    p.add_input("2", 1, rand.uniform(-1, 1))

    def answer(p_x, p_y):
        if p_y > calc_y(p_x):
            return 1
        else:
            return -1


    def calc_y(p_x):
        return p_x + 2

    for ind in range(0, 1000):
        x = rand.randint(-640 / 2, 640 / 2)
        y = rand.randint(-480 / 2, 480 / 2)
        print(x, y)
        p.input(x, y)
        print("error: %f" % p.guess(answer(x, y), learn_rate))

    for i in range(0, 1000):
        x = int(input("x: "))
        y = int(input("y: "))
        p.input(x, y)
        if p.activation() == 1:
            print("TRUE")
        else:
            print("FALSE")


def and_perceptron():
    p.add_input("1", 1, rand.uniform(-1, 1))
    p.add_input("2", 1, rand.uniform(-1, 1))
    p.add_input("bias", 1, rand.uniform(-1, 1))

    # train
    for ind in range(0, 500):
        i = data.inputs
        for key in data.inputs:
            p.input(i[key].value1, i[key].value2)
            print("error: %f" % p.guess(i[key].target, learn_rate))

    for i in range(0, 1000):
        x = input("Arg1: ")
        y = input("Arg2: ")
        p.input(x, y)
        if p.activation() == 1:
            print("TRUE")
        else:
            print("FALSE")

line_perceptron()