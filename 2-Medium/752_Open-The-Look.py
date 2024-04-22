def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        if "0000" in deadends:
            return -1
        
        deadends = set(deadends)
        visited = set()
        queue = deque([('0000', 0)])
        
        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            if current in deadends or current in visited:
                continue
            
            visited.add(current)
            
            for i in range(4):
                for j in [-1, 1]:
                    next_digit = str((int(current[i]) + j) % 10)
                    new_lock = current[:i] + next_digit + current[i+1:]
                    if new_lock not in visited and new_lock not in deadends:
                        queue.append((new_lock, moves + 1))
        
        return -1
