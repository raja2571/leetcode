class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_ = False
        col_ = False

        # Check first column
        for i in range(rows):

            if matrix[i][0] == 0:
                col_ = True

        # Check first row
        for j in range(cols):

            if matrix[0][j] == 0:
                row_ = True

        # Mark rows and columns
        for i in range(1, rows):

            for j in range(1, cols):

                if matrix[i][j] == 0:

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Fill zeros
        for i in range(1, rows):

            for j in range(1, cols):

                if matrix[0][j] == 0 or matrix[i][0] == 0:

                    matrix[i][j] = 0

        # Set first row zero
        if row_:

            for j in range(cols):

                matrix[0][j] = 0

        # Set first column zero
        if col_:

            for i in range(rows):

                matrix[i][0] = 0