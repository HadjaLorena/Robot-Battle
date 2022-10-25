from Model.Part import Part

class Robot:
  def __init__(self, name, color_code):
    self.name = name
    self.color_code = color_code
    self.energy = 100
    self.health = 100
    self.on = True
    self.parts = [
      Part("Head", attack_level=5, armor_defense_level=100, energy_consumption=5),
      Part("Weapon", attack_level=18, armor_defense_level=10, energy_consumption=15),
      Part("Left Arm", attack_level=10, armor_defense_level=20, energy_consumption=10),
      Part("Right Arm", attack_level=7, armor_defense_level=20, energy_consumption=5),
      Part("Left Leg", attack_level=12, armor_defense_level=20, energy_consumption=10),
      Part("Right Leg", attack_level=10, armor_defense_level=20, energy_consumption=5),
    ]
  

  def manage_parts_points(self):
    points_available = 10

    while(points_available > 0):
      
      self.print_status()
      print("----" * 10)
      print("Available parts to upgrade:")
      print("[0] Head")
      print("[1] Weapon")
      print("[2] Left Arm")
      print("[3] Right Arm")
      print("[4] Left Leg")
      print("[5] Right Leg")

      part_to_upgrade = int(input("Select a part to upgrade: "))

      if(part_to_upgrade >= 0 and part_to_upgrade < 6):
        print("----" * 10)
        print("[1] Attack Level")
        print("[2] Armor Defense Level")

        part_attribute = input("Select attack or defense to upgrade: ")

        if(part_attribute == "1"):
          print(f"You have {points_available} to use")
          
          user_input = int(input("How many points you want to use: "))

          if(user_input <= points_available):
            points_available = points_available - user_input

            self.parts[part_to_upgrade].attack_level = self.parts[part_to_upgrade].attack_level + user_input

          else:
            print("You don't have enough points")

        elif(part_attribute == "2"):
          print(f"You have {points_available} points to use")
        
          user_input = int(input("How many points you want to use: "))

          if(user_input <= points_available):
            points_available = points_available - user_input

            self.parts[part_to_upgrade].armor_defense_level = self.parts[part_to_upgrade].armor_defense_level + user_input

          else:
            print("You don't have enough points")

        else:
          print("Select a valid option!")

      else:
        print("Select a valid option!")

  def print_status(self):
      print(self.color_code)
      str_robot = robot_art.format(**self.get_part_status())
      self.greet()
      self.print_energy_and_system()
      print(str_robot)
      print(menu_colors["WHITE"])
  

  def greet(self):
      print(f"Hello, I'm robot {self.name}")
  

  def print_energy_and_system(self):
      print(self.color_code)
      print(f"SYSTEM OPERATIONAL: {self.on}")
      print(f"CURRENT ENERGY OF THE CORE: {self.energy}")
      print(f"HEALTH STATUS: {self.health}")

  def reduce_health(self, attack_level):
    self.health = self.health - attack_level

    if(self.health <= 0):
      self.health = 0
      
  def has_health(self):
    if(self.health == 0):
      return False
    return True
  
  def get_part_status(self):
    part_status = {}
    for part in self.parts:
      status_dict = part.get_status_dict()
      part_status.update(status_dict)
    return part_status
    

  def is_there_available_part(self):
      for part in self.parts:
        if part.is_available():
            return True
      return False
  

  def is_on(self):
          return self.energy >= 0

  def attack(self, enemy_robot, part_to_use, part_to_attack):
      if(enemy_robot.parts[part_to_attack].armor_defense_level == 0):
        enemy_robot.reduce_health(self.parts[part_to_use].attack_level)
        self.energy -= self.parts[part_to_use].energy_consumption

      else:
        enemy_robot.parts[part_to_attack].reduce_defense(self.parts[part_to_use].attack_level) 
        self.energy -= self.parts[part_to_use].energy_consumption
  
  def get_part_status(self):
          part_status = {}
          for part in self.parts:
              status_dict = part.get_status_dict()
              part_status.update(status_dict)
          return part_status

  def energy_recharge(self):
    if(self.energy < 100):
      self.energy = self.energy + 5
      print(f"REMAINING ENERGY: {self.energy}")
      return True

    else:
      print("----" * 10)
      print("CORE FULLY ENERGIZED, THIS OPERATION CANNOT BE PERFORMED!")
      return False




robot_art = r"""
          [0]: {head_name}
          |Is available: {head_status}
          |Attack Level: {head_attack}                              
          |Armor Defense Level: {head_defense}
          |Energy consumption: {head_energy_consump}
                  ^
                  |                  [1]: {weapon_name}
                  |                  |Is available: {weapon_status}
        ____      |    ____          |Attack Level: {weapon_attack}
        |oooo|  ____  |oooo| ------> |Armor Defense Level: {weapon_defense}
        |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
        |oooo|/\_||_/\|oooo|       
        `----' / __ \  `----'          [2]: {left_arm_name}
      '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
      /  \|#|| |/\| ||#|/  \           |Attack Level: {left_arm_attack}
      / \_/|_|| |/\| ||_|\_/ \         |Armor Defense Level: {left_arm_defense}
    |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
    <_>      |=\__/=|      <_> ------> 
    <_>      |------|      <_>       [3]: {right_arm_name}
    | |   ___|======|___   | |       |Is available: {right_arm_status}
   // \\ / |O|======|O| \  //\\      |Attack Level: {right_arm_attack}
   |  |  | |O+------+O| |  |  |      |Armor Defense Level: {right_arm_defense}
   |\/|  \_+/        \+_/  |\/|      |Energy consumption: {right_arm_energy_consump}
   \__/ _|||        |||_   \__/        
        | ||        || |          [4]: {left_leg_name} 
       [==|]        [|==]         |Is available: {left_leg_status}
       [===]        [===]         |Attack Level: {left_leg_attack}
        >_<          >_<          |Armor Defense Level: {left_leg_defense}
       || ||        || ||         |Energy consumption: {left_leg_energy_consump}
       || ||        || || ------> 
       || ||        || ||          [5]: {right_leg_name}
     __|\_/|__    __|\_/|__        |Is available: {right_leg_status}
    /___n_n___\  /___n_n___\       |Attack Level: {right_leg_attack}
               |                   |Armor Defense Level: {right_leg_defense}
               |                   |Energy consumption: {right_leg_energy_consump}
               |
               |
               |
               \_________________>|.o.| [6]: Recharge Energy                   
    """

colors = {
            "BLACK": '\x1b[90m',
            "BLUE": '\x1b[94m',
            "CYAN": '\x1b[96m',
            "GREEN": '\x1b[92m',
            "MAGENTA": '\x1b[95m',
            "RED": '\x1b[91m',
            "WHITE": '\x1b[97m',
            "YELLOW":'\x1b[93m',
        }

menu_colors = {"WHITE": '\x1b[97m'}