'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # check if less than two characters
    if len(word) < 2:
        # return 0 since impossible
        # also stops the recurive cycle
        return 0
    # check if first two characters are 'th'
    if word[:2] == 'th':
        # if so, return one
        # and iterate through next two characters
        # by a recursive call
        return 1 + count_th(word[1:])
    else:
        # if its not 'th' then continue to next set
        # also by removing the first character
        return count_th(word[1:])


print(count_th("threethreethree"))
