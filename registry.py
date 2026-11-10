from shapes import Shape


class ShapeRegistry:
    
    def __init__(self):
        self._prototypes = {}
        
    def register(self, k:str, p:Shape):
        self._prototypes[k] = p
        
    def create(self,k:str):
        prototype: Shape = self._prototypes[k]
        
        if not prototype:
            raise KeyError(f"Prototype with key '{k}' not found in registry.")
        
        return prototype.clone()
