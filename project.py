def findMinMax(arr):
    n = len(arr)
    # n is even
    # initialize the first two elements as minimum and maximum
    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        # set the starting index for loop
        i = 2
    # n is odd
    # initialize the first element as minimum and maximum
    else:
        mx = mn = arr[0]
        # set the starting index for loop
        i = 1
    # pick elements in pair and compare the pair with max and min
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        i += 2
    return (mx, mn)


n = int(input())
arr_x = []
arr_y = []
for i in range(n):
    x, y = input().split()
    arr_x.append(int(x))
    arr_y.append(int(y))
max_x, min_x = findMinMax(arr_x)
max_y, min_y = findMinMax(arr_y)
print("Maximum x is: ", max_x)
print("Minimum x is: ", min_x)
print("Maximum y is: ", max_y)
print("Minimum y is: ", min_y)
