import math
def median(input_list):
  middle_num = len(input_list) // 2
  if len(input_list) % 2 == 1:
    return input_list[middle_num]
  else:
    return (input_list[middle_num] + input_list[middle_num - 1]) / 2

list1 = [0, 1, 2, 3, 4, 5, 6]
print("median:" , median(list1))