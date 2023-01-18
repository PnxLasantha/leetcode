#https://leetcode.com/problems/counting-words-with-a-given-prefix/
from typing import List

words = ["leetcode","win","loops","success"]
pref = "at"
def prefixCount( words: List[str], pref: str) -> int:
    count = 0
    if(len(words) == 0):
        return count
    
    for word in words:
        if(word.startswith(pref)):
           count +=1
    return count


print(prefixCount(words,pref))