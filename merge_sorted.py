# def insert(num, l):
#     if not l:
#         return [num]
#     if len(l) == 1:
#         if l[0]<num:
#             return l+[num]
#         return [num]+l
#     mid = len(l)//2
#     if l[mid]<num:
#         return l[:mid] + insert(num, l[mid:])
#     else:
#         return insert(num, l[:mid]) + l[mid:]


def merge(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    result = l1+l2
    curr_1, curr_2, curr = 0,0,0
    while True:
        if curr_1 == len(l1):
            result[curr:] = l2[curr_2:]
            break
        if curr_2 == len(l2):
            result[curr:] = l1[curr_1:]
            break
        else:
            if l1[curr_1] > l2[curr_2]:
                result[curr] = l2[curr_2]
                curr_2 += 1
            else:
                result[curr] = l1[curr_1]
                curr_1 += 1
            curr += 1
    return result

# for m, n be the length of the two lists
# time complexity: O(n+m) worst case
# space complexity: O(n+m)




if __name__=="__main__":
    a, b = [1,3,5,7],[2,4,6,8]
    assert merge(a,b) == [1,2,3,4,5,6,7,8], "wrong input {} output {}".format([a,b], merge(a,b))
    a, b = [1],[2,3]
    assert merge(a,b) == sorted(a+b), "wrong input {} output {}".format([a,b], merge(a,b))
    a, b = [2,3],[1]
    assert merge(a,b) == sorted(a+b), "wrong input {} output {}".format([a,b], merge(a,b))
    a, b = [1,3],[2,4]
    assert merge(a,b) == sorted(a+b), "wrong input {} output {}".format([a,b], merge(a,b))
    a, b = [2,4],[1,3]
    assert merge(a,b) == sorted(a+b), "wrong input {} output {}".format([a,b], merge(a,b))
    a, b = [],[]
    assert merge(a,b) == [], "wrong output {}".format(merge(a,b))