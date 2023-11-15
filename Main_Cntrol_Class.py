class Main_Class:

    self.cockpit_temperature = 0
    # -3, -2, -1, 0, +1, +2, +3
    def set_cockpit_temperature(self, temperature_selector):
        if -4<temperature_selector<4:
            self.cockpit_temperature = temperature_selector
        else:
            raise Exception("Out of range value!")
        return

    self.forward_cabin_temperature = 0
    # -3, -2, -1, 0, +1, +2, +3
    def set_forward_cabin_temperature(self, temperature_selector):
        if -4<temperature_selector<4:
            self.forward_cabin_temperature = temperature_selector
        else:
            raise Exception("Out of range value!")
        return

    self.afterward_cabin_temperature = 0
    # -3, -2, -1, 0, +1, +2, +3
    def set_afterward_cabin_temperature(self, temperature_selector):
        if -4<temperature_selector<4:
            self.afterward_cabin_temperature = temperature_selector
        else:
            raise Exception("Out of range value!")
        return

    self.hot_air_fault = True #True
    # on : True | off : False
    def toggle_hot_air_fault (self):
        self.hot_air_fault = not self.hot_air_fault
        return

    self.pack1_fault = True
    # on : True | off : False
    def toggle_hot_air_fault (self):
        self.pack1_fault = not self.pack1_fault
        return

    self.pack2_fault = True
    # on : True | off : False
    def toggle_hot_air_fault (self):
        self.pack2_fault = not self.pack2_fault
        return

    self.engine1_bleed_fault = True
    # on : True | off : False
    def toggle_engine1_bleed_fault (self):
        self.engine1_bleed_fault = not self.toggle_engine1_bleed_fault
        return

    self.engine2_bleed_fault = True
    # on : True | off : False
    def toggle_engine2_bleed_fault (self):
        self.engine2_bleed_fault = not self.toggle_engine2_bleed_fault
        return

    self.apu_bleed_fault = False
    def toggle_apu_bleed_fault (self):
        self.apu_bleed_fault = not apu_bleed_fault
        return
    
