start = 0x1F600
end = 0x1F64F
table_size = end - start + 1
shift = int(input())
phrase = list(input())

print('Result: "{0}"'.format("".join([chr((ord(char) + shift - start) % table_size + start) for char in phrase])))

