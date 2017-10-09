# https://www.reddit.com/r/dailyprogrammer/759fha/

def sum(listname):
    total, length = 0, len(listname)
    for x in range(length):
        for y in range(x + 1, length):
            if listname[y] == listname[x] + 1:
                total += y - x
                break
    return total