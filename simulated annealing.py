import random
import math

def simulated_annealing(domain, costf, temp = 10000.0,
                     cool = 0.95, step = 1):
    
    current_sol = [float(random.randint(domain[i][0], domain[i][1])) for i in range(len(domain))]
    while temp > 0.1:
        
        i = random.randint(0, len(domain) - 1)
        
        
        direction = random.randint(- step, step)
        
        new_sol = current_sol[:]
        new_sol[i] += direction
        if new_sol[i] < domain[i][0]: new_sol[i] = domain[i][0]
        elif new_sol[i] > domain[i][1]: new_sol[i] = domain[i][1]

        current_cost = costf(current_sol)
        new_cost = costf(new_sol)
        
        p = math.e ** (( - new_cost - current_cost) / temp)
        
        if (new_cost < current_cost or random.random() < p):
            current_sol = new_sol
            print(new_cost)
        
        temp = temp * cool
    return current_sol

