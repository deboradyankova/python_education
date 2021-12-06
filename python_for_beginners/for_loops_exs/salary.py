websites = {
    'FACEBOOK': 150,
    'INSTAGRAM': 100,
    'REDDIT': 50,
}

open_tabs_count = int(input('tabs'))
salary = float(input('salary'))

for _ in range(open_tabs_count):
    site_name = input().upper()

    if site_name in websites.keys():
        salary -= websites[site_name]

if salary <= 0:
    print('You have lost your salary')
else:
    print(f'{salary:.2f}')
