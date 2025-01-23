# Lab_Sofware-3.

Creational Design Patterns

Creational patterns focus on simplifying the object creation process. They abstract the instantiation process to make it more flexible and efficient. Here’s a brief explanation of each:

    Singleton Pattern:
        Purpose: Ensures that a class has only one instance and provides a global point of access to it.
        Use: It is used when you need to control access to shared resources, like a database connection or logging service, and ensure there is only one instance of a class throughout the application.

    Factory Method Pattern:
        Purpose: Defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created.
        Use: It is useful when you don’t know in advance what type of object you will need, and it enables you to delegate the object creation to subclasses. For example, in a game, the factory method can be used to create different types of characters (warrior, mage, etc.).

    Abstract Factory Pattern:
        Purpose: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
        Use: It is helpful when your code needs to work with different types of related objects (like UI components across different operating systems). The Abstract Factory ensures that all products are compatible with each other.

    Builder Pattern:
        Purpose: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
        Use: It is useful for constructing objects with many attributes that may not all be required at once. It enables you to create complex objects step-by-step (e.g., building a car, step by step, with different options).

    Prototype Pattern:
        Purpose: Specifies the kind of objects to create using a prototypical instance and creates new objects by copying this prototype.
        Use: It is beneficial when the creation of new objects is more expensive than copying an existing one (e.g., creating clones of a complex object with minimal changes).

Why We Use Creational Patterns:

    Flexibility: These patterns help decouple the object creation logic from the rest of the code, making it easier to change the way objects are created.
    Scalability: Creational patterns promote scalability and manageability in large systems by handling object creation in a centralized manner.
    Efficiency: They help optimize resource usage, like ensuring only one instance of a class or reusing existing objects instead of creating new ones.
