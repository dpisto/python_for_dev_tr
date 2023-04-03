class Car:
    """
    Car models w/ tires and an engine
    """
    
    def __init__(self, engine, tires):
        """
        Create variables
        """
        self.engine = engine
        self.tires = tires
        
    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires.")