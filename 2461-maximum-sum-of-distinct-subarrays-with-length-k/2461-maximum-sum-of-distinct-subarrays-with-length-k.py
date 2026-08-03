class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        window_sum = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            window_sum += nums[right]

            if right - left + 1 > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                if len(freq) == k:
                    ans = max(ans, window_sum)

        return ans                            