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


# Find Leaders in an array
def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    leaders.reverse()
    return leaders


print(find_leaders([16, 17, 4, 3, 5, 2]))


# Merge Overlapping Intervals (Medium)
def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        last_interval = result[-1]
        current_interval = intervals[i]
        if current_interval[0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], current_interval[1])
        else:
            result.append(current_interval)
    return result


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))


# Longest Subarray with Sum ≤ K
def longest_subarray(nums, k):
    left = 0
    total = 0
    max_length = 0
    for i in range(len(nums)):
        total += nums[i]
        while total > k:
            total -= nums[left]
            left += 1
        length = i - left + 1
        if length > max_length:
            max_length = length
    return max_length


print(longest_subarray([2, 1, 5, 1, 3, 2], 7))


# Find the Majority Element(element that appears more than n/2 times.)
def majority_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key in freq:
        if freq[key] > len(arr) / 2:
            return key


print(majority_element([2, 1, 1, 3, 3, 3, 3, 3]))


# Two Sum
def two_sum(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return [i, j]
        if arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1


print(two_sum([2, 11, 7, 15], 9))


# Find the Length of the Last Word
def length_of_last_word(str):
    count = 0
    i = len(str) - 1
    while i >= 0 and str[i] == " ":
        i -= 1
    while i >= 0 and str[i] != " ":
        count += 1
        i -= 1
    return count


print(length_of_last_word("   fly me   to   the moon  "))


# LeetCode 42 - Trapping Rain Water(Hard)
def trap(arr):
    left = 0
    right = len(arr) - 1
    leftMax = 0
    rightMax = 0
    water = 0
    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= leftMax:
                leftMax = arr[left]
            else:
                water += leftMax - arr[left]
            left += 1
        else:
            if arr[right] <= arr[left]:
                if arr[right] > rightMax:
                    rightMax = arr[right]
                else:
                    water += rightMax - arr[right]
            right -= 1
    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# LeetCode 11 - Container With Most Water(Medium)
def max_area(arr):
    left = 0
    right = len(arr) - 1
    maxWater = 0
    while left < right:
        width = right - left
        currentArea = min(arr[left], arr[right]) * width
        maxWater = max(currentArea, maxWater)
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
    return maxWater


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# LeetCode 5 - Longest Palindromic Substring(Medium)
def longest_palindrome(str):
    longest = ""
    for i in range(len(str)):
        for j in range(i, len(str)):
            left = i
            right = j
            isPalindrome = True
            while left < right:
                if str[left] != str[right]:
                    isPalindrome = False
                    break
                left += 1
                right -= 1
            if isPalindrome:
                if (j - i + 1) > len(longest):
                    longest = ""
                    for k in range(i, j + 1):
                        longest += str[k]
    return longest


print(longest_palindrome("ikbabad"))


# LeetCode 300 - Longest Increasing Subsequence(Medium)
def length_of_lis(nums):
    tails = []
    for num in nums:
        if len(tails) == 0:
            tails.append(num)
        elif num > tails[-1]:
            tails.append(num)
        else:
            for i in range(len(tails)):
                if tails[i] >= num:
                    tails[i] = num
                    break
    return len(tails)


print("Answer:", length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))


# LeetCode 560 - Subarray Sum Equals K (Medium)
def subarray_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if k == sum:
                count += 1
    return count


print(subarray_sum([1, 2, 3], 3))


# Maximum Difference Between Two Elements
def max_difference(arr):
    diff = 0
    grt = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > grt:
            grt = arr[i]
            for j in range(i - 1, -1, -1):
                current_diff = grt - arr[j]
                if current_diff > diff:
                    diff = current_diff
        else:
            grt = arr[i]
    if diff > 0:
        return diff
    return -1


print(max_difference([2, 3, 8, 4, 6, 10, 1]))


# Find the Longest Consecutive Sequence
def longest_consecutive(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    prev = arr[0]
    count = 1
    max_count = 1
    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        if arr[i] == prev + 1:
            count += 1
        else:
            if count > max_count:
                count = max_count
            count = 1
        perv = arr[i]
        if count > max_count:
            count = max_count
        return max_count


print(longest_consecutive([100, 4, 200, 1, 3, 2]))


# Maximum Product of Two Elements in an Array
def max_product(arr):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return max(largest * second_largest, smallest * second_smallest)


print(max_product([-10, -20, 5, 4]))


# LeetCode 525 - Longest Subarray with Equal Number of 0s and 1s(Medium)
def findMaxLength(arr):
    maxLength = 0
    for i in range(len(arr)):
        zeros = 0
        ones = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                zeros += 1
            else:
                ones += 1
            if ones == zeros:
                currentLength = j - i + 1
                if currentLength > maxLength:
                    maxLength = currentLength
    return maxLength


print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))


# Longest Sub-array with Equal Sum of Two Halves
def longestEqualHalfSum(arr):
    max_Length = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_Length = j - i + 1
            if current_Length % 2 != 0:
                continue
            mid = i + current_Length // 2
            first_half_Sum = 0
            second_half_sum = 0
            for k in range(i, mid):
                first_half_Sum += arr[k]
            for l in range(mid, j + 1):
                second_half_sum += arr[l]
            if first_half_Sum == second_half_sum:
                if max_Length < current_Length:
                    max_Length = current_Length
    return max_Length


print(longestEqualHalfSum([1, 5, 2, 8, 3, 7, 4]))


# Longest Substring with Exactly K Unique Characters
def longest_substring(s, k):
    maxLength = 0
    for i in range(len(s)):
        currentString = ""
        uniqueCount = 0
        for j in range(i, len(s)):
            ch = s[j]
            alreadyExists = False
            for x in range(len(currentString)):
                if currentString[x] == ch:
                    alreadyExists = True
                    break
            if alreadyExists:
                currentString = currentString + ch
            else:
                if uniqueCount < k:
                    uniqueCount += 1
                    currentString = currentString + ch
                else:
                    break
            if uniqueCount == k:
                if maxLength < len(currentString):
                    maxLength = len(currentString)
    return maxLength


print(longest_substring("aabacbebebe", 3))


# Chocolate Distribution Problem
def chocolate_distribution(arr, m):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    min_diff = float("inf")
    for i in range(len(arr) - m + 1):
        difference = arr[i + m - 1] - arr[i]
        if difference < min_diff:
            min_diff = difference
    return min_diff


print(chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 3))


# Remove Duplicates from Array
def remove_duplicates(arr):
    result = []
    for i in range(len(arr)):
        flag = False
        for j in range(len(result)):
            if arr[i] == result[j]:
                flag = True
                break
        if not flag:
            result.append(arr[i])
    return result


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# Write Fibonacci Series
def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


print(fibonacci(10))


# Find Second Largest Element in Array
def second_Largest(s):
    largest = 0
    second_Largest = 0
    for i in range(len(s)):
        if s[i] > largest:
            second_Largest = largest
            largest = s[i]
        else:
            if s[i] > second_Largest:
                second_Largest = s[i]
    return second_Largest


print(second_Largest([10, 16, 20, 8, 15]))


# Sort Array by Parity(Even first, then Odd)
def sort_By_Parity(s):
    even = []
    odd = []
    for i in range(len(s)):
        if s[i] % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    return even + odd


print(sort_By_Parity([3, 1, 2, 4]))


# Find First Non-Repeating Element
def first_non_repeating(arr):
    map = {}
    for num in range(len(arr)):
        map[num] = map.get(num, 0) + 1
    for num in arr:
        if map[num] == 1:
            return num
    return None


print(first_non_repeating([4, 5, 1, 2, 0, 4, 1, 0]))


# Find Pair with Given Sum
def two_sum(s, target):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == target:
                return [s[i], s[j]]
    return []


print(two_sum([2, 7, 11, 15], 13))


# Maximum Product of Three Elements
def max_product_of_three(s):
    max1 = float("-inf")
    max2 = float("-inf")
    max3 = float("-inf")
    min1 = float("inf")
    min2 = float("inf")
    for i in range(len(s)):
        n = s[i]
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n
        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n
    product1 = max1 * max2 * max3
    product2 = min1 * min2 * max1
    if product1 > product2:
        return product1
    else:
        return product2


print(max_product_of_three([-10, -10, 1, 2, 3]))


# Find the Maximum Subarray Sum (Kadane’s Algorithm)
def maxSubArray(arr):
    currentSum = 0
    maxSum = 0
    for num in arr:
        total = currentSum + num
        if total < 0:
            currentSum = 0
        else:
            currentSum = total
        maxSum = max(maxSum, currentSum)
    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 3, 1, -5, 4]))


# Group Anagrams
def groupAnagrams(strs):
    map = {}
    for string in strs:
        key = "".join(sorted(string))
        if key not in map:
            map[key] = []
        map[key].append(string)
    return list(map.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# Find the Maximum Consecutive 1's in an Array
def maxConsecutiveOnes(s):
    count = 0
    maxCount = 0
    for i in s:
        if i == 1:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 0
    return maxCount


print(maxConsecutiveOnes([1, 1, 0, 1, 1, 1]))


# Find the First Recurring Character
def first_recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)


print(first_recurring_char("abbcc"))


# without inbuilt
def first_recurring_char(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return s[j]


print(first_recurring_char("abbcc"))


# Separate Numbers and Strings in an Array
def separate(val):
    string = []
    numbers = []
    for i in val:
        if isinstance(i, str):
            string.append(i)
        else:
            numbers.append(i)
    return [string] + [numbers]


print(separate([10, "a", "b", "c", 11, 4]))


# Longest Substring with At Most K Distinct Characters
def longestSubstringKDistinct(s, k):
    left = 0
    maxLength = 0
    count = {}
    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        maxLength = max(maxLength, right - left + 1)
    return maxLength


print(longestSubstringKDistinct("eceba", 2))


# isPrime
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(isPrime(5))


# Binary Search: search for a target value in a sorted array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 30))


# Leetcode 121- best time to buy and sell stock
def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    i = 1
    while i < len(prices):
        if prices[i] < min_price:
            min_price = prices[i]

        profit = prices[i] - min_price

        if profit > max_profit:
            max_profit = profit

        i += 1

    return max_profit


# Tech Number
digits = 0


def count_digits(n):
    global digits
    temp = n
    while temp > 0:
        digits += 1
        temp = temp // 10


def is_tech_num(n):
    count_digits(n)
    half_length = digits / 2
    if digits % 2 != 0:
        print("Not a techNumber!")
        return
    divisor = 1
    for i in range(int(half_length)):
        divisor = divisor * 10
    first_half = n // divisor
    second_half = n % divisor
    sum_and_square_of_half = (first_half + second_half) ** 2
    if sum_and_square_of_half == n:
        print("Is techNumber!")
    else:
        print("Not a techNumber!")


is_tech_num(2025)


# Sort Array Elements
def sort_array(s):
    for i in range(len(s)):
        for j in range(len(s) - 1):
            if s[j] > s[j + 1]:
                temp = s[j]
                s[j] = s[j + 1]
                s[j + 1] = temp
    return s


print(sort_array([5, 2, 8, 1, 4]))


# LeetCode 643 — Maximum Average Subarray I
def maximum_average_subarray_i(arr, k):
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


print(maximum_average_subarray_i([1, 12, -5, -6, 50, 3], 4))


# LeetCode 125 — Valid Palindrome
def is_palindrome(s):
    new_str = ""
    for i in range(len(s)):
        ascii_value = ord(s[i])
        if 65 <= ascii_value <= 90:
            ascii_value = ascii_value + 32
        if 97 <= ascii_value <= 122 or 48 <= ascii_value <= 57:
            new_str = new_str + chr(ascii_value)
    left = 0
    right = len(new_str) - 1
    while left < right:
        if new_str[left] != new_str[right]:
            return False
        left = left + 1
        right = right - 1
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
