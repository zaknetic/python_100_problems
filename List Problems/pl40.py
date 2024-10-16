#Given two lists of integers, write a Python
#  program to create a new list that contains 
# elements common to both lists.

def get_common_items(group1, group2):
    # Use list comprehension to find common items
    common_items = [item for item in group1 if item in group2]
    
    # Use set to remove duplicates, if any
    return list(set(common_items))

# Example usage
group1 = [1, 2, 3, 4, 5]
group2 = [4, 5, 6, 7, 8]

common = get_common_items(group1, group2)
print("Common items:", common)
