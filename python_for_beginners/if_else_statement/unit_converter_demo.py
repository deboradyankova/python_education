def mm_to_cm(number):
    return number * 10


def mm_to_m(number):
    return number / 1000


def cm_to_mm(number):
    return number / 10


def cm_to_m(number):
    return number / 100


def m_to_mm(number):
    return number * 1000


def m_to_cm(number):
    return number * 100


MAPPER = {
    'mm': {
        'cm': mm_to_cm,
        'm': mm_to_m,
    },
    'cm': {
        'mm': cm_to_mm,
        'm': cm_to_m,
    },
    'm': {
        'mm': m_to_mm,
        'cm': m_to_cm,
    }
}

number = float(input('Number'))
unit_type_input = str(input('Unit type input'))
unit_type_output = str(input('Unit type output'))

result = MAPPER[unit_type_input][unit_type_output]
result = result(number)
print(result)
