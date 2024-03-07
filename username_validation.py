"""
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
"""

def CodelandUsernameValidation(strParam):
  if len(strParam) < 4 or len(strParam) > 25:
    return False
  
  if not strParam[0].isalpha():
    return False

  if strParam.endswith("_"):
    return False
  
  for _element in strParam:
    if _element.isalpha() or _element.isdigit() or _element == "_":
      continue
    else:
      return False

  return True

def main():
    inputs = [
        "aa_",
        "u__hello_world123",
    ]
    for _input in inputs:
        print(CodelandUsernameValidation(_input))

if __name__== '__main__':
    main()
