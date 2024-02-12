def find_duplicates(nums):
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    duplicates = [num for num, freq in freq_dict.items() if freq > 1]
    
    return duplicates


integer_array = [1, 2, 3, 4, 2, 7, 8, 1, 4]
duplicate_numbers = find_duplicates(integer_array)
print("Duplicate numbers:", duplicate_numbers)
