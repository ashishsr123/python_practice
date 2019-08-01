if __name__ == '__main__':
    #n = int(input())
    # stampCountryName = set([input() for name in range(n)])
    # print(len(stampCountryName))
    #print(len(set(country for country in input())))
    print(len({input() for i in range(int(input()))}))