from itertools import combinations_with_replacement

input_ = input().split()

new_tuple = tuple(input_[0])
sorted_new_tuple = sorted(new_tuple)

new_list = list(
    combinations_with_replacement(sorted_new_tuple, int(input_[1]))
)

sort = sorted(new_list)

for i in sort:
    print("".join(i))