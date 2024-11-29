# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the word in lowercase for case-insensitive matching
        self.word = word.lower()
        # Store the sorted version of the word for comparison
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        # Create a list to store matching anagrams
        matches = []
        for word in word_list:
            # Compare sorted versions of the words
            if sorted(word.lower()) == self.sorted_word:
                matches.append(word)
        return matches

