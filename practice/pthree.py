# Problem 3

def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    txt_list = list(s)
    se = []
    maximum = 0
    while i < len(txt_list):
        if txt_list[i] not in se:
            se.append(txt_list[i])
            i = i + 1
            if maximum<len(se):
                maximum = len(se)
        else:
            del se[0]
    return maximum


def twoSum(nums, target):
    dic = {}
    for i, j in enumerate(nums):
        if target - j not in dic:
            dic[j] = i
        else:
            return [i, dic[target - j]]


print(twoSum([0,3,5,10,11], 8))