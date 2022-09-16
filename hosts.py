from random import randint
import json
import urllib.request
import time

hosts = ["Ryan Reynolds", "Justin Bieber", "Patrick J. Adams", "Catherine Reitman", "Dan Levy"]

def talk_to_host():
    with open("current_player.json", "r") as game:
        details = json.load(game)
    host =    hosts[randint(0,4)]
    print(f"Welcome {details['username']}, my name is {host} ")
    print("I am interested in buying and selling things!")
    operation = randint(1,2)
    if operation == 1:
      print(f"Hi! I am {host}. I would like to sell you some enery. I know you have {details['money']} CAD")
      print(f"I am here to give you 50 enery point for {round(details['money']/3)}")
      time.sleep(5)
      details['money'] = details['money']/3
      details['energy'] = details['energy'] + 50
      print("Here is you enery. I have your money.")
      print("BYE!!!!!!!!!!")
      time.sleep(5)
      
    if operation == 2:
      tradeenery = randint(25,30)
      print(f"Hi! I am {host}. I would like to trade you 50$ of money for {tradeenery} enery points of your enery")
      ans = input("Do you want to trade? Y/N:")
      if ans.lower == 'n':
        print("okay. I am dying because of you. BYE!!")
      else:
        print("Cool. Thanks Dude!")
        details['money'] = details['money'] + 50
        details['energy'] = details['energy'] - tradeenery
      time.sleep(5)
    with open("current_player.json", "w") as game:
        json.dump(details,game)
    time.sleep(5)
