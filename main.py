import timeit
import matplotlib.pyplot as plt
import numpy as np

ax, fig = plt.subplots()

mysetup = "from math import sqrt"
k = 0
mycode = '''
def gen_rec(k, real_sqrt):
    a = []
    i = 1
    a.append(2)
    a.append(2)
    while (abs(a[i] / a[i - 1] - 1 - real_sqrt) > 0.01):
        i += 1
        a.append(2 * a[i - 1] + (k - 1) * a[i - 2])
    return a[i] / a[i - 1] - 1
x = gen_rec({}, sqrt({}))
'''.format(k, k)

mysetup1 = "from math import sqrt"
mycode1 = '''
x = sqrt({})
'''.format(k)

vals = np.linspace(0, 10e7, 1000)

rec = []
base = []

for val in vals:
    k = val
    rec.append(timeit.timeit(setup=mysetup,
                             stmt=mycode,
                             number=10) - timeit.timeit(setup=mysetup1,
                                                        stmt=mycode1,
                                                        number=10))

    base.append(timeit.timeit(setup=mysetup1,
                              stmt=mycode1,
                              number=10))
    plt.scatter(rec[len(rec) - 1], val, color='r')
    plt.scatter(base[len(base) - 1], val, color='b')

print("base sqrt:\n std:", np.std(base), "\nmin/max:", np.min(base), np.max(base))
print("\nour sqrt:\n std:", np.std(rec), "\nmin/max:", np.min(rec), np.max(rec))
plt.show()