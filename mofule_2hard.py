import random


def pick():
    num_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    stone_num_ = random.choice(num_)
    return stone_num_


result = ''
stone_num_ = pick()
print(stone_num_)
for i in range(1, stone_num_):
    for j in range(i + 1, stone_num_):
        if stone_num_ % (i + j) == 0:
            result += str(i) + str(j)

print(int(result))
