# HHam tinh luy thua 
# Vi du:
#   2^3 = 8
#   3^2 =9
print(3**2)

def calculate_power(base_number, exponent):
    result = 1 
    for index in range(exponent):
        result = result * base_number
    return result

print(calculate_power(2, 3))
