def find_additives(array, target_sum):
    mySet = set(array)
    for num in mySet:
        looking_for_num = target_sum - num
        if looking_for_num != num and looking_for_num in mySet:
            return [num, looking_for_num]
    return []


# Best time: O(n); Space: O(n) - check!

# Write a fun8ction that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
# Note that the target sum has to be obtained by summing two different integers
# in the array; You can't add a single integer to itself in order to obtain the
# target sum.
# You can assume that there will be at most one pair of numbers summing up to
# the target sum.

tests = [([3, 5, -4, 8, 11, 1, -1, 6], 10, ([-1, 11], [11, -1]))]

for num, test in enumerate(tests):
    array, target_sum, expected = test
    res = find_additives(array, target_sum)
    status = "SUCCESS" if res in expected else "FAILED"
    print(f"{num}) {array}, {target_sum} -> {expected}, GOT: {res} ({status})")
