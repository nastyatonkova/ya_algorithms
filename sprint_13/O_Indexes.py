"""
Gosha had traveled a long time and measured the area of each of the n islands of the Algos, 
but that wasn't enough for him! Now he wanted to estimate how diverse are the islands within the archipelago.

To do that, Gosha looked at all the pairs of islands (such pairs, let's remind you, 
are n * (n-1) / 2) and counted pairwise the difference of areas between all the islands. 
Now he's going to order the resulting differences to take the k-th of them in order.

Help Gosha find the k-th minimum difference between the areas effectively.

Explanations of the examples

Example 1

Write out all pairs of areas and find the corresponding differences

    |2 - 3| = 1
    |3 - 4| = 1
    |2 - 4| = 2

Since we need the 2nd largest difference, the answer is 1.

Example 2.

We have two identical elements in the array -- two units, so the minimum (first) difference is zero.   
"""


def check_index(array, middle, k_position, s_len):
    left = count = 0
    for right in range(s_len):
        val_right = array[right]
        val_left = array[left]
        while val_right - val_left > middle:
            left += 1
            val_left = array[left]
        count += right - left
        if count >= k_position:
            return True
    return False


def diff(s_len, s, k_position):
    s.sort()
    left, right = 0, s[-1] - s[0]
    while left < right:
        middle = (left + right) // 2
        if check_index(s, middle, k_position, s_len):
            right = middle
        else:
            left = middle + 1
    return left


print(diff(int(input()), list(map(int, input().split())), int(input())))
