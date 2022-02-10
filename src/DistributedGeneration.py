class DistributedGeneration:
    def __init__(self, power_produced):
        self.power_produced = power_produced


class PV(DistributedGeneration):
    def __init__(self, power_produced):
        super().__init__(power_produced)


class WindPower(DistributedGeneration):
    def __init__(self, power_produced):
        super().__init__(power_produced)


