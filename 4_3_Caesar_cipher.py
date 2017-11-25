def encrypt1(phrase, shift):
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    encrypted = []

    for char in list(phrase):
        encrypted.append(alphabet[(alphabet.index(char) + shift) % len(alphabet)])
    return "".join(encrypted)


def encrypt2(phrase, shift):
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    return "".join([alphabet[(alphabet.index(char) + shift) % len(alphabet)] for char in phrase])


_shift = int(input())
_phrase = input().strip()

print('Result: "{}"'.format(encrypt2(_phrase, _shift)))
print('Result: "{}"'.format(encrypt2(_phrase, _shift)))
