basketball_training_annual_tax = float(input('Basketball training annual tax'))

sneakers = basketball_training_annual_tax * (1 - 0.4)
equipment = sneakers * (1 - 0.2)
ball = equipment * 0.25
accessories = ball * 0.2

total = sneakers + equipment + ball + accessories + basketball_training_annual_tax

print(total)
