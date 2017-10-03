from decimal import Decimal

def check(strnumber):
    number = Decimal(strnumber)
    exp = '%.5E' % number
    left = exp.split('E')[0].rstrip('0').rstrip('.')
    right = exp.split('E')[1]
    return left + 'E' + right