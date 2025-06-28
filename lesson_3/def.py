def say_hi_name(name):
    print(f"Привет, {name}")
    
name = 'Вася' 


# say_hi_name('Вася')

# def count_num(num1, num2):
#     result = num1+num2
#     return print(result)

# number1 = 5
# number2 = 17

# count_num(number1, number2)

def get_numbers():
    one_numb = int(input('enter first num '))
    second_numb = int(input('enter second num '))

    return one_numb, second_numb

def summ_numbers():
    one, two = get_numbers()
    result = one + two
    return result

def print_result():
    print(summ_numbers())

print_result()