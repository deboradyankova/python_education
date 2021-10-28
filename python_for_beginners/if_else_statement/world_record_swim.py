RESISTANCE_PER_15_M = 12.5
BREAK_POINT_TO_ADD_RESISTANCE = 15

current_world_record = float(input('current world record'))
distance_m = int(input('distance'))
time_sec_per_m = float(input('time per meter'))

slow_downs = distance_m // BREAK_POINT_TO_ADD_RESISTANCE

total_time_sec = distance_m * time_sec_per_m
total_time_sec += slow_downs * RESISTANCE_PER_15_M

if current_world_record > total_time_sec:
    print(f" Yes, he succeeded! The new world record is {total_time_sec:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time_sec - current_world_record:.2f} seconds slower.")