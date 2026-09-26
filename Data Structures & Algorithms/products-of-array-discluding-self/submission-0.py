class Solution:

  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    res = [1] * n

    # Step 1: Fill left products
    for i in range(1, n):
      left[i] = left[i - 1] * nums[i - 1]

    # Step 2: Fill right products
    for i in range(n - 2, -1, -1):
      right[i] = right[i + 1] * nums[i + 1]

    # Step 3: Combine them
    for i in range(n):
      res[i] = left[i] * right[i]

    return res