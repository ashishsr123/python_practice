if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print("n :" ,n)
    print("arr : ",arr)
    lis = list(arr) 
    max_lis = max(lis)
    new_list = []
    for n in lis:
        if n != max_lis:
            new_list.append(n)
    print("second largest number is : ", max(new_list))