class Solution:
  def checkIfPangram(self, sentence):
    # TODO: Write your code here
    alphabet=set("abcdefghijklmnopqrstuvwxyz")
    alpha=set()
    sentence=sentence.lower()
    for char in sentence:
      if char in alphabet:
        alpha.add(char)
    print(alpha)
    print(len(alpha))

    if len(alpha)==26:
      return True

    return False



# Test cases
sol = Solution()
# Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
# Expected output: True
print(sol.checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

# Test case 2: "This is not a pangram"
# Expected output: False
print(sol.checkIfPangram("This is not a pangram"))

# Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
# Expected output: True
print(sol.checkIfPangram("abcdef ghijkl mnopqr stuvwxyz"))

# Test case 4: ""
# Expected output: False
print(sol.checkIfPangram(""))

# Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Expected output: True
print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
