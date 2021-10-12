deposited_amount = float(input('Deposit amount'))
term_deposit_months = int(input('Term deposit'))
annual_interest_rate = float(input('Annual interest rate'))

monthly_income = ((deposited_amount * annual_interest_rate / 100) / 12)

total = deposited_amount + term_deposit_months * monthly_income

print(total)
