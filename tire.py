from tire_class import Tire
from car import Car
tire = Tire('P', 205, 55, 15)
tires = [tire, tire, tire, tire]
BMW = Car(tires=tires, engine='6-cylinder')
BMW.description
