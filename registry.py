from shapes import Shape


class ShapeRegistry:
    
    def __init__(self):
        self._prototypes = {}
        
    def register(self, k:str, p:Shape):
        self._prototypes[k] = p
        
    def create(self,k:str):
        try:
            prototype = self._prototypes[k]
            return prototype.clone()
        except KeyError:
            raise KeyError(f"Shape '{k}' is not registered in the registry.")
