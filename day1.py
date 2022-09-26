def fibonacci(position):
    if position < 2:        # 0 o 1
        return position
    else:
        # Llamada recursiva
        return fibonacci(position-1) + fibonacci(position-2)


def print_list_fibonacci(limit):
    for i in range(limit):
        # print the fibonacci of each i position
        print(fibonacci(i))  


def sum_fibonacci(limit):
    sum = 0
    for i in range(limit):
        # Adding the fibonacci of each i position
        sum += fibonacci(i)    
    return sum

# Test
print_list_fibonacci(5)
print(fibonacci(3))
print(sum_fibonacci(3))
