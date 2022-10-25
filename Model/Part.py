class Part():
    
    def __init__(self, name: str, attack_level=0, armor_defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.armor_defense_level = armor_defense_level
        self.energy_consumption = energy_consumption
        
    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.armor_defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }
        
    def reduce_defense(self, attack_level):
        self.armor_defense_level = self.armor_defense_level - attack_level

        if(self.armor_defense_level <= 0):
            self.armor_defense_level = 0
    
    def is_available(self):
      return self.armor_defense_level > 0