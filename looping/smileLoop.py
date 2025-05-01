#prints a smiley emoji on each lie, the number of emoji's increases by 1 each time until 10
for num in range(1, 11):
    times = 1
while times < 11:
    print("\U0001f600"*times)
    times += 1


    