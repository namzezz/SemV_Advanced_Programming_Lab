import json

# JSON object (as a Python dictionary)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize the Python dictionary to a JSON string
json_str = json.dumps(data)
print("Serialized JSON string:")
print(json_str)

# Deserialize the JSON string back to a Python object (dictionary)
parsed_data = json.loads(json_str)
print("\nDeserialized Python object:")
print(parsed_data)

# Accessing individual elements in the parsed data
print("\nAccessing elements in the parsed data:")
print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
