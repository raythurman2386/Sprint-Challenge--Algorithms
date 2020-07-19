'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    # if the length of the word is one,
    if len(word) <= 1:
        # return the count
        return count

    # Check the first two positions for th
    if word[0:2] == 'th':
        # if 'th' add to the count
        count += 1

    # recurse after the first index of the word
    # to ensure every two combinations are checked
    return count + count_th(word[1:])


print(count_th("thhtthht"))
print(count_th("THtHThth"))
