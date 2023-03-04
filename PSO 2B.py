import numpy as np
from numpy import sqrt, absolute

def function(x,y) :
    return((1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2)

def PSO(xyn, vn, c1, c2, r1, r2, w, iteration, pbest = None, miteration = 0) :
    if miteration == 0 :
        miteration = iteration

    if pbest == None :
        pbest = xyn
    index = 0
    gbest = 0
    for xy in xyn :
        if index == 0 :
            before = function(xy[0], xy[1])
            gbest = xy
        if before > function(xy[0], xy[1]) :
            before = function(xy[0], xy[1])
            gbest = xy

    new_v_matrix = []
    index = 0
    for v in vn :
        new_v_matrix.append(w*np.matrix([v])+ c1*r1*(np.matrix([pbest[index]]) - np.matrix([xyn[index]])) + c2*r2*(np.matrix([gbest])- np.matrix([xyn[index]])))

    new_xyn = []
    new_v = []
    new_pbest = []
    index = 0

    print("\033[92m"+f"iteration ke-{miteration-iteration+1}"+"\033[0m")
    for xy in xyn :
        xy_matrix = np.matrix(xy)+new_v_matrix[index]

        new_xyn.append([xy_matrix[0,0], xy_matrix[0,1]])

        if function(xy[0], xy[1]) > function(xy_matrix[0, 0], xy_matrix[0, 1]) :
            new_pbest.append([xy_matrix[0, 0], xy_matrix[0]])

        else :
            new_pbest.append([xy[0], xy[1]])

        new_v.append([new_v_matrix[index][0, 0],new_v_matrix[index][0, 1]])
        print("X"+ str(index), "=", xy_matrix)
        index += 1

    print("F(X) = ", function(gbest[0], gbest[1]))
    print()
    if iteration == 1 :
        print("nilai minimum = ", function(gbest[0], gbest[1]))
    else :
        PSO(new_xyn, new_v, c1, c2, r1, r2, w, iteration-1, new_pbest, miteration)

print(".: PSO :.")
PSO([[1,1], [-1,2], [2,1]], [[0, 0], [0, 0], [0, 0]], 1, 0.5,1, 1, 1, 3)