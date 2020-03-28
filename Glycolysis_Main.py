from multiprocessing import Process
import Glycolysis as g

if __name__ == '__main__':
    h = 0.001
    alpha = 400
    betta = 10

    euler_proc = Process(target=g.euler, args=(h, alpha, betta))
    trapezoid_proc = Process(target=g.trapezoid, args=(h, alpha, betta))
    n_euler_proc = Process(target=g.n_euler, args=(h, alpha, betta))
    runge_kutta_proc = Process(target=g.runge_kutta, args=(h, alpha, betta))
    euler_proc.start()
    trapezoid_proc.start()
    n_euler_proc.start()
    runge_kutta_proc.start()
