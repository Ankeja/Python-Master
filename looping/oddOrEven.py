#runs through 1-20 and says if it is odd or even, says 4 and 13 are unlucky.
for number in range(1,21):
    if number == 4:
        print(str(number)+" is unlucky")
    elif number == 13:
        print(str(number)+" is unlucky")
    elif number % 2 == 0:
        print(str(number)+" is even")
    else:
        print(str(number)+" is odd")

#i could have used f-string i.e. f"{number} is unlucky"

#class version (less print statements)
# for num in range(1, 21):
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")