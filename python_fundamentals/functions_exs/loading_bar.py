def progress_bar(percentage):
    bar = ['.' for _ in range(10)]
    for index in range(percentage // 10):
        bar[index] = '%'
    return bar


percentage = int(input())

if percentage == 100:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
else:
    bar = progress_bar(percentage)
    print(f'{percentage}% [{"".join(bar)}]')
    print('Still loading...')