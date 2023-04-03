class Tire:
    """
    Tire represents a tire that would be used with an automobile
    """
    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diamter = diameter
        self.construction = construction

    def __repr__(self):
        """
        Represent the tire's information in the standard notation present on the side of the tire.
        Example: 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}{self.construction}{self.diamter}")


