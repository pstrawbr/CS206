import numpy
import matplotlib.pyplot as plt

# backLegSensorValues = numpy.load("data/backLegSense.npy")
# frontLegSensorValues = numpy.load("data/frontLegSense.npy")
#
# plt.plot(backLegSensorValues, linewidth=4)
# plt.plot(frontLegSensorValues)
#
# plt.legend(('Back Leg', 'Front Leg'))

plt.rcParams.update({'font.size': 12})

with open('quad_vals.npy', 'rb') as f:
    quad_vals = numpy.load(f)

with open('oct_vals.npy', 'rb') as f:
    oct_vals = numpy.load(f)

with open('hex_vals.npy', 'rb') as f:
    hex_vals = numpy.load(f)

for row in range(quad_vals.shape[0]):
    plt.plot(quad_vals[row, :], "b", linewidth=2)
    plt.plot(hex_vals[row, :], "g", linewidth=2)
    plt.plot(oct_vals[row, :], "r", linewidth=2)

plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.legend(('Quadruped', 'Hexaped', 'Octoped'))

plt.show()

for row in range(quad_vals.shape[0]):
    quad_mean = numpy.mean(quad_vals, dtype=numpy.float64, axis=0)
    oct_mean = numpy.mean(oct_vals, dtype=numpy.float64, axis=0)
    hex_mean = numpy.mean(hex_vals, dtype=numpy.float64, axis=0)
    plt.plot(quad_mean, "b", linewidth=2)
    plt.plot(hex_mean, "g", linewidth=2)
    plt.plot(oct_mean, "r", linewidth=2)

plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.title('Mean fitness value of 4, 6, and 8 Legs')
plt.legend(('Quadruped', 'Hexaped', 'Octoped'))

plt.show()

for row in range(quad_vals.shape[0]):
    quad_mean = numpy.mean(quad_vals, dtype=numpy.float64, axis=0)
    oct_mean = numpy.mean(oct_vals, dtype=numpy.float64, axis=0)
    hex_mean = numpy.mean(hex_vals, dtype=numpy.float64, axis=0)
    quad_std = numpy.std(quad_vals, dtype=numpy.float64, axis=0)
    oct_std = numpy.std(oct_vals, dtype=numpy.float64, axis=0)
    hex_std = numpy.std(hex_vals, dtype=numpy.float64, axis=0)
    #plt.plot(quad_mean, "b", linewidth=2)
    plt.plot(hex_mean, "g", linewidth=2)
    plt.plot(oct_mean, "r", linewidth=2)
    #plt.plot(quad_mean + quad_std, "b", linewidth=2)
    #plt.plot(quad_mean - quad_std, "b", linewidth=2)
    plt.plot(hex_mean + hex_std, "g", linewidth=2)
    plt.plot(hex_mean - hex_std, "g", linewidth=2)
    plt.plot(oct_mean + oct_std, "r", linewidth=2)
    plt.plot(oct_mean - oct_std, "r", linewidth=2)

plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.title('Mean (+/-) Standard Deviation of 6 and 8 Legs')
plt.legend(['Hexaped', 'Octoped']) #, 'Quadruped'

plt.show()
