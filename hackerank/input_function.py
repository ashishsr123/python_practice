if __name__ == '__main__':
    #marksheet =[]
    #scores = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = int(input())
    #     scores.append(score)
    #     marksheet += [[name,score]]
    n = int(input())
    marksheet = [ [input(), float(input())] for _ in range(n)]
    sorted_scores =   sorted(list(set([score  for name , score in marksheet ])))[1]
    for a,b in sorted(marksheet):
        if b == sorted_scores:
            print(a)
