import json # Java Script Object Notation

employee = {"eid":101, "name":"Jhon", "salary":100000 }
print(employee)
print(type(employee))

print()

# Convert Dictonary to JSON
# JSON is textual i.e. String representation of Dictonary

jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))

jsonData = str(employee)
print(jsonData)
print(type(jsonData))



