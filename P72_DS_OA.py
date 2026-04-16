# %%
# write a python function that accepts functions as arguments, 
# returns a new function representing their composition, 
# passes args to the first function, passes each function's output 
# to the next function and returns the final output. 
# The provided funcs are 
# add(*args): returns sum of all args 
# square(a) returns square 
# splitter(a) returns [floor(a/2), a%2] 
# my_max(a) returns max val in a number or list 
# my_min(a) returns min val in a number or list 
# 
# Note only the first function handles multiple args: 
# subsequent functions take a single argument. 
# def compose(*functionsList): 
# Example 
# functionList = [add, splitter] 
# compose(functionList[1], functionList[2]) 
# shoulr return a function, composedFunctions. 
# if argumentList = [2,3], composedFunctions(2,3) should return [2,3]
def add(*args):
    return sum(args)

def square(a):
    return a ** 2

def splitter(a):
    return [a//2, a %2]

def my_max(a):
    return max(a) if isinstance(a, list) else a

def my_min(a):
    return min(a) if isinstance(a, list) else a


def compose(*function_list):
    def composed(*args):
        res = function_list[0](*args)
        for func in function_list[1:]:
            res = func(res)
        return res
    return composed


functionList = [add, splitter, my_max, splitter, my_min, square]
composedFunc = compose(*functionList)
res = composedFunc(1,2,3,4)
# %%
# implement two mixin classes that add functionality to Python class: DictMixin: 
# Adds a to_dict method that converts a python class to dict JSONMixin: 
# adds a to_json method that convera python class to JSON 
# The mixin should: only converrt object attributes that do not start 
# with '_' raise a type error with message 'Object is not JSON 
# serializable' if a class cannot be converted to JSON 
# 
# Example Class MyClass(DictMixin, JSONMixin): 
# def __init___(self, name, data, secret): 
#   self.name = name 
#   self.data = data 
#   self._secret = secret 
# 
# obj = MYClass("abc", 10, "secret"): 
# obj.to_dict() should return {'name':'abc', 'data': 10} 
# obj.to_json() should return {"name":"abc", "data":10}
import json

# Only DictMixin
class DictMixin:
    def to_dict(self):
        """
        Convert all public attributes (not starting with '_') to dict
        """
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


# Only JSONMixin (works independently)
class JSONMixin:
    def to_json(self):
        """
        Convert public attributes to JSON string.
        Raises TypeError if object is not JSON serializable
        """
        # Build dict inside JSONMixin since no DictMixin is inherited
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        try:
            return json.dumps(data)
        except (TypeError, ValueError):
            raise TypeError("Object is not JSON serializable")


# Example class with DictMixin only
class MyClass1(DictMixin):
    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret


# Example class with JSONMixin only
class MyClass2(JSONMixin):
    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret


# Test
obj1 = MyClass1("abc", 10, "secret")
print(obj1.to_dict())  # {'name': 'abc', 'data': 10}

obj2 = MyClass2("xyz", 20, "topsecret")
print(obj2.to_json())  # '{"name": "xyz", "data": 20}'