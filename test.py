def divisible(arr):
    result  = []
    for i in arr:
        if i % 3 == 0:
            result.append(i)
    return result

test_arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
print(divisible(test_arr))