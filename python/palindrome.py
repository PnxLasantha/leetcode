"""https://leetcode.com/problems/palindrome-number/solutions/?languageTags=python3"""
def isPalindrome( x: int) -> bool:
   print("The original number : " + str(x))
   stringNum  = [str(i) for i in str(x)]
   str_length = stringNum.__len__()
  
   for i in range(int(str_length/2)):
        
        if(stringNum[i] != stringNum[str_length-i-1]):
            return False

   return True

"""Better answer """
num = 1661
val : bool = True  if str(num) == str(num)[::-1] else False