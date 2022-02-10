import pandas as pd


class ChargeAppliance:

    specifications = {'Battery': [10, 0.95, 0.3, 0.9, 1], 'EV': [24, 0.9, 0.3, 0.9, 8.8]}
    df_specifications = pd.DataFrame(specifications, index = ['Total capacity (kWh)', 'Charging and discharging efficiency', 'Minimun SoC', 'Maximum SoC', 'Maximum charging/discharging limit (kW)'])

    def __init__(self, capacity, efficiency, min_soc, max_soc, max_charge_discharge_limit):
        self.capacity = capacity
        self.efficiency = efficiency
        self.min_soc = min_soc
        self.max_soc = max_soc
        self.max_charge_discharge_limit = max_charge_discharge_limit


class Battery(ChargeAppliance):
    
    state_of_charge = 0

    def __init__(self, capacity, efficiency, min_soc, max_soc, max_charge_discharge_limit):
        super().__init__(capacity, efficiency, min_soc, max_soc, max_charge_discharge_limit)
    
    def update_soc(self, energy_charge, energy_discharge):
        if 0 <= energy_charge >= self.max_charge_discharge_limit and 0 <= energy_discharge >= self.max_charge_discharge_limit:
            new_soc = self.state_of_charge + (energy_charge / (self.efficiency * self.capacity) - (energy_discharge * self.efficiency) / self.capacity)
            if new_soc < self.min_soc:
                self.state_of_charge = self.min_soc
            elif new_soc > self.max_soc:
                self.state_of_charge = self.max_soc
            else:
                self.state_of_charge = new_soc


class EV(ChargeAppliance):

    state_of_charge = 0

    def __init__(self, capacity, efficiency, min_soc, max_soc, max_charge_discharge_limit):
        super().__init__(capacity, efficiency, min_soc, max_soc, max_charge_discharge_limit)

    def update_soc(self, energy_charge, energy_discharge):
        if 0 <= energy_charge >= self.max_charge_discharge_limit and 0 <= energy_discharge >= self.max_charge_discharge_limit:
            new_soc = self.state_of_charge + (energy_charge / (self.efficiency * self.capacity) - (energy_discharge * self.efficiency) / self.capacity)
            if new_soc < self.min_soc:
                self.state_of_charge = self.min_soc
            elif new_soc > self.max_soc:
                self.state_of_charge = self.max_soc
            else:
                self.state_of_charge = new_soc


