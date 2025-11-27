class zip_sequences:
    
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0
       
        self.min_length = min(len(seq) for seq in sequences) if sequences else 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.min_length:
            result = tuple(seq[self.index] for seq in self.sequences)
            self.index += 1
            return result
        raise StopIteration


print("Zip Sequences:")
for item in zip_sequences([1, 2], [3, 4], [5, 6]):
    print(item, end=" ")
print()  
