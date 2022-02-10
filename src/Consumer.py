class Consumer:
    def __init__(self, appliances, electricity_costs, charge_appliances, ev = [], pv = []):
        self.appliances = appliances
        self.electricity_costs = electricity_costs
        self.charge_appliances = charge_appliances
        self.ev = ev
        self.pv = pv

    def compute(self, cost):
        pass

    def update_all(self, appliance_values, charge_appliance_values):
        for value, appliance in zip(appliance_values, self.appliances):
            appliance.update(value)
        for charge_value, charge_appliance in zip(charge_appliance_values, self.charge_appliances):
            charge_appliance.update()
        

    