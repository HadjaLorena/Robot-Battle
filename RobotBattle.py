
def build_robot():
    robot_name = input("Give a name for your robot: ").upper()
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.manage_parts_points()
    robot.print_status()
    return robot

def print_rules():
  print("----" * 10)
  print("How to win:")
  print("1. Destroy your enemy head")
  print("2. Destroy all parts of your enemy")
  print("3. Make your enemy use all of it core's energy")
  print("4. If your enemy give up")

def choose_color():
  available_colors = colors

  color_loop = True

  while(color_loop == True):
    print("Available colors:")

    for key, value in available_colors.items():
      print(value, key)
      print(menu_colors["WHITE"])
    chosen_color = input("Give a color to your robot: ").upper()

    for key, value in available_colors.items():

      if(chosen_color == key):
        color_code = available_colors[chosen_color]
        colors.pop(chosen_color) # quando um jogador seleciona uma cor, ela não está mais disponível para o outro jogador
        return color_code

    print("----" * 10)
    print("Select a valid color!")
    print("----" * 10)
  
def check_winner(current_robot, enemy_robot):
  playing = True

  if(enemy_robot.is_there_available_part() == False):
    playing = False
    print("----" * 10)
    print(f"All parts of robot {enemy_robot.name} were destroyed!")
    print(f"The winner is robot {current_robot.name}!")
    print("----" * 10)
    return playing

  elif(enemy_robot.has_health() == False):
    playing = False
    print("----" * 10)
    print(f"The HP of robot {enemy_robot.name} is 0!")
    print(f"The winner is robot {current_robot.name}!")
    print("----" * 10)
    return playing

  elif(current_robot.is_on() == False):
    playing = False
    print("----" * 10)
    print(f"The core's energy of {current_robot.name} has been completely depleted!")
    print(f"The winner is robot {enemy_robot.name}!")
    print("----" * 10)
    return playing

  elif(enemy_robot.parts[0].is_available() == False):
    playing = False
    print("----" * 10)
    print("Your enemy's vital point has been destroyed!")
    print(f"The winner is robot {current_robot.name}!")
    print("----" * 10)
    return playing
  
  return playing

def give_up_battle(enemy_robot):
  give_up_loop = True
  playing = True

  while(give_up_loop == True):
    player_answer = input("Do you want to leave the battle? Your adversary will win (YES or NO): ").lower()
    
    if(player_answer == "yes"):
      continue_battle_loop = False
      print("----" * 10)
      print(f"The winner is robot {enemy_robot.name}!")
      print("Until the next robot battle.")
      print("----" * 10)
      playing = False
      return playing

    elif(player_answer == "no"):
      print("----" * 10)
      print("Glad you decided to play some more.")
      print("----" * 10)
      return playing
    
    else:
      print("----" * 10)
      print("Select a valid answer!")
      print("----" * 10)

def play():
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1:")
    robot_one = build_robot()
    print("Datas for player 2:")
    robot_two = build_robot()
    
    current_robot = robot_one
    enemy_robot = robot_two
    round = 0
    
    while playing:
        if(round % 2 == 0):
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one

        current_robot.print_status()
        print(f"Select from the options above which part of the robot {current_robot.name} you would like to use to attack your enemy:")
        print("Or if you want to leave the battle select [7]:")
        part_to_use = input("Enter your answer (only numbers are accepted): ")
        part_to_use = int(part_to_use)
        
        if(part_to_use >= 0 and part_to_use < 6):
          if(current_robot.parts[part_to_use].is_available() == True):
            enemy_robot.print_status()
            print(f"Select from the options above which part of the robot {enemy_robot.name} you would like to attack:")
            part_to_attack = input("Enter your answer (only numbers are accepted): ")
            part_to_attack = int(part_to_attack)
            
            if(part_to_attack >= 0 and part_to_attack < 6):

              current_robot.attack(enemy_robot, part_to_use, part_to_attack)

              round = round + 1
             
              playing = check_winner(current_robot, enemy_robot)
              
            else:
              print("----" * 10)
              print("Select a valid option!")
              print("----" * 10)

          else:
            print("----" * 10)
            print("The selected part isn't available, select another part!")
            print("----" * 10)

        elif(part_to_use == 6):
          recharged = current_robot.energy_recharge()

          if(recharged == True):
            round = round + 1

          else:
            print("Play again!")

        elif(part_to_use == 7):
          playing = give_up_battle(enemy_robot)

        else:
          print("----" * 10)
          print("Select a valid answer!")
          print("----" * 10)

main_menu_loop = True

print("Ladies and Gentlemen,")
print("Welcome to the robot battle arena!")
print("Choose your seats, grab your popcorn and place your bets,")
print("The battle will begin!")

while(main_menu_loop == True):

  print("----" * 10)
  print("[1] Play")
  print("[2] Rules")
  print("[3] Exit")

  player_answer = input("Select your option: ")

  if(player_answer == "1"):
    print("----" * 10)
    play()

  elif(player_answer == "2"):
    print_rules()
  
  elif(player_answer == "3"):
    player_answer = input("Do you want to leave the game? (YES or NO): ").lower()
    
    if(player_answer == "yes"):
      main_menu_loop = False
      print("----" * 10)
      print("Until the next robot battle.")
        
    elif(player_answer == "no"):
      print("----" * 10)
      print("Glad you decided to play some more.")

    else:
      print("----" * 10)
      print("Select a valid answer!")
    
  else:
    print("----" * 10)
    print("Select a valid answer!")