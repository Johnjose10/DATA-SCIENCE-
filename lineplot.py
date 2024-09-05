import matplotlib.pyplot as plt
import numpy as np
x=np.array([2010,2011,2012,2013,2014,2015,2016])
y=np.array([60000,50000,45000,40000,40000,33500,27000])
plt.plot(x,y)
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.title("value Depresiation")

plt.plot(x,y,ls="-.",color="r",marker="*",markerfacecolor="g",markersize=20)
plt.show()
