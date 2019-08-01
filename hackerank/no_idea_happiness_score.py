if __name__ == '__main__':
    n ,m = input().split()
    num_list = [int(num) for num in input().split()]
    A = set([ int(num) for num in input().split()])
    B = set([ int(num) for num in input().split()])
    score = 0
    # for num_a in A:
    #     if num_a in num_list:
    #         score+=1
    # for num_b in B:
    #     if num_b in num_list:
    #         score-=1
    # print(score)

    score = sum(((i in A) - ( i in B) for i in num_list))
    print(score)