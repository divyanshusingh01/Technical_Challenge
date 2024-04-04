def get_value(obj, key):
    keys = key.split('/')
    for k in keys:
        if k in obj:
            obj = obj[k]
        else:
            return None
    return obj

# Example usage:
obj1 = {"a":{"b":{"c":"d"}}}
key1 = "a/b/c"
print(get_value(obj1, key1))  # Output: d

obj2 = {"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
print(get_value(obj2, key2))  # Output: a
