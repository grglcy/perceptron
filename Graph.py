from graphics import *

class Graph(object):

    def __init__(self, p_width, p_height, p_name):
        self.win = GraphWin("perceptron", p_width, p_height)
        self.win.setCoords(0, 0, 640, 480)
        self.x_offset = p_width / 2
        self.y_offset = p_height / 2
        self.win.setCoords(0, 0, 640, 480)
        Line(Point(0, p_height / 2), Point(p_width, p_height / 2)).draw(self.win)
        Line(Point(p_width / 2, 0), Point(p_width / 2, p_height)).draw(self.win)

    def drawLine(self, p_point1, p_point2):
        Line(p_point1, p_point2).draw(self.win).move(self.x_offset, self.y_offset)

    def drawCircle(self, p_centre, p_radius, p_fill):
        circle = Circle(p_centre, p_radius)
        circle.setFill(p_fill)
        circle.setOutline(p_fill)
        circle.draw(self.win).move(self.x_offset, self.y_offset)

