import collections


def find_anagrams(word, anagrams):
    word_letters = collections.Counter(word.replace(' ', ''))
    return [anagram for anagram in anagrams
            if word_letters == collections.Counter(anagram.replace(' ', ''))]
