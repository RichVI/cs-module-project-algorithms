'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    # Create window with 0s
    window = []
    max_nums = [0] * k

    # Loop from left(0) to 
    for i in range(0, len(nums) - k + 1):
        max_nums = nums[i:i + k]
        window.append(max(max_nums))
    return window


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
