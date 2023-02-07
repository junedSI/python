def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def longest_collatz_sequence_under_n(n):
    longest_sequence = 0
    starting_number = 0
    for i in range(1, n):
        length = collatz_sequence_length(i)
        if length > longest_sequence:
            longest_sequence = length
            starting_number = i
    return starting_number


print("Starting number under one million that produces the longest chain:",
      longest_collatz_sequence_under_n(1000000))
