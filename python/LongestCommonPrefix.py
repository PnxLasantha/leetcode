"""https://leetcode.com/problems/longest-common-prefix/description/"""



import os
from typing import List

strs =  ["ab"]
def longestCommonPrefix( strs: List[str]) -> str:
    res = os.path.commonprefix(strs)
    return res




def longestCommonPrefixZip( strs: List[str]) -> str:
   commonPrefix = ""
   for chars in zip(*strs):
    if len(set(chars))==1:
        commonPrefix += chars[0]
    else:
        break

   return commonPrefix
print(longestCommonPrefixZip(strs))