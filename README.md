# wk5-plp-oop
Python Object-Oriented Programming Assignment

This project demonstrates key Object-Oriented Programming concepts in Python:

    Class design with attributes and methods

    Constructors for object initialization

    Inheritance and method overriding

    Polymorphism through interface implementation

Files

    main.py: Contains all class definitions and demonstration code

Classes Implemented
Superhero Classes

    Superhero: Base class representing a superhero with:

        Attributes: name, secret identity, powers, weakness, energy level

        Methods: use_power(), rest(), reveal_identity()

    EnhancedSuperhero: Inherits from Superhero and adds:

        Enhanced powers available when transformed

        Transformation capability

        Overridden use_power() method to handle enhanced powers

Polymorphism Examples

    Animal classes demonstrating polymorphism through the move() method:

        Bird: Moves by flying

        Fish: Moves by swimming

        Cheetah: Moves by running

    Vehicle classes demonstrating polymorphism through the move() method:

        Car: Moves by driving

        Airplane: Moves by flying

        Boat: Moves by sailing

How to Run

Execute the script with Python 3:

python main.py

The program will demonstrate:

    Superhero creation and power usage

    Enhanced superhero transformation

    Polymorphic behavior of animals

    Polymorphic behavior of vehicles

Key OOP Concepts Demonstrated

    Encapsulation: Attributes are encapsulated within classes

    Inheritance: EnhancedSuperhero inherits from Superhero

    Polymorphism: Different implementations of move() method across classes

    Abstraction: Base classes define interface that subclasses implement

This assignment showcases how to design classes with unique characteristics while maintaining a consistent interface through polymorphism.
