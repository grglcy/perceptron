from Perceptron import Perceptron
from random import Random
from Dataset import Dataset
from Graph import *

rand = Random()
learn_rate = 0.01

p = Perceptron()

def line_perceptron():
    graph = Graph(640, 480, "Perceptron")
    graph.drawLine(Point(-1000, -1000 + 100), Point(1000, 1000 + 100))

    p.add_input("1", 1, rand.uniform(-1, 1))
    p.add_input("2", 1, rand.uniform(-1, 1))
    p.add_input("bias", 1, rand.uniform(-1, 1))

    def answer(p_x, p_y):
        if p_y > calc_y(p_x):
            return 1
        else:
            return -1

    def calc_y(p_x):
        return p_x + 100

    for ind in range(0, 1000):
        x = rand.randint(-1000, 1000)
        y = rand.randint(-1000, 1000)
        print(x, y)
        p.input(x, y)
        z = answer(x, y)
        print("error: %f" % p.guess(z, learn_rate))

    '''for i in range(0, 1000):
        x = int(input("x: "))
        if x == 9001:
            break
        y = int(input("y: "))
        p.input(x, y)
        if p.activation() == 1:
            graph.drawCircle(Point(x, y), 4, "green")
        else:
            graph.drawCircle(Point(x, y), 4, "red")'''

    for i in range(0, 1000000):
        x = rand.randint(-320, 320)
        y = rand.randint(-240, 240)
        p.input(x, y)
        if p.activation() == 1:
            graph.drawCircle(Point(x, y), 4, "green")
        else:
            graph.drawCircle(Point(x, y), 4, "red")
        if i % 1000 == 0:
            graph.drawLine(Point(-1000, -1000 + 100), Point(1000, 1000 + 100))

    input()

def and_perceptron():
    data = Dataset(open("input.txt").read().split('\n'), open("target.txt").read().split('\n'))
    i = data.inputs

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
