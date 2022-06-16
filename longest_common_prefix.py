"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        result_str = ""
        letters_list = []
        index = 0
        smallest_item = min(strs, key=len)
        while index < len(smallest_item):
            for item in strs:
                letters_list.append(item[index])
                
            if letters_list.count(letters_list[0]) == len(strs):
                result_str += letters_list[0]
            else:
                return result_str
            index += 1
            letters_list = []
        return result_str
 
 
 
