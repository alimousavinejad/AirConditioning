class Pack:
    self.pack_flow = str()
    # PackFlow = [low, normal, high]
    self.compressor_outlet_temperature= float()
    self.by_pass_valve_position = bool()
    # open = True, close = False
    self.pack_outlet_temperature = float()
    def __init__(self):
        print("The pack was created!")

    def attitude(self, condition):
        self.pack_flow_attitude = condition
        if condition == True:
            print("Pack flow : On")
        elif condition == False:
            print("Pack flow : Off")
        else:
            raise Exception("There is a problem...")
        # if True:on | False:off

    def set_pack_flow(self, condition):
        if self.pack_flow_attitude == True :
            condition = condition.lower()
            self.pack_flow = condition
            print("Pack Flow set: Low")
        elif self.pack_flow_attitude == False:
            print("You must turn on the pack then set pack flow.")
        else:
            raise Exception("There is a problem!")
        return
