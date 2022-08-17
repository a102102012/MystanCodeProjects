"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print(f"Welcome to stanCode \" Anagram Generator\" (or -1 to quit)")
    s = input("Find anagrams for: ")
    # print(find_anagrams(s))
    dict = read_dictionary()

    if s == EXIT:
        print('')
    else:
        search_lst = find_anagrams(s)  # Possible input word combinations
        input_lst = []
        for input_word in search_lst:  # Compare each input word combination
            if input_word in dict[input_word[:3]]:  # Search in the prefix dict value list
                print('Searching...')
                print(f'Found: {input_word}')
                input_lst.append(input_word)
        print(f"{len(input_lst)} anagrams: {input_lst}")

    while True:
        if s == EXIT:
            break
        else:
            s = input("Find anagrams for: ")
            search_lst = find_anagrams(s)
            input_lst = []
            for input_word in search_lst:
                if input_word in dict[input_word[:3]]:
                    print('Searching...')
                    print(f'Found: {input_word}')
                    input_lst.append(input_word)
            print(f"{len(input_lst)} anagrams: {input_lst}")

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Create dictionary in dict by three prefix
    for example:
    'foo': ['food', 'foodless', 'foodlessness', 'foods'...]
    'giv': ['give', 'giveable', 'giveaway', 'giveaways', 'given'...]
    """
    dict = {}
    with open(FILE,'r') as words:
        for word in words:
            word = word[:-1]
            word_prefix = word[:3]
            if word_prefix not in dict:
                dict[word_prefix] = [word]
            else:
                dict[word_prefix].append(word)
        #print(dict)
        return dict


def find_anagrams(s):
    """
    :param s: string, input word
    :return: list['combinaion A', 'combination B',...]
    """
    anagram_lst = []
    return find_anagrams_helper(s, len(s), [], anagram_lst, [])


def find_anagrams_helper(s, len_s, current_s, anagram_lst, index):
    if len(current_s) == len_s:
        if ''.join(current_s) not in anagram_lst:
            if has_prefix(''.join(current_s)):
                #print(''.join(current_s))
                anagram_lst.append(''.join(current_s))
                #print(anagram_lst)
        return anagram_lst
    else:
        for i in range(len_s):
            if i not in index:  # avoid the chosen character
                # choose
                current_s.append(s[i])
                index.append(i)
                # explore
                find_anagrams_helper(s, len_s, current_s, anagram_lst, index)
                # un-choose
                index.pop()
                current_s.pop()
        return anagram_lst


def has_prefix(sub_s):
    """
    :param sub_s: string
    :return: boolean
    """
    if sub_s[:3] in read_dictionary():
        return True


if __name__ == '__main__':
    main()
