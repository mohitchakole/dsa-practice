# print 1 to n using recursion

def print_num(i, n):
    if i > n:
        return
    print(i, end=" ")
    print_num(i+1, n)

print_num(1, 8)
