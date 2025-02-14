import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

#x = time for dicisions
x = numpy.random.normal(5.0, 1.5, 1000)
#y = money to spend
y = numpy.random.normal(1000, 100, 1000) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 1000)

print(mymodel(5))

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()