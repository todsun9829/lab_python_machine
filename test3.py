import numpy
import matplotlib.pyplot as plt

age = numpy.random.normal(40,15,1000);
wealth = numpy.random.normal(3000,300,1000);

plt.scatter(age,wealth)
plt.show()
