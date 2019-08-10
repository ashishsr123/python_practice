

if __name__ == '__main__':
    N = int(input())
    simple_list = []
    for _ in range(N):
        user_input = input()
        input_list = user_input.split()
        if input_list[0] == 'insert':
            #simple_list[input_list[1]] = input_list[2]
            simple_list.insert(int(input_list[1]),int(input_list[2]))
        elif input_list[0] == 'print':
            print(simple_list)
        elif input_list[0] == 'remove':
            simple_list.remove(int(input_list[1]))
        elif input_list[0] == 'append':
            simple_list.append(int(input_list[1]))
        elif  input_list[0] == 'sort':
            simple_list.sort()
        elif input_list[0] == 'pop':
            simple_list.pop()
        elif input_list[0] == 'reverse':
            simple_list.reverse()
        else :
            print( "incorrect option ")


#     n = input()
# l = []
# for _ in range(n):
#     s = input.split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print (l)

            