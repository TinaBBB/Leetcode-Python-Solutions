class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Initialization of the grid-related vars.
        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols -1) 

        # Corner case, obstacle budge guarantees shortest path.
        if k >= rows+cols-2:
            return rows+cols-2
        
        # Directional vars.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # queue variable, storing the amount of steps taken, row, column, and remaining obstacle credit.
        queue = collections.deque([(0, (0, 0, k))])
        # Seen listing the spots landed.
        seen = set([(0, 0, k)])

        while queue:
            # Get the current iter's spot
            steps, (row, col, remaining_credit) = queue.popleft()

            # Base case at the target spot
            if (row, col) == target:
                return steps
            
            # Expand along the current branch
            for direction in directions:
                row_new = row + direction[0]
                col_new = col + direction[1]
                
                # Check oob
                if 0<= row_new <= rows-1 and 0 <= col_new <= cols-1:
                    # Get the new statement
                    new_credit = remaining_credit - grid[row_new][col_new]
                    new_state = (row_new, col_new, new_credit)
                    
                    # Append the new spot
                    if new_credit >= 0 and new_state not in seen:
                        seen.add((new_state))

                        queue.append((steps+1, new_state))

        return -1 
                    
