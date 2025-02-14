import numpy
import matplotlib.pyplot as plt

age = numpy.random.uniform(0.0, 120.00, 300)
age_thai = numpy.random.normal(40, 10, 10000);
plt.hist(age_thai, 100)
plt.show()