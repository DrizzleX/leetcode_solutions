from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        1. There are n numbers on the nth row
        2. first & last number of a row is always 1
        3. num[row][col] = num[row-1][col-1] + num[row-1][col] (2 <= row <= numRows-1)
        """
        result = []
        for row in range(numRows):
            current_row = []
            for col in range(row+1):  # Note: row+1
                if col == 0:  # first number of the current row
                    current_row.append(1)
                elif col == row:  # last number of the current row
                    current_row.append(1)
                else:
                    current_row.append(result[row-1][col-1] + result[row-1][col])
            result.append(current_row)
        return result

        