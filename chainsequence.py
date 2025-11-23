class chain_sequences:
    """
    Iterator that chains multiple sequences together, yielding elements
    from each sequence in order.
    
    Args:
        *sequences: Variable number of sequences to chain together
    """
    def __init__(self, *sequences):
        self.sequences = sequences
        self.seq_index = 0
        self.element_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.seq_index < len(self.sequences):
            current_seq = self.sequences[self.seq_index]
            
            if self.element_index < len(current_seq):
                element = current_seq[self.element_index]
                self.element_index += 1
                return element
            else:
                # Move to next sequence
                self.seq_index += 1
                self.element_index = 0
        
        raise StopIteration

# Example usage
print("Chain Sequences:")
for item in chain_sequences([1, 2, 3], [4], [5]):
    print(item, end=" ")
print()  # Output: 1 2 3 4 5