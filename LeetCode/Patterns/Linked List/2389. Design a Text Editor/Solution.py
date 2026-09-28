class TextEditor:

    def __init__(self):
        self.left = []   # Characters to the left of the cursor
        self.right = []  # Characters to the right of the cursor (stored in reverse order of appearance)

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        deleted_count = 0
        while self.left and k > 0:
            self.left.pop()
            k -= 1
            deleted_count += 1
        return deleted_count

    def cursorLeft(self, k: int) -> str:
        while self.left and k > 0:
            self.right.append(self.left.pop())
            k -= 1
        return self._get_left_string()

    def cursorRight(self, k: int) -> str:
        while self.right and k > 0:
            self.left.append(self.right.pop())
            k -= 1
        return self._get_left_string()

    def _get_left_string(self) -> str:
        # Returns the last min(10, len) characters to the left of the cursor
        start = max(0, len(self.left) - 10)
        return "".join(self.left[start:])