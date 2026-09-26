class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            # Update the row in reverse to use values from the previous step
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row