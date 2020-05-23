def move_to_end(array, to_move):
    end_idx = len(array) - 1
    curr_idx = 0
    while end_idx > curr_idx:
        if array[curr_idx] == to_move:
            while array[end_idx] == to_move and end_idx > curr_idx:
                end_idx -= 1
            array[curr_idx], array[end_idx] = array[end_idx], array[curr_idx]
            end_idx -= 1
        curr_idx += 1
    return array


# You're given an array of integers and an integer. Write a function that moves
# all instances of that integer in the array to the end of the array and
# returns the array.
# The function should perform this in place (i.e, it should mutate the input
# array) and doesn't need to maintain the order of the other integers)

tests = [([2, 1, 2, 2, 2, 3, 4, 2], 2, [1, 3, 4, 2, 2, 2, 2, 2])]

for num, test in enumerate(tests):
    array, to_move, expected = test
    array_one = array[:]
    res = move_to_end(array, to_move)
    status = "SUCCESS" if res == expected else "FAILED"
    print(
        f"{num}) {array_one}, {to_move} -> {expected}, GOT: {res} ({status})")

# Optimal time O(n), optimal space O(1)
