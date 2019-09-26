
def BinarySearch(arr,searchData):
    
    start = 0
    end = len(arr)-1

    while start <= end:

        mid = (start+end)//2

        if arr[mid] == searchData:
            globals()['index'] = mid+1
            return True
        else:
            if searchData < arr[mid]:
                end = mid-1
            else:
                start = mid + 1
    return False

if __name__ == '__main__':

    arr = [1, 3, 5, 8, 9, 45, 56, 78, 4534, 34534]

    n = 50
    
    if BinarySearch(arr,n):
        print(f'Found! Index: {index}')
    else:
        print(f"Oh Sorry! {n} Not Found")
