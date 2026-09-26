class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Step 1: Store elements in a hash set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        # Step 2: Check each unique number
        for num in num_set:
            # Check if this number is the START (Leader) of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Step 3: Count up along the chain
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak