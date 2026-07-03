class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        cur_layer = 0
        
        res = []
        seen = set()
        while cur_layer < len(matrix):
            for c in range(cur_layer, COLS - cur_layer):
                r = cur_layer
                if (r,c) in seen:
                    break
                if (0 <= r < ROWS and 0 <= c < COLS):
                    res.append(matrix[r][c])
                seen.add((r,c))

            for r in range(cur_layer + 1, ROWS - 1 - cur_layer):
                c = COLS - 1 - cur_layer
                if (r,c) in seen:
                    break
                if (0 <= r < ROWS and 0 <= c < COLS):
                    res.append(matrix[r][c])
                seen.add((r,c))

            for c in range(COLS - 1 - cur_layer, -1 + cur_layer, -1):
                r = ROWS - 1 - cur_layer

                if (r,c) in seen:
                    break
                if (0 <= r < ROWS and 0 <= c < COLS):
                    res.append(matrix[r][c])
                seen.add((r,c))
            for r in range(ROWS - 1 - cur_layer - 1, -1 + cur_layer + 1, -1):
                c = cur_layer

                if (r,c) in seen:
                    break
                if (0 <= r < ROWS and 0 <= c < COLS):
                    res.append(matrix[r][c])
                seen.add((r,c))

            cur_layer += 1
        
        return res
                

            

        