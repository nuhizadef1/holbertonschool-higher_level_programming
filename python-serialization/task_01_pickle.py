#!/usr/bin/env python3
import pickle


class CustomObject:
    """This task is bad"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized to {filename}")
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes the object from a file and returns an instance."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
            return True 

        except FileNotFoundError:
            return False 
        except Exception:
            return None


if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    if new_obj:
        print("\nDeserialized Object:")
        new_obj.display()
