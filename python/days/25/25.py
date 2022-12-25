# Finality

import math

def to_decimal(snafu):
    if len(snafu) == 1:
        return {
            '=': -2,
            '-': -1,
            '0': 0,
            '1': 1,
            '2': 2
        }[snafu]

    decimal = 0
    for i, l in enumerate(reversed(snafu)):
        decimal += pow(5, i)*to_decimal(l)
    return decimal

def to_snafu(decimal):
    max_len = math.ceil(math.log(decimal, 5))
    snafu = list('2'*max_len)
    for i, l in enumerate(snafu):
        for snaf in ['1','0','-','=']:
            new_snafu = snafu.copy()
            new_snafu[i] = snaf
            if to_decimal(new_snafu) >= decimal:
                snafu = new_snafu
    if(to_decimal(''.join(snafu)) != decimal):
        print("Error, snafu is ", ''.join(snafu), '(', to_decimal(''.join(snafu)), ')', " decimal is ", decimal)
        exit(-1)
    return ''.join(snafu)

def start(line, lines):
    sum = 0
    for l in lines:
        sum += to_decimal(l)
    print(to_snafu(sum))