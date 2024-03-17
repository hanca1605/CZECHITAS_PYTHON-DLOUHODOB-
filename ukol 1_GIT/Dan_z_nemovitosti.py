class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient


class Property:
    def __init__(self, locality):
        self.locality = locality

from math import ceil

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == "land":
            coefficient = 0.85
        elif self.estate_type == "building site":
            coefficient = 9
        elif self.estate_type == "forest":
            coefficient = 0.35
        else:
            raise ValueError("Invalid estate type")

        tax = ceil(self.area * coefficient * self.locality.coefficient)
        return tax

class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        base_tax = self.area * self.locality.coefficient * 15
        if self.commercial:
            total_tax = base_tax * 2
        else:
            total_tax = base_tax
        return ceil(total_tax)

manetin_locality = Locality("Manětín", 0.8)
brno_locality = Locality("Brno", 3)

estate1 = Estate(manetin_locality, "land", 900)
residence1 = Residence(manetin_locality, 120)
residence2 = Residence(brno_locality, 90, commercial=True)


tax1 = estate1.calculate_tax()
tax2 = residence1.calculate_tax()
tax3 = residence2.calculate_tax()


print(f"Dan z pozemku: {tax1}")
print(f"Dan z bytu: {tax2}")
print(f"Dan z kanceláře: {tax3}")