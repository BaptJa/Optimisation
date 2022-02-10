from Consumer import Consumer
import pandas as pd

class Prosumer(Consumer):

    
    def __init__(self, appliances, electricity_costs, charge_appliances, distributed_generation):
        super().__init__(appliances, electricity_costs, charge_appliances)
        self.distributed_generation = distributed_generation

    def objective_function(self, P_grid, C_grid):
        cost = 0
        for t in range(24):
            cost += P_grid[t]*C_grid[t]*U[t]
        return cost

