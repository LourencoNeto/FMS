import random

size = 20
index_list = list(range(size))
print(index_list)
random.Random().shuffle(index_list)
print(index_list)

