import math, random
#1 simulation two six-sided dice rolls 
roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
#2comute and print the outcomes 
print(f"Roll 1: {roll1} | Roll 2:{roll2}")
total_sum = roll1 + roll2
print(f"sum: {total_sum}")
#3. calcuate and print squre root 
root_value = math.sqrt(total_sum)
print(f"Square root of sum: {root_value}")