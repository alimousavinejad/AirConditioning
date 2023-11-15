class Cargo_heat:
    def __init__(self):
        self.FWD_ISOL_VALVE = False
        self.AFT_ISOL_VALVE = False
        self.HOT_AIR = False
        self.FWD = 0
        self.AFT = 0

    def set_AFT(self, value: (int, float)):
        if -3 <= value <= 3:
            self.AFT = value
        else:
            raise Exception("Out of range value")

    def set_FWD(self, value: (int, float)):
        if -3 <= value <= 3:
            self.FWD = value
        else:
            raise Exception("Out of range value")

    def toggle_FWD_ISOL_VALVE(self):
        self.FWD_ISOL_VALVE =~ self.FWD_ISOL_VALVE

    def toggle_AFT_ISOL_VALVE(self):
        self.AFT_ISOL_VALVE =~ self.AFT_ISOL_VALVE

    def toggle_HOT_AIR(self):
        self.HOT_AIR =~ self.HOT_AIR
