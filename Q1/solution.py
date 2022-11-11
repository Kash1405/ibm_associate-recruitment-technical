if __name__ == '__main__':

    # inputs
    a = int(input())
    shirts = list(input().split())
    b = int(input())
    req = list(input().split())

    # dict for sizes
    size = {'S': [], 'M': [], 'L': []}

    # flag for requirements
    flag = True

    # entering stock
    for i in shirts:
        # count
        c = i.count('X')
        # size
        s = i[-1]
        if s == 'M' or s == 'L':
            size[s].append(c)
        else:
            size[s].append(c*-1)
    # sort sizes dict
    size['S'].sort()
    # size['M'].sort()
    size['L'].sort()

    # checking if all requirements met
    for i in req:
        # count
        c = i.count('X')
        # size
        s = i[-1]

        if s == 'M':
            if len(size['L']) == 0 and len(size['M']) == 0:
                flag = False
                break
        elif s == 'L':
            if size[s][-1] < c:
                flag = False
                break
        else:
            if len(size['L']) == 0 and len(size['M']) == 0 and size[s][-1] < c*-1:
                flag = False
                break
    if flag == True:
        print("Yes")
    else:
        print("No")
