import matplotlib.pyplot as plt
import numpy as np
# Make the graph beautiful
import seaborn as sns
sns.set()

class secondOrderEuler:
    def __init__(self, xi, yi, zi, g, xf, h):
        self.xi, self.yi, self.zi, self.g, self.xf, self.h = xi, yi, zi, g, xf, h

    def y_axis(self):
        x, y, z = self.xi, self.yi, self.zi
        yy = []
        while(x <= self.xf):
            yy.append(y)
            y += self.h*z                  # THE
            x += self.h                    # SIMULTANEOUS
            z += self.h*self.g(x, y, z)    # EQUATIONS
                        
        return yy

    #         #          #
    def z_axis(self):
        x, y, z = self.xi, self.yi, self.zi
        zz = []
        while(x < self.xf):
            zz.append(z)
            z += self.h*self.g(x, y, z)
            x += self.h
            y += self.h*z
            
        return zz
    #         #          #

    def x_axis(self):
        x = self.xi
        xx = []
        while (x < self.xf):
            xx.append(x)
            x += self.h

        return xx

## Degree to radian
def degRad(x):
    return np.pi*x/180

## Intial condtion
ti = 0
theta_i = degRad(150)
theta1primei = 0
tf = 4*np.pi
h = 0.01
##

#
Dsim = secondOrderEuler(ti, theta_i, theta1primei, lambda x, y, z: -y, tf, h)

Dpen = secondOrderEuler(ti, theta_i, theta1primei, lambda x, y, z: -np.sin(y) , tf, h)
#

#How to find the time period of the given plot
def TimePeriod(y, x):
	i = 1
	while (y[i] > y[i+1]):
		i += 1
		
	return 2*(x[i] - x[1])

print("The period for Simple", TimePeriod(Dsim.y_axis(), Dsim.x_axis()))

print("The period for original", TimePeriod(Dpen.y_axis(), Dpen.x_axis()))

#Plotting
plt.rcParams["figure.figsize"] = (150, 6)
plt.title(r"Initial angle $150°$", size = 35)
plt.plot(Dsim.x_axis(), Dsim.y_axis(),"red", label = r"$-\theta$ approx")
plt.ylabel(r"$\theta$", size = 20)

plt.plot(Dpen.x_axis(), Dpen.y_axis(),"Green", label = r"$-\sin \theta$ approx")
plt.legend(loc = 'best')
plt.ylabel(r"$\theta$", size = 20)
plt.xlabel(r'$t$', size = 20)
plt.show()