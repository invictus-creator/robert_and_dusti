import math

small = int(input("Enter the smaller number: "))
large = int(input("Enter the larger number: "))
max_tries = math.ceil(math.log2(large - small))

count = 0
while count < max_tries:
    print(small, large)
    n = (small + large) // 2
    print("Your number is", n)
    count += 1
    choice = input("Enter =, <, or >: ")
    if choice == '=':
        print("Hooray, I've got it in", count, "tries!")
        break
    elif choice == '<':
        large = n-1
    else:
        small = n+1
    if count == max_tries:
        print("I'm out of guesses, and you cheated!")
        break
        