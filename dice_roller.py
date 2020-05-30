<<<<<<< HEAD
import random

def main():
  dice_rolls = 2
  #creates variable dice_rolls (4loop)
  dice_sum = 0
  #creates variable dice_sum and sets value to 0
  for i in range(0,dice_rolls):
    #for every index in a range starting after 0 until the value is equal to dice_rolls, do this:
    roll = random.randint(1,6)
    #roll equals random number between 1,6 including each
    dice_sum += roll
    #Also can be written as [dice_sum = dice_sum + roll]
    print(f'You rolled a {roll}')
    #prints each roll
  print(f'You have rolled a total of {dice_sum}') #prints value created by sum
  #above print is not indented since that would include it in the 4loop

if __name__== "__main__":
  main()







