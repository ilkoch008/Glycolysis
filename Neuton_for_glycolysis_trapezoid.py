import math
import numpy


def neuton(x0, y0, h, alpha, betta):
    matrix_J = [0] * 2
    matrix_J_inv = [0] * 2
    vector_sol = [1.0] * 2
    vector_at_point = [0.0] * 2
    vector_sol = numpy.array(vector_sol)
    vector_save = numpy.array(vector_sol)
    vector_at_point = numpy.array(vector_at_point)
    vector_sol[0] = x0
    vector_sol[1] = y0
    const1 = 2*x0 + 2*h - h*x0*y0
    const2 = 2*y0 + h*alpha*y0*x0 - h*alpha*y0*(1+betta)/(y0+betta)

    for i in range(0, 2):
        matrix_J[i] = [0.0] * 2

    while 1 > 0:
        matrix_J[0][0] = 2 + h * vector_sol[1]
        matrix_J[0][1] = vector_sol[0] * h
        matrix_J[1][0] = -h * alpha * vector_sol[1]
        matrix_J[1][1] = 2 - h*alpha*vector_sol[0] + alpha*betta*(betta+1)*h/math.pow(betta+vector_sol[1], 2)
        vector_at_point[0] = 2*vector_sol[0] + h*vector_sol[0]*vector_sol[1] - const1
        vector_at_point[1] = 2*vector_sol[1] - h*alpha*vector_sol[0]*vector_sol[1] + h*alpha*vector_sol[1]*(1+betta)/(vector_sol[1]+betta) - const2
        matrix_J_inv = numpy.linalg.inv(matrix_J)
        vector_sol = vector_sol - matrix_J_inv.dot(vector_at_point)
        if numpy.linalg.norm(vector_sol - vector_save) < math.pow(10, -8):
            break
        vector_save = vector_sol
    return vector_sol
