class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here
    #vowels=['a','e','i','o','u','A','E','I','O','U']
    vowels=set('aeiouAEIOU')
    s_list=list(s)

    l=0
    r=len(s_list)-1

    while l<r:
      #ref
      if s_list[l] not in vowels:
        l+=1
      if s_list[r] not in vowels:
        r-=1
      if s_list[r] in vowels and s[l] in vowels:
        temp=s_list[r]
        s_list[r] = s_list[l]
        s_list[l]=temp
        l+=1
        r-=1

    s=''.join(s_list)
    return s

if __name__ == "__main__":
  solution = Solution()

  s1 = "hello"
  expected_output1 = "holle"
  actual_output1 = solution.reverseVowels(s1)
  print("Test Case 1: ", expected_output1 == actual_output1)

  s2 = "DesignGUrus"
  expected_output2 = "DusUgnGires"
  actual_output2 = solution.reverseVowels(s2)
  print("Test Case 2: ", expected_output2 == actual_output2)

  s3 = "AEIOU"
  expected_output3 = "UOIEA"
  actual_output3 = solution.reverseVowels(s3)
  print("Test Case 3: ", expected_output3 == actual_output3)

  s4 = "aA"
  expected_output4 = "Aa"
  actual_output4 = solution.reverseVowels(s4)
  print("Test Case 4: ", expected_output4 == actual_output4)

  s5 = ""
  expected_output5 = ""
  actual_output5 = solution.reverseVowels(s5)
  print("Test Case 5: ", expected_output5 == actual_output5)
