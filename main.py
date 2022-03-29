# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot
import numpy as np
import pylab as plt


class Point:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.group = group


def generatePoints(amount):
    a = random.randint(-5, 5)
    b = random.randint(-10, 10)

    counter = 0

    points = []
    while (counter < amount):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        if y == x * a + b:
            continue
        if (y > a * x + b):
            group = 1
        else:
            group = 0
        points.append(Point(x, y, group))
        counter += 1
    return points

def addPoint(points,x,y):
    group = (w[0] * x + w[1] * y + b > 0) * 1
    points.append(Point(x,y,group))


def plocik(points,w,b):

    for point in points:
        if point.group:
            plt.plot([point.x], [point.y], 'o', color='red')
        else:
            plt.plot(point.x, point.y, 'o', color='blue')

    y = [-b / w[1], 0]
    x = [0, -b / w[0]]
    p1 = np.polyfit(x, y, 1)
    lim = plt.xlim()
    x.insert(0, lim[0])
    y.insert(0, np.polyval(p1, lim[0]))
    x.append(lim[1])
    y.append(np.polyval(p1, lim[1]))
    plt.plot(x, np.polyval(p1, x), 'g-')

    plt.show()


if __name__ == '__main__':
    points = generatePoints(30)
    tempArr = []
    tempExp = []




    for point in points:
        tempArr.append([point.x, point.y])
        tempExp.append(point.group)

    array = np.array(tempArr)
    expected = np.array(tempExp)
    w = np.array([random.randint(0,1),random.randint(0,1)])
    b = -(w[0] *array[0][0] + w[1]*array[0][1])

    c = ' '
    i = 0
    dW = 0

    while (1):
        s = ((array[i][0] * w[0] + array[i][1] * w[1] + b) > 0) * 1
        e = expected[i] - s

        if e != 0:
            w += e * array[i]
            b += e
            i = 0
            continue
        i += 1

        if i == len(array):
            break

    while c != 'n':
        plocik(points,w,b)
        tmp = input("Chcesz dodać pkt? t/n")
        if tmp == 't':
            x = int(input("Podaj x: "))
            y = int(input("Podaj y: "))
            addPoint(points,x,y)



