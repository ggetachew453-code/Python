def generate_combinations(sequence, k):
    """
    Generator that yields all combinations of length k from the input sequence.
    
    Args:
        sequence: Input sequence (list, tuple, etc.)
        k: Length of each combination
    
    Yields:
        Tuples representing combinations of length k
    """
    def _combine(start, current_comb):
        # Base case: combination of desired length found
        if len(current_comb) == k:
            yield tuple(current_comb)
            return
        
        # Recursive case: build combination
        for i in range(start, len(sequence)):
            current_comb.append(sequence[i])
            yield from _combine(i + 1, current_comb)
            current_comb.pop()  # Backtrack
    
    yield from _combine(0, [])

# Example usage
print("Combinations:")
for comb in generate_combinations([1, 2, 3], 2):
    print(comb, end=" ")
print()  # Output: (1, 2) (1, 3) (2, 3)