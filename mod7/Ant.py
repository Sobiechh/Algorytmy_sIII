#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

#funkcje
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum

class Ant(object):
    def __init__(self, position):
        self.position = position
#-----------------------------------------------------------------------------
#dane z wykladu


def AntAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 200         #dane 
    populationCount = 60          
    alpha           = 0.2
    population = [Ant(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)] #populacja na poczatku
    
    population.sort(key=lambda x: Function(x.position))
    if searchingMinimum == False: population.reverse()
    bestPosition = population[0].position[:]

    t = 0
    while t <= generationCount:
        # Mrowki poruszanie
        for antNumber in range(populationCount):
            ant = population[antNumber]
            if antNumber == 0: #jezeli blisko
                for k in range(dimension):
                    ant.position[k] += alpha * random.uniform(-1,1)
                    ant.position[k] = max(min(ant.position[k], rightEnd), leftEnd)
            else:              # dla pozostalych przypadlow
                for k in range(dimension): 
                    ant.position[k] += (bestPosition[k] - ant.position[k]) * random.uniform(-1, 1)
                    ant.position[k] = max(min(ant.position[k], rightEnd), leftEnd)

        # Najmocniejsza mrowka
        population.sort(key=lambda x: Function(x.position))
        if searchingMinimum == False: population.reverse()
        bestPosition = population[0].position[:]
        t += 1

    # Rozwiaazanie
    bestVector = bestPosition
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "Max" if searchingMinimum == False else "Min"
    print("  ", str(Function.__name__).upper() + "'S", extremum, " \n   x  =", bestVector,         "\n f(x) =", round(Function(bestVector), 5), "\n")

AntAlgorithm(Sum_Squares, -10, 10, 5, True)
AntAlgorithm(Weierstrass, -10, 10, 5, True)
AntAlgorithm(Sum_Squares, -10, 10, 5, False)
AntAlgorithm(Weierstrass, -10, 10, 5, False)

