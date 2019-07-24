
def bin_search(arr, target):
    head = 0
    tail = len(arr)-1
    if arr[head] == target or arr[tail] == target:
            return 1
    while head < tail-1:
        mid = (head+tail)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            tail = mid
        else:
            head = mid
    return 0

def find_pair(arr, target):
    arr = sorted(arr)
    res = 0
    for i in range(len(arr)):
        if arr[i] > target:
            res += bin_search(arr[:i], arr[i]-target)
    return res

def find_pair_2(arr,target):
    large,small = 1,0
    arr = sorted(arr)
    res = 0
    while large < len(arr):
        if small == large:
            large += 1
        if arr[large]-arr[small] == target:
            res += 1
            large+= 1
            small += 1
        elif arr[large]-arr[small] < target:
            large += 1
        else:
            small += 1
    return res
        




if __name__ == "__main__":
    assert find_pair_2([1,5,3,4,2], 2) == 3, "get {}".format(find_pair([1,5,3,4,2], 2))
    assert find_pair_2([1,2], 1) == 1, "get {}".format(find_pair_2([1,2], 1))
    assert find_pair_2([1,2], 2) == 0, "get {}".format(find_pair_2([1,2], 2))
    assert find_pair_2([10,20,30,40,50], 10) == 4, "get {}".format(find_pair_2([10,20,30,40,50], 10))
    print("finished")