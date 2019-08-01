def count_val(val,values):
    count = 0
    # for num in values:
    #     if val == num:
    #         count+=1
    # return count
    num12 = [count + i for num in  enumerate(values) if val == num]

    return  num12

if __name__ == '__main__':
    values = [ 1, 2,2,2,4,5,66,66,7,6,8,99,9,0,0,0]
    val = int(input())
    n1 = count_val(val,values)
    num123 = count_val(val,values)
    count1 =0
    num1234 = [count1 + i for num in  enumerate(values) if val == num]
    #print(type(count_val(val)))
    #print(" occurence of ",val,n12)
    print(num123)
    print(num1234)