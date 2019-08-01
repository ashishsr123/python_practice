import math
if __name__ == '__main__':
    n = int(input())
    num_array = [ int(num) for num in input().split() ]
    print(num_array)
    mean = 0
    for num in num_array:
        mean+= num
    print("mean: ",mean/len(num_array))
