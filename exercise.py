"""
Problem: Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example: Input : ["flower","flow","flight"]
         Output: "fl"
          
          Input: ["dog","racecar","car"]
          Output: ""
          Explanation: There is no common prefix among the input strings.

Data Structure: Array(list)

Algorithim: 
create a holder
loop over the array
  -  check if the substring of all elements starting at the front in the array is the same
  - add to holder 
  - return the holder

"""

def longest_prefix(lst):
  if len(lst) == 0: return ""
  
  new_str = ""
  
  for i in range(len(lst[0])):
    new_str += lst[0][i]
    if lst[i][i] == new_str[i]:
      new_str += lst[i][i]
    else:
      new_str[0: -1]
      return new_str
  
  return new_str

print(longest_prefix([""]))
print(longest_prefix(["flower","flow","flight"]))