import time
from typing import Any, Iterator, Tuple

class AllUnique:
    """A class providing methods to check if all elements in a sequence are unique."""
    
    def __init__(self, limit: int = 5, slow: int = 3) -> None:
        """
        Initialize the AllUnique checker.
        
        Args:
            limit: Length threshold for choosing strategy
            slow: Delay in seconds for sleep
        """
        self.LIMIT = limit
        self.SLOW = slow
        self.WARNING = 'too bad, you picked the slow algorithm :('

    def _pairs(self, seq: Any) -> Iterator[Tuple[Any, Any]]:
        """
        Generate pairs of adjacent elements from sequence.
        
        Args:
            seq: Input sequence
            
        Returns:
            Iterator of pairs of elements
        """
        n = len(seq)
        for i in range(n):
            yield seq[i], seq[(i + 1) % n]

    def _all_unique_sort(self, s: Any) -> bool:
        """
        Check uniqueness using sorting strategy.
        
        Args:
            s: Input sequence
            
        Returns:
            True if all elements are unique
        """
        if len(s) > self.LIMIT:
            print(self.WARNING)
            time.sleep(self.SLOW)
        srt_str = sorted(s)
        for (c1, c2) in self._pairs(srt_str):
            if c1 == c2:
                return False
        return True

    def _all_unique_set(self, s: Any) -> bool:
        """
        Check uniqueness using set strategy.
        
        Args:
            s: Input sequence
            
        Returns:
            True if all elements are unique
        """
        if len(s) < self.LIMIT:
            print(self.WARNING)
            time.sleep(self.SLOW)
        return True if len(set(s)) == len(s) else False

    def test(self, sequence: Any) -> bool:
        """
        Test if all elements in sequence are unique.
        
        Args:
            sequence: Input sequence to check
            
        Returns:
            True if all elements are unique
        """
        if len(sequence) < self.LIMIT:
            return self._all_unique_sort(sequence)
        return self._all_unique_set(sequence)


def main():
    """Run demo of AllUnique class usage."""
    checker = AllUnique()
    
    while True:
        word = input('Insert word (type quit to exit)> ')
        if word == 'quit':
            print('bye')
            break
            
        result = checker.test(word)
        print(f'allUnique({word}): {result}')


if __name__ == '__main__':
    main()