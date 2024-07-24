def binary_search(arr, x):
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    result = []
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            result.append(mid)
            for i in range(mid-1, -1, -1):
                if arr[i] == x:
                    result.append(i)
                else:
                    break
            for i in range(mid+1, len(arr)):
                if arr[i] == x:
                    result.append(i)
                else:
                    break
            return result
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return "Angka {} tidak ada dalam array".format(x)

array = [19, 40, 10, 90, 2, 50, 60, 50, 1]

x = 1
result_a = binary_search(array, x)
print(f"Input : {x}")
if isinstance(result_a, list):
    print(f"Output : Angka {x} ada di indeks ke {result_a}")
else:
    print(f"Output : {result_a}")

x = 50
result_b = binary_search(array, x)
print(f"\nInput : {x}")
if isinstance(result_b, list):
    print(f"Output : Angka {x} ada di indeks ke {result_b}")
else:
    print(f"Output : {result_b}")

x = 100
result_c = binary_search(array, x)
print(f"\nInput : {x}")
if isinstance(result_c, list):
    print(f"Output : Angka {x} ada di indeks ke {result_c}")
else:
    print(f"Output : {result_c}")
