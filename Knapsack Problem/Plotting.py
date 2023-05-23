import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
import random
from KnapSack import KnapSack

def calc_time(profits, weights, capacity):
    i = KnapSack(profits, weights, capacity)
    time1 = time.time()
    i.solve_knapsack_brute_force()
    time2 = time.time()
    return time2 - time1

def calc_average_time(howMany):
    times = 0
    for i in range(10):
        randomProfits = random.sample(range(1, 30), howMany)
        randomWeights = random.sample(range(1, 30), howMany)
        randomCapacity = random.randint(1, 30)
        time = calc_time(randomProfits, randomWeights, randomCapacity)
        times += time
    times /=  10
    return times
