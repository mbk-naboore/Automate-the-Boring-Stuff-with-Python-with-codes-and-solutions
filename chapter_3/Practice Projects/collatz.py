def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1
    pass


try:
    user_input_number = int(input('Enter a number greater than one: '))
    while True and user_input_number > 0:
        if user_input_number != 1:
            user_input_number = collatz(user_input_number)
            print(user_input_number)
        else:
            break
    else:
        print("You entered 0 or less, for that try again...")
except:
    print('Error: you can not enter anything other than numbers.')
