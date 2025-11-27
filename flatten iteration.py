class flatten_iterate:
    
    def __init__(self, nested_structure):
        self.stack = [iter([nested_structure])]
        self.current_iter = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.stack:
            if self.current_iter is None:
                self.current_iter = self.stack[-1]
            
            try:
                element = next(self.current_iter)
                
                
                if isinstance(element, list):
                    self.stack.append(iter(element))
                    self.current_iter = None
                else:
                    return element
                    
            except StopIteration:
                
                self.stack.pop()
                self.current_iter = None
        
        raise StopIteration


print("Flatten Iterator:")
for item in flatten_iterate([1, 2, [3, [4], 5]]):
    print(item, end=" ")
print()  # Output: 1 2 3 4 5
