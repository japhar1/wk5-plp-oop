class Superhero:
    """A class representing a superhero with unique powers and abilities."""
    
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        """
        Initialize a superhero with unique attributes.
        
        Args:
            name (str): The superhero's public name
            secret_identity (str): The superhero's secret identity
            powers (list): List of superpowers
            weakness (str): The superhero's primary weakness
            energy_level (int): Current energy level (0-100)
        """
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.weakness = weakness
        self.energy_level = energy_level
        self.is_transformed = False
    
    def use_power(self, power_index):
        """Use a specific power if the hero has enough energy."""
        if self.energy_level <= 10:
            print(f"{self.name} is too exhausted to use powers!")
            return False
        
        if power_index < len(self.powers):
            power = self.powers[power_index]
            self.energy_level -= 15
            print(f"{self.name} uses {power}! Energy level: {self.energy_level}")
            return True
        else:
            print(f"{self.name} doesn't have that power!")
            return False
    
    def rest(self):
        """Rest to regain energy."""
        if self.energy_level < 100:
            self.energy_level = min(100, self.energy_level + 30)
            print(f"{self.name} rests. Energy level: {self.energy_level}")
        else:
            print(f"{self.name} is already fully rested!")
    
    def reveal_identity(self):
        """Reveal the superhero's secret identity."""
        print(f"{self.name}'s secret identity is {self.secret_identity}!")
    
    def __str__(self):
        """String representation of the superhero."""
        return (f"Superhero: {self.name}\n"
                f"Powers: {', '.join(self.powers)}\n"
                f"Weakness: {self.weakness}\n"
                f"Energy: {self.energy_level}%")
    
#Inheritance Layer: EnhancedSuperhero
class EnhancedSuperhero(Superhero):
    """A superhero with enhanced abilities and transformation capability."""
    
    def __init__(self, name, secret_identity, powers, weakness, enhanced_powers, energy_level=100):
        """
        Initialize an enhanced superhero.
        
        Args:
            enhanced_powers (list): Additional powers available when transformed
        """
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.enhanced_powers = enhanced_powers
    
    def transform(self):
        """Transform to access enhanced powers."""
        if self.energy_level >= 40 and not self.is_transformed:
            self.is_transformed = True
            self.energy_level -= 40
            print(f"{self.name} transforms! Enhanced powers activated!")
            return True
        elif self.is_transformed:
            print(f"{self.name} is already transformed!")
            return False
        else:
            print(f"{self.name} doesn't have enough energy to transform!")
            return False
    
    def revert(self):
        """Revert back to normal form."""
        if self.is_transformed:
            self.is_transformed = False
            print(f"{self.name} reverts to normal form.")
            return True
        else:
            print(f"{self.name} is not transformed!")
            return False
    
    def use_power(self, power_index):
        """Override use_power to include enhanced powers when transformed."""
        if self.is_transformed and power_index < len(self.enhanced_powers):
            power = self.enhanced_powers[power_index]
            self.energy_level -= 20
            print(f"{self.name} uses enhanced {power}! Energy level: {self.energy_level}")
            return True
        else:
            return super().use_power(power_index)
    
    def __str__(self):
        """Enhanced string representation."""
        base_info = super().__str__()
        if self.is_transformed:
            return base_info + "\nStatus: TRANSFORMED"
        return base_info
    
#Activity 2: Polymorphism Challenge!
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """How the animal moves."""
        raise NotImplementedError("Subclasses must implement move()")
    
    def speak(self):
        """Sound the animal makes."""
        raise NotImplementedError("Subclasses must implement speak()")

class Bird(Animal):
    """A bird that can fly."""
    
    def move(self):
        print(f"{self.name} is flying through the air!")
    
    def speak(self):
        print(f"{self.name} says: Tweet tweet!")

class Fish(Animal):
    """A fish that can swim."""
    
    def move(self):
        print(f"{self.name} is swimming in the water!")
    
    def speak(self):
        print(f"{self.name} says: Glub glub!")

class Cheetah(Animal):
    """A cheetah that can run very fast."""
    
    def move(self):
        print(f"{self.name} is running at incredible speed!")
    
    def speak(self):
        print(f"{self.name} says: Growl!")

# Demonstration of polymorphism
def demonstrate_movement(animals):
    """Demonstrate how different animals move differently."""
    print("\n=== Animal Movement Demonstration ===")
    for animal in animals:
        animal.move()
        animal.speak()
        print()

# Vehicle classes with polymorphism
class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
    
    def move(self):
        """How the vehicle moves."""
        raise NotImplementedError("Subclasses must implement move()")
    
    def describe(self):
        """Describe the vehicle."""
        raise NotImplementedError("Subclasses must implement describe()")

class Car(Vehicle):
    """A car that drives on roads."""
    
    def move(self):
        print(f"{self.model} is driving at {self.speed} mph!")
    
    def describe(self):
        print(f"{self.model} is a car with {self.speed} mph top speed.")

class Airplane(Vehicle):
    """An airplane that flies."""
    
    def move(self):
        print(f"{self.model} is flying at {self.speed} mph!")
    
    def describe(self):
        print(f"{self.model} is an airplane with {self.speed} mph cruising speed.")

class Boat(Vehicle):
    """A boat that sails on water."""
    
    def move(self):
        print(f"{self.model} is sailing at {self.speed} knots!")
    
    def describe(self):
        print(f"{self.model} is a boat with {self.speed} knots top speed.")

def demonstrate_vehicle_movement(vehicles):
    """Demonstrate how different vehicles move differently."""
    print("\n=== Vehicle Movement Demonstration ===")
    for vehicle in vehicles:
        vehicle.move()
        vehicle.describe()
        print()

# Main execution
if __name__ == "__main__":
    print("=== Superhero Demonstration ===")
    # Create a regular superhero
    superman = Superhero(
        "Superman", 
        "Clark Kent", 
        ["Super strength", "Heat vision", "Flight"], 
        "Kryptonite"
    )
    print(superman)
    superman.use_power(0)
    superman.use_power(1)
    print()
    
    # Create an enhanced superhero
    wonder_woman = EnhancedSuperhero(
        "Wonder Woman",
        "Diana Prince",
        ["Super strength", "Lasso of Truth"],
        "Being bound by a man",
        ["God mode", "Aegis shield"],
        90
    )
    print(wonder_woman)
    wonder_woman.transform()
    wonder_woman.use_power(0)  # Use enhanced power
    print(wonder_woman)
    print()
    
    # Demonstrate animal polymorphism
    animals = [
        Bird("Robin"),
        Fish("Goldfish"),
        Cheetah("Chester")
    ]
    demonstrate_movement(animals)
    
    # Demonstrate vehicle polymorphism
    vehicles = [
        Car("Toyota Camry", 120),
        Airplane("Boeing 747", 570),
        Boat("Sailboat", 25)
    ]
    demonstrate_vehicle_movement(vehicles)