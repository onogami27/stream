import random
import matplotlib.pyplot as plt
def rand():
    list = []
    for i in range(10):
        x = random.randint(1,10)
        list.append(x)
    
    y_list = [1,2,3,4,5,6,7,8,9,10]

    plt.plot(list, y_list)
    plt.grid()
    plt.show()

