import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    the_list = list()
    for i in range(100):  # each time you increase the loop the percentage will get closer to the 100%...
        the_list.append(random.randint(0, 1))
    count_0 = 0
    count_1 = 0

    for result in the_list:
        if result:
            count_0 = 0
            count_1 += 1
        else:
            count_1 = 0
            count_0 += 1

        if count_1 == 6 or count_0 == 6:
            numberOfStreaks += 1
            count_1 = 0
            count_0 = 0
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

