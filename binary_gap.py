def binary_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))


print(binary_gap(32))
print(binary_gap(15))
print(binary_gap(9))
print(binary_gap(529))

# def binary_gap_2(N):
#     binary = format(N, 'b').strip('0').split('1')
#     print(max(binary))

# binary_gap_2(32)
# binary_gap_2(529)

# print(max(['00', '000', '0', '000']))qs

print(format(15, 'b'))
print(format(2147483649, 'b'))