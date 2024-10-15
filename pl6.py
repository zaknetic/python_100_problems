#Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

#method 1
def get_data_type(variable):
    # Dictionary to map types to their names
    type_mapping = {
        int: "int",
        float: "float",
        str: "str",
        list: "list",
        tuple: "tuple",
        dict: "dict",
        bool: "bool",
        set: "set",
        type(None): "NoneType"  # For None
    }
    
    # Get the type of the variable and return the corresponding name
    return type_mapping.get(type(variable), "unknown type")

# Example usage
print(get_data_type(10))              # Output: int
print(get_data_type(10.5))            # Output: float
print(get_data_type("Hello"))         # Output: str
print(get_data_type([1, 2, 3]))       # Output: list
print(get_data_type((1, 2, 3)))       # Output: tuple
print(get_data_type({"key": "value"})) # Output: dict
print(get_data_type(True))             # Output: bool
print(get_data_type(None))             # Output: NoneType
print(get_data_type({1, 2, 3}))       # Output: set
print(get_data_type(complex(1, 2)))    # Output: unknown type


#method 2 

def get_data_type(variable):
    # Return the name of the class of the variable as a string
    return variable.__class__.__name__

# Example usage
print(get_data_type(10))              # Output: int
print(get_data_type(10.5))            # Output: float
print(get_data_type("Hello"))         # Output: str
print(get_data_type([1, 2, 3]))       # Output: list
print(get_data_type((1, 2, 3)))       # Output: tuple
print(get_data_type({"key": "value"})) # Output: dict
print(get_data_type(True))             # Output: bool
