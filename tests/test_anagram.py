from betbright.anagram import find_anagrams


def test_find_anagrams_returns_list_with_valid_anagrams():
    word = '123'
    valid_anagrams = [
        '123',
        '321',
        '213',
        '132',
        ' 3 2 1 ',
    ]
    invalid_anagrams = [
        '1123',
        '1233',
        '4567',
        'asdf980',
    ]
    anagrams = valid_anagrams + invalid_anagrams
    observed = find_anagrams(word, anagrams)
    assert observed == valid_anagrams
