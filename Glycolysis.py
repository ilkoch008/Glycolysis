import matplotlib.pyplot as plt
import Neuton_for_glycolysis_trapezoid as nfgt
import Neuton_for_glycolysis_Euler as nfge
import Find_next_for_Runge_Kutta as fn


# ----------------------------------------------------------------------------------------------------------------------
# Явный метод Эйлера ---------------------------------------------------------------------------------------------------
def euler(h, alpha, betta):

    solution_y1 = [0.0] * int(50/h)
    solution_y2 = [0.0] * int(50/h)
    t = [0.0] * int(50/h)

    for i in range(0, t.__len__()):
        t[i] = i * h

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    for i in range(0, t.__len__()-1):
        solution_y1[i+1] = solution_y1[i] + h*(1-solution_y1[i]*solution_y2[i])
        solution_y2[i+1] = solution_y2[i] + h*(alpha*solution_y2[i]*(solution_y1[i] - (1 + betta)/(solution_y2[i] + betta)))

    fig, axs = plt.subplots(2)

    axs[0].plot(t, solution_y1)
    axs[0].set_title("Явный метод Эйлера y1")
    axs[0].grid(True)
    axs[0].minorticks_on()
    axs[0].grid(which='minor', linestyle=':')
    axs[1].plot(t, solution_y2)
    axs[1].set_title("Явный метод Эйлера y2")
    axs[1].grid(True)
    axs[1].minorticks_on()
    axs[1].grid(which='minor', linestyle=':')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Неявный метод Трапеций------------------------------------------------------------------------------------------------

def trapezoid(h, alpha, betta):

    solution_y1 = [0.0] * int(50 / h)
    solution_y2 = [0.0] * int(50 / h)
    t = [0.0] * int(50 / h)

    for i in range(0, t.__len__()):
        t[i] = i * h

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    for i in range(0, t.__len__()-1):
        following = nfgt.neuton(solution_y1[i], solution_y2[i], h, alpha, betta)
        solution_y1[i+1] = following[0]
        solution_y2[i+1] = following[1]

    fig, axs = plt.subplots(2)

    axs[0].plot(t, solution_y1)
    axs[0].set_title("Неявный метод трапеций y1")
    axs[0].grid(True)
    axs[0].minorticks_on()
    axs[0].grid(which='minor', linestyle=':')
    axs[1].plot(t, solution_y2)
    axs[1].set_title("Неявный метод трапеций y2")
    axs[1].grid(True)
    axs[1].minorticks_on()
    axs[1].grid(which='minor', linestyle=':')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Неявный метод Эйлера--------------------------------------------------------------------------------------------------


def n_euler(h, alpha, betta):
    solution_y1 = [0.0] * int(50 / h)
    solution_y2 = [0.0] * int(50 / h)
    t = [0.0] * int(50 / h)

    for i in range(0, t.__len__()):
        t[i] = i * h

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    for i in range(0, t.__len__()-1):
        following = nfge.neuton(solution_y1[i], solution_y2[i], h, alpha, betta)
        solution_y1[i+1] = following[0]
        solution_y2[i+1] = following[1]

    fig, axs = plt.subplots(2)

    axs[0].plot(t, solution_y1)
    axs[0].set_title("Неявный метод Эйлера y1")
    axs[0].grid(True)
    axs[0].minorticks_on()
    axs[0].grid(which='minor', linestyle=':')
    axs[1].plot(t, solution_y2)
    axs[1].set_title("Неявный метод Эйлера y2")
    axs[1].grid(True)
    axs[1].minorticks_on()
    axs[1].grid(which='minor', linestyle=':')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Метод Рунге-Кутты (p=4, r=4)------------------------------------------------------------------------------------------

def runge_kutta(h, alpha, betta):
    solution_y1 = [0.0] * int(50 / h)
    solution_y2 = [0.0] * int(50 / h)
    t = [0.0] * int(50 / h)

    for i in range(0, t.__len__()):
        t[i] = i * h

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    solution_y1[0] = 1
    solution_y2[0] = 0.001

    for i in range(0, t.__len__() - 1):
        following = fn.find_next(solution_y1[i], solution_y2[i], h, alpha, betta)
        solution_y1[i + 1] = following[0]
        solution_y2[i + 1] = following[1]

    fig, axs = plt.subplots(2)

    axs[0].plot(t, solution_y1)
    axs[0].set_title("Неявный метод Рунге-Кутты y1")
    axs[0].grid(True)
    axs[0].minorticks_on()
    axs[0].grid(which='minor', linestyle=':')
    axs[1].plot(t, solution_y2)
    axs[1].set_title("Неявный метод Рунге-Кутты y2")
    axs[1].grid(True)
    axs[1].minorticks_on()
    axs[1].grid(which='minor', linestyle=':')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


