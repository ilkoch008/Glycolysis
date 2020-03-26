# Glycolysis

### Introduction
This repository discusses some solutions to the equation describing the simplest glycolysis model.

This equation is given below.

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/task.png "The equation of the simplest glycolysis model")

![](https://raw.githubusercontent.com/ilkoch008/Glycolysis/master/images/T_k.png)

Here you can find the implementation of 4 methods.

They are:
  1. Explicit Euler Method
  2. Implicit Euler Method
  3. Implicit trapezoid method
  4. Four Step Fourth Order Runge-Kutta Method

Now we will consider each method separately.

## Explicit Euler Method
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

## Implicit Euler Method

In this method, the derivative is taken at the point for which the value is calculated:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_1.png?raw=true)

In the context of our task, this will be written as follows:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_2.png?raw=true)

To simplify the view, I introduced the following notation:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_3.png?raw=true)

Rewrite the equation again:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_4.png?raw=true)

And again:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_5.png?raw=true)

To solve this system, I used the Newton method. Find the Jacobi matrix:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_6.png?raw=true)

Then the solution to this system of equations is found by the following iterative process:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/euler_7.png?raw=true)

Thus, for each step of Implicit Euler Method we must solve nonlinear system of equations which, in turn, is also an iterative process. So this method takes too much time to be calculated. That is why it is not widely used in practice (this applies to most implicit methods).

## Implicit trapezoid method
This method is a logical continuation of Explicit Euler Method and Implicit Euler Method. It can be said that it is the arithmetic mean of the previous two methods. Regarding calculations and transformations, this method is very similar to Implicit Euler Method in my case. Here it is:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/trap_1.png?raw=true)

Or in our terms:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/trap_2.png?raw=true)

(constants introduced as explanation for code)

The corresponding Jacobi matrix for this system (almost the same as for Implicit Euler Method):

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/trap_3.png?raw=true)

The rest of the algorithm is similar to my realization of the Implicit Euler Method.

## Four Step Fourth Order Runge-Kutta Method
Below are the formulas that I used to calculate the solution:

![](https://github.com/ilkoch008/Glycolysis/blob/master/images/r_k_1.png?raw=true)

I draw your attention to the fact that vector quantities were also used in some previous expressions. In this expression, I considered it necessary to emphasize this.
