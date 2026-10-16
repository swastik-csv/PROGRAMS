class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        def backtrack(index: int, path: list[str]) -> None:
            if index == len(digits):
                combinations.append("".join(path))
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return combinations