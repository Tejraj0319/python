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
    stack=[]
    for element in str:
        if element == "(" or element == "{" or element == "[":
            stack.append(element)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if((element == ")" and last != "(") or
            (element == "}" and last != "{") or
            (element == "]" and last != "[")):
              return False
    return len(stack)==0
print(isValid("({[]})"))


# String Compression
def stringCompression(s):
    count = 1
    new_str = ""
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            new_str += s[i-1] + str(count)
            count = 1
    return new_str if len(new_str) < len(s) else s
print(stringCompression("aabcccccaaa"))


# Custom Reduce Function Implementation
def my_function(arr, callback, intial_value):
  accumulator = intial_value;
  for i in range(len(arr)):
    accumulator = callback(accumulator, arr[i])
  return accumulator
num = [1,2,3,4]
result = my_function(num, lambda acc, curr: acc + curr, 0)
print("num:",result)


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
  for i in range(1, n+1):
    xor ^= i 
  for num in arr:
    xor ^= num
  return xor
print(find_missing([1, 2, 3, 5], 5))


# Find Duplicate Elements in an Array
def find_duplicates(arr):
  freq_map={}
  duplicates = []
  for num in arr:
    freq_map[num] = freq_map.get(num, 0) + 1
  for key, value in freq_map.items():
    if value > 1:
      duplicates.append(key)
  return duplicates
print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))