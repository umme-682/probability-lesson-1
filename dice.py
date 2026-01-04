import random

def dice_exp():
    dice = ['1', '2', '3', '4', '5', '6']
    
    result = random.choice(dice)
    
    pro = dice.count('4')/len(dice)
    print("Probability of Picking 4 is: ", pro)
    
    if result == '4': 
        return '4 was Picked'
    else:
        return 'Better Luck Next Time'
    
res = dice_exp()
print(res)