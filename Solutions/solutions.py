# maximum product of any continuous subarray
def maxProductSubarray(nums):
    max_val = nums[0]
    min_val = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_val, min_val = min_val, max_val
        max_val = max(nums[i], max_val * nums[i])
        min_val = min(nums[i], min_val * nums[i])
        result = max(result, max_val)
    return result


print(maxProductSubarray([2, -3, -3, -2, 4]))


# Valid Parentheses
def isValid(str):
    stack = []
    for element in str:
        if element == "(" or element == "{" or element == "[":
            stack.append(element)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (
                (element == ")" and last != "(")
                or (element == "}" and last != "{")
                or (element == "]" and last != "[")
            ):
                return False
    return len(stack) == 0


print(isValid("({[]})"))


# String Compression
def stringCompression(s):
    count = 1
    new_str = ""
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            new_str += s[i - 1] + str(count)
            count = 1
    return new_str if len(new_str) < len(s) else s


print(stringCompression("aabcccccaaa"))


# Custom Reduce Function Implementation
def my_function(arr, callback, intial_value):
    accumulator = intial_value
    for i in range(len(arr)):
        accumulator = callback(accumulator, arr[i])
    return accumulator


num = [1, 2, 3, 4]
result = my_function(num, lambda acc, curr: acc + curr, 0)
print("num:", result)


# Single number
def single_number(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
    return xor


print(single_number([1, 1, 4, 2, 2]))


# Find Missing number using xor
def find_missing(arr, n):
    xor = 0
    for i in range(1, n + 1):
        xor ^= i
    for num in arr:
        xor ^= num
    return xor


print(find_missing([1, 2, 3, 5], 5))


# Find Duplicate Elements in an Array
def find_duplicates(arr):
    freq_map = {}
    duplicates = []
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    for key, value in freq_map.items():
        if value > 1:
            duplicates.append(key)
    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))


# Rotate Array by K Steps (Right Rotation)
def rotate_array(arr, k):
    result = []
    arr_len = len(arr)
    for i in range(arr_len - k, arr_len):
        result.append(arr[i])
    for i in range(0, arr_len - k):
        result.append(arr[i])
    return result


print(rotate_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))


# Product of Array Except Self
def product_except_self(arr):
    newArr = []
    for i in arr:
        prod = 1
        for j in arr:
            if i != j:
                prod = j * prod
        newArr.append(prod)
    return newArr


print(product_except_self([1, 2, 3, 4]))


# toLowerCase
def to_lower_case(str):
    result = ""
    for i in range(len(str)):
        char_code = ord(str[i])
        # ord(): returns the Unicode code point
        if char_code >= 65 and char_code <= 90:
            # chr() : reverse of ord()
            result += chr(char_code + 32)
        else:
            result += str[i]
    return result


print(to_lower_case("RAJESH aNANta paTIL"))


# First Unique Character in a String
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in freq:
        if freq[char] == 1:
            return char


print(first_unique_char("lovelveetcode"))


# Check if Two Strings are Isomorphic
def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    obj1 = {}
    obj2 = {}
    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]
        if char1 in obj1 and obj1[char1] != char2:
            return False
        if char2 in obj2 and obj2[char2] != char1:
            return False
        obj1[char1] = char2
        obj2[char2] = char1
    return True


print(is_isomorphic("egg", "add"))


# Find the Intersection of Two Arrays
def intersection(arr1, arr2):
    new_arr = []
    for i in arr1:
        if i in arr2:
            new_arr.append(i)
            arr2.remove(i)
    return new_arr


print(intersection([1, 2, 2, 3, 4], [2, 2, 4, 6, 5, 1]))


# Find the Longest Common Prefix
def longest_common_prefix(arr):
    arr.sort()
    first_word = arr[0]
    last_word = arr[-1]
    new_str = ""
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] == last_word[i]:
            new_str += first_word[i]
        else:
            break
    return new_str


print(longest_common_prefix(["apple", "app", "application"]))


# Check if two strings are anagrams
def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    s1 = "".join(sorted(str1.lower()))
    s2 = "".join(sorted(str1.lower()))
    return s1 == s2


print(isAnagram("listen", "silent"))


# Longest Substring Without Repeating Characters
def longest_substring(s):
    max_length = 0
    arr = []
    for char in s:
        while char in arr:
            arr.pop(0)
        arr.append(char)
        max_length = max(max_length, len(arr))
    return max_length


print(longest_substring("abcdabcbb"))


# find the index from elements started repeating
def repeating(arr):
    s = set()
    for i in arr:
        s.add(i)
    return len(s)


print(repeating([1, 2, 3, 4, 5, 6, 1, 2]))


# Merge Two Sorted Arrays
def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


print(merge_sorted_arrays([1, 2, 3, 5, 7], [4, 6]))


# Check if a string is a palindrome
# start → where to begin
# stop → where to end (not included)
# step → how many positions to move each time

text = "madam"
reversed_text = text[
    ::-1
]  # variable[Start from here : Stop before here : Move by this many steps]
if reversed_text == text:
    print("Palindrome")
else:
    print("Not Palindrome")


# Move All Zeros to End
def move_zeros(arr):
    new_arr = []
    for i in range(0, len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])

    j = len(new_arr)
    while j < len(arr):
        new_arr.append(0)
        j += 1
    return new_arr


print(move_zeros([0, 1, 0, 3, 12]))


# Reverse Words in a Sentence
def reverse_words(text):
    result = []
    words = text.split(" ")
    for i in words:
        reverse_word = i[::-1]
        result.append(reverse_word)
    return " ".join(result)


print(reverse_words("hello world"))


# Count frequency of each character in a string.
def char_count(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count


print(char_count("aabbc"))



# LeetCode 394 - Decode String
def decode_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for ch in s:
        if ch.isdigit():
            current_number = current_number * 10 + int(ch)
        elif ch == "[":
            stack.append(current_string)
            stack.append(current_number)
            current_number = 0
            current_string = ""
        elif ch == "]":
            repeat = stack.pop()
            prevStr = stack.pop()
            current_string = prevStr + current_string * repeat
        else:
            current_string += ch
    return current_string
print(decode_string("2[a2[cd]]"))





# LeetCode 209 - Minimum Size Subarray Sum
def min_subarray_len(target, arr):
    total = 0
    left = 0
    min_length = float("inf")
    for right in range(len(arr)):
        total += arr[right]
        while total >= target:
            current_length = right - left + 1
            if min_length > current_length:
                min_length = current_length
            total -= arr[left]
            left += 1
    return 0 if min_length == float("inf") else min_length
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))




# Find the Maximum Occurring Character in a String
def max_occurring_char(s):
    freq = {}
    max_count = 0
    char = ""
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

        if freq[ch] > max_count:
            max_count = freq[ch]
            char = ch
    return char
print(max_occurring_char("hello"))



# Maximum Sum of K Consecutive Elements
def max_sum_subarray(arr, k):
    window_sum = 0
    # Calculate the sum of the first window
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
print(max_sum_subarray([2, 1, 10, 1, 3, 2], 3))



# Count of Zeros and Ones in an Array
def count_zeros_and_ones(arr):
    ones = 0
    for i in range(len(arr)):
        ones += arr[i]
    print("Count of 1 is:", ones)
    print("Count of 0 is:", len(arr) - ones)
count_zeros_and_ones([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])