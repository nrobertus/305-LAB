import numpy as np
import math
import pylab


def calcPoints(num_points):
    print("Testing over " + str(num_points) + " pointz.")
    num_points_inside = 0
    points = np.zeros([num_points, 2])
    for x in range(num_points):
        points[x,0] = np.random.random()
        points[x,1] = np.random.random()
        if(math.sqrt(points[x,0]**2 + points[x,1]**2) < 1):
            num_points_inside += 1

    print(str(num_points_inside) + " pointz inside.")
    return (float(num_points_inside)/float(num_points))*4.0


for x in range(100):
    test_value = 100*(x+1)
    exp_pi = calcPoints(test_value)
    pi_diff = abs(math.pi - exp_pi)
    pylab.plot(test_value, pi_diff,"ro")

pylab.show()
    # test_value
    #print pi_diff
