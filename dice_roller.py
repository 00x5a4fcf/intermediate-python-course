import random

def main():
  dice_rolls = int(input('How many dice would you like to roll? ')) #ask 4 user input on how many rolls = dice_roll
  dice_size = int(input('How many sides do the dice have?')) #ask 4 user input on size = dice_size
  dice_sum = 0
  #creates var dice_sum and sets value to 0
  for i in range(0,dice_rolls):
    #for every index in a range starting after 0 until the value is equal to dice_rolls, do this:
    roll = random.randint(1,dice_size)
    #roll equals random number between 1 and var dice_size from user
    dice_sum += roll
    #Also can be written as [dice_sum = dice_sum + roll]
    if roll == 1:
      print (f'You rolled a {roll}! Critical Fail') #IF 1 print this
    elif roll == dice_size: #also if roll is = to highest value set by user dice_size print CRIT
      print(f'You rolled a {roll}! Critical Success')
    else:
      print(f'You rolled a {roll}') #otherwise print roll
  print(f'You have rolled a total of {dice_sum}') #prints value created by sum
  #above print is not indented since that would include it in the 4loop

if __name__== "__main__":
  main()
