class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, max_len = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of valid palindrome: (right - 1) - (left + 1) + 1
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand_around_center(i, i)
            len_even = expand_around_center(i, i + 1)
            curr_max = max(len_odd, len_even)

            if curr_max > max_len:
                max_len = curr_max
                # Derive start index from the center and length
                start = i - (curr_max - 1) // 2

        return s[start:start + max_len]