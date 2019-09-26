def BinarySearch(arr,searchData):

    start = 0
    end = len(arr)-1

    while True:

        mid = (start+end)//2

        if searchData == arr[mid]:
            print(f"Found ! Index: {mid+1}")
            break
    else:
        if searchData < arr[mid]:
            end = mid-1
        else:
            start = mid + 1

if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 45, 56, 56, 56, 78, 4534, 34534]
    BinarySearch(arr,45)
