import random
import time
import os
from random import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def checks_in_vector(vector, arr_len, bot, top):
    num = randint(bot, top)
    for element in vector:
        if element == num:
            num = checks_in_vector(vector, arr_len, bot, top)

    return num

def randomize_vector(bot, top, arr_len):
    vector = []
    for x in range (0, arr_len ):
        value = checks_in_vector(vector, arr_len, bot, top)
        vector.append(value)
    return vector

def randomize_vector_repeat(bot, top, arr_len):
    vector = []
    for x in range (0, arr_len ):   
        vector.append(randint(bot, top))
    return vector

def quicksort(V):
    if len(V) <= 1: 
        return V
    
    pivot = V[0]
    equal = [x for x in V if x == pivot]
    lesser = [x for x in V if x < pivot]
    greater = [x for x in V if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)





arr_counter = []

arr_1 = randomize_vector(1, 10, 10)

start_time = time.time()
quicksort(arr_1)
endtime = time.time() - start_time
arr_counter.append(endtime)

arr_2 = randomize_vector(1, 50, 50)

start_time = time.time()
quicksort(arr_2)
endtime = time.time() - start_time
arr_counter.append(endtime)

arr_3 = randomize_vector(1, 100, 100)

start_time = time.time()
quicksort(arr_3)
endtime = time.time() - start_time
arr_counter.append(endtime)

arr_4 = randomize_vector(1, 250, 250)

start_time = time.time()
quicksort(arr_4)
endtime = time.time() - start_time
arr_counter.append(endtime)

arr_5 = randomize_vector(1, 500, 500)


start_time = time.time()
quicksort(arr_5)
endtime = time.time() - start_time
arr_counter.append(endtime)

#################################################################################

arr_r_counter = []

arr_r1 = randomize_vector_repeat(1, 10, 10)

start_time = time.time()
quicksort(arr_r1)
endtime = time.time() - start_time
arr_r_counter.append(endtime)

arr_r2 = randomize_vector_repeat(1, 50, 50)

start_time = time.time()
quicksort(arr_r2)
endtime = time.time() - start_time
arr_r_counter.append(endtime)

arr_r3 = randomize_vector_repeat(1, 100, 100)

start_time = time.time()
quicksort(arr_r3)
endtime = time.time() - start_time
arr_r_counter.append(endtime)

arr_r4 = randomize_vector_repeat(1, 250, 250)

start_time = time.time()
quicksort(arr_r4)
endtime = time.time() - start_time
arr_r_counter.append(endtime)

arr_r5 = randomize_vector_repeat(1, 500, 500)

start_time = time.time()
quicksort(arr_r5)
endtime = time.time() - start_time
arr_r_counter.append(endtime)


final_arr_1 = np.array(arr_counter)

final_arr_2 = np.array(arr_r_counter)

##############################################################################################



##############################################################################################


y = [10, 50, 100 , 250, 500]

y = np.array(y)

plt.plot(final_arr_1, y, color='red')
plt.plot(final_arr_2, y, color='blue')
plt.title("Comparação QS números aleatórios repetidos e não repetidos")
red_patch = mpatches.Patch(color='red', label='Sem repetição')
blue_patch = mpatches.Patch(color='blue', label='Com repetição')
plt.legend(handles=[red_patch, blue_patch])
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho do vetor')
plt.show()