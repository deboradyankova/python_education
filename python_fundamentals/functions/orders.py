def product(products, quantity):
    prices = {
        'coffee': 1.5,
        'water': 1,
        'coke': 1.4,
        'snacks': 2,
    }
    return prices[products] * quantity


products = input()
quantity = int(input())

print(f' {product(products, quantity):.2f}')
