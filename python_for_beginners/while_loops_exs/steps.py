STEPS_TARGET = 10000

overall_steps = 0

while True:
    current_steps = input()

    if current_steps == 'Going home':
        current_steps = int(input())
        overall_steps += current_steps
        break

    overall_steps += int(current_steps)

    if overall_steps >= STEPS_TARGET:
        overall_steps = overall_steps
        break

if overall_steps >= STEPS_TARGET:
    print(f'Goal reached! Good job!')
    print(f'{overall_steps - STEPS_TARGET} steps over the goal!')
else:
    print(f'{abs(STEPS_TARGET - overall_steps)} more steps to reach goal.')
