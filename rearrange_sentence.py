"""
1451. Rearrange Words in a Sentence
Given a sentence text (A sentence is a string of space-separated words) in the following format:

- First letter is in upper case.
- Each word in text are separated by a single space.
- Always end with a period

Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.


Example 1:

Input: text = "Leetcode is cool."
Output: "Is cool leetcode."

Example 2:
Input: text = "Keep calm and code on."
Output: "On and keep calm code."

Example 3:
Input: text = "To be or not to be."
Output: "To be or to be not."
 

Constraints:

text begins with a capital letter and then contains lowercase letters and single space between words and ends with a period.
1 <= text.length <= 10^5

"""

def arrange(sentence):
    sentence = sentence.lower()[:-1].split(" ")
    sorted_words = sorted(sentence, key=len)
    rearrange_sentence = " ".join(sorted_words) + "."
    
    return rearrange_sentence.capitalize()

def main():
    sentences = []
    sentences.append("The lines are in reversed order.")
    sentences.append("Cats and hats.")
    sentences.append("There are many ways of performing this.")
    sentences.append("Leetcode is cool.")
    sentences.append("Keep calm and code on.")
    sentences.append("To be or not to be.")

    for sentence in sentences:
        print(arrange(sentence))

if __name__== '__main__':
    main()
