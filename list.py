if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        arr1 = map(str, input().split(" "))
        arr = [i for i in arr1]
        if arr[0] == "insert":
            i = int(arr[1])
            e = int(arr[2])
            lst.insert(i,e)
        elif arr[0] == 'print':
            print(lst)
        elif arr[0] == 'remove':
            e = int(arr[1])
            lst.remove(e)
        elif arr[0] == 'append':
            e = int(arr[1])
            lst.append(e)
        elif arr[0] == 'sort':
            lst.sort()
        elif arr[0] == 'pop':
            lst.pop()
        elif arr[0] == 'reverse':
            lst.reverse()

        
