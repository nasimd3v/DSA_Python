def LinearSearch(arr,SearchData):
    start = 0
    end = len(arr)-1

    for i in range(start,end):
        if arr[i] == SearchData:
            return f"Found index at {i+1}"
    return "Not Found"


if __name__ == '__main__':
    arr = [24,45,434,23,423,423,23,423,423,4,56,657,435,33]

    n = 423435

    print(LinearSearch(arr,n))
