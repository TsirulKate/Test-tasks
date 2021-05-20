# you have the list of symbols (example: a, b, c, c, a (it’s very primitive)).You should write function that
# returns the first repeating element from this list (in our example it’s “c”).

#Time: 12 minutes


def find_first_repeat(list):
    set_help = set()
    for elem in list:
        if elem in set_help:
            return elem
        else:
            set_help.add(elem)


list = list('asdsefnvijfvoosja')
result = find_first_repeat(list)
if result is not None:
    print("The first repeat in the list is:", result)
else:
    print("There is no repeat in the list")
