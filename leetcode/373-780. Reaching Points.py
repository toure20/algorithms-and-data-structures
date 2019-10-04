# 780. Reaching Points
import collections
class Solution:
    # brute force: MLE
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty: return False
        
        q = collections.deque([(sx, sy)])
        while q:
            cx, cy = q.popleft()
            if cx == tx and cy == ty: return True
            
            if cx+cy <= tx and cy <= ty:
                q.append((cx+cy, cy))
            if cx <= tx and cy+cx <= ty:
                q.append((cx, cy+cx))
        
        return False

