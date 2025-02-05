if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = [i for i in arr]
    def max_finder(arr):
        max = arr[0]
        for i in arr:
            if i > max:
                max = i
        return max
    max1 = max_finder(arr) 
    while max1 in arr:
        arr.remove(max_finder(arr))
    print(max_finder(arr))
        
        
