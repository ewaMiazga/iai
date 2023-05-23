from KnapSack import KnapSack
import numpy as np
import matplotlib.pyplot as plt


from Plotting import calc_average_time 

def main():
  weights = np.array([8, 3, 5, 2])
  capacity = 9
  profits = np.array([16, 8, 9, 6])

  knapClass = KnapSack(profits, weights, capacity)

  print("Solution of knapsack brute force algorithm: ")
  knapClass.format(knapClass.solve_knapsack_brute_force())
  print()
  print("Solution of knapsack pw ratio algorithm: ")
  knapClass.format(knapClass.solve_knapsack_pw_ratio())

  values = []
  for i in range (21):
    values.append(calc_average_time(i))

  x = [i for i in range(21)]
  plt.plot(x, values)
  plt.tight_layout()
  plt.xlabel("n elements")
  plt.ylabel("times in seconds")
  plt.savefig("Plot.png")
  plt.show()

if __name__ == '__main__':
    main()