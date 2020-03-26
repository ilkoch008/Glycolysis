# Glycolysis

### Introduction
This repository discusses some solutions to the equation describing the simplest glycolysis model.

This equation is given below.

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/task.png "The equation of the simplest glycolysis model")

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/T_k.png)

Here you can find the implementation of 4 methods.

They are:
  1. Explicit Euler Method
  2. Implicit trapezoid method
  3. Implicit Euler Method
  4. Four Step Fourth Order Runge-Kutta Method

Now we will consider each method separately.

### Explicit Euler Method
One of the simplest methods.
In general terms, our equation looks like this:

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/1.png)

After approximation:

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/2.png)

Now finding a solution to the equation is reduced to simple sequential calculations.

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/3.png)

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/h.png)

Let's move on to the condition of our task:

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/4.png)

According to this formula the solution of equation is calculated.
