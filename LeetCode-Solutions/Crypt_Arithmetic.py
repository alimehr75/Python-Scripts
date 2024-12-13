from itertools import permutations, chain
import re


def solve(equation):
    """
    solve(['SEND', 'MORE'], 'MONEY')
    SEND(9567) + MORE(1085) = MONEY(10652)

    """

    digits = "0123456789"
    # Finding words in given string

    result = re.findall(r'(\b[A-Z]+\b)', equation)
    initial_letters = ''.join(set(chain(r[0] for r in result)))
    letters = "".join(set(chain(*result)))

    def decipher(string: str, table):
        """
        convert given string to integer
        """
        return string.translate(table)

    for perm in permutations(digits, len(letters)):
        # generate a translate table per each permutation
        table = str.maketrans(letters, ''.join(perm))
        # Leading Zeroes "0" not allowed
        if "0" in decipher(initial_letters, table):
            continue

        deciphered_sum = sum(int(i) for i in map(
            lambda x: decipher(x, table), result[0:-1]))

        if deciphered_sum == int(decipher(result[-1], table)):
            print(f"{equation} is okay")
            break
    else:
        print(f"{equation} is Not okay")


solve("'ODD' + 'ODD' = 'EVEN'")
solve("'SEND' + 'MORE' ='MONEY'")
solve("'BASE' + 'BALL' ='GAMESS'")
solve("'CRACK' + 'HACK' ='ERRORR'")
