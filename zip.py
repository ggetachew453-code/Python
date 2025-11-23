class zip_sequences:
    """
    Iterator that zips multiple sequences together, yielding tuples
    containing elements from each sequence at the same position.
    
    Args:
        *sequences: Variable number of sequences to zip together
    """
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0
        # Find minimum length to stop at shortest sequence
        self.min_length = min(len(seq) for seq in sequences) if sequences else 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.min_length:
            result = tuple(seq[self.index] for seq in self.sequences)
            self.index += 1
            return result
        raise StopIteration

# Example usage
print("Zip Sequences:")
for item in zip_sequences([1, 2], [3, 4], [5, 6]):
    print(item, end=" ")
print()  # Output: (1, 3, 5) (2, 4, 6)