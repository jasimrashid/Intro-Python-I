# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_data(self):
        print(f'{self.lat}, {self.lon}')

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name=name


    def get_data(self):
        print(f'"{self.name}", {self.lat}, {self.lon}')

# This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.

# This method must return the String object. If we don’t implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.
    def __str__(self):
        return f'"{self.name}", {self.lat}, {self.lon}'

# Python __repr__() function returns the object representation. It could be any valid python expression such as
    def __repr__(self):
        return {'name': self.name, 'lat':self.lat, 'lon':self.lon}

    # __repr__ = __str__

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty=difficulty
        self.size=size

    def __str__(self):
        return f'{self.lat}, {self.lon}, {self.name}, {self.difficulty}, {self.size}'
    
    def __repr__(self):
        return f'{self.lat}, {self.lon}, {self.name}, {self.difficulty}, {self.size}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(waypoint)

# breakpoint()
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(name="Newberry Views", difficulty=1.5, size=2, lat=44.052137, lon=-121.41556)

# Print it--also make this print more nicely

print(geocache)
