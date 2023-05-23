from itertools import product

class KnapSack:
  def __init__(self, profits, weights, capacity):
    self.profits = profits
    self.weights = weights
    self.capacity = capacity

  def solve_knapsack_brute_force(self):
    dane = [0, 1]
    max_profit = 0
    productSet = product(dane, repeat = len(self.weights))

    for element in productSet:
      profit = 0
      weight = 0
      for index in range(len(element)):
        sum = element[index] * self.weights[index]
        weight += sum
        res = element[index] * self.profits[index]
        profit += res

      if(weight <= self.capacity and profit >= max_profit):
        max_profit = profit
        indexes = [i for i in range(len(element)) if element[i] == 1]
    return indexes
        


  def solve_knapsack_pw_ratio(self):
    ratios = []
    for p, w, i in zip(self.profits, 
                       self.weights, 
                       range(len(self.weights))
                       ):
        ratios.append( (p/w, i) )
    ratios.sort(reverse = True)

    sum = 0
    i = 0
    indexes = []

    while(sum + self.weights[ratios[i][1]] <= self.capacity):
        index = ratios[i][1]
        sum += self.weights[index]
        indexes.append(index)
        i += 1
    return indexes

  def format(self, indexes):
    indexes.sort()
    print([el for el in indexes])
