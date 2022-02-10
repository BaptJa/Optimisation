class Appliance:
    def __init__(self, name, starting_time, ending_time, duration, power_rating):
        self.name = name
        self.status = "OFF"
        self.energy_history = 0
        self.energy_consumed = 0
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.duration = duration
        self.power_rating = power_rating


    def update(self, energy_consumed):
      if energy_consumed - energy_history == 0 or energy_consumed == 0:
        self.status = "OFF"
      else:
        self.status = "ON"
        #save the new value in the history
        energy_history = energy_consumed
        self.energy_consumed = energy_consumed - energy_history

    def constraints_appliance(self, t, df_appliances):
      if t <= df_appliances[df_appliances['appliances'] == self.name].loc['starting_time'] and t >= df_appliances[df_appliances['appliances'] == self.name].loc['ending_time']:
        return 0 # the electrical appliance is OFF
      else:
        return 1 # the optimization algorithm will decide the status of the appliance


class ElectricalAppliance(Appliance):
  def __init__(self, name):
    super().__init__(name)


class ThermostaticAppliance(Appliance):
  def __init__(self, name):
    super().__init__(name)

