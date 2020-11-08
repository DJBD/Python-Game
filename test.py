import random
plus_x_range, y_range = random.randint(0, 1920), random.choice([1200, -500])
x_range, pos_y_range = random.choice([-200,2000]), random.randint(0,1080)

HW, HH = random.choice([(plus_x_range, y_range), (x_range, pos_y_range)])
print(HW, HH)