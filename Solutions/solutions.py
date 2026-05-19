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
