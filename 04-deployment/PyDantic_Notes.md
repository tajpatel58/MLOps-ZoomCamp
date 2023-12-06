### PyDantic:

- Here we take a small detour on pydantic, which is a package used to enforce structure of inputs and outputs in our API methods. 
- So why might this be useful? 
  - Well suppose we get a "PUT" method to update the entry into a database. Database have schemas so we can't simply add any data into a particular table. Hence we pydantic to ensure that the correct keys are present. 
  - It provides input and output valdation of methods. Eg if a POST method should return an int, and we return a float, then that's a problem. 
- A bit like the base class of Pandas is: "DataFrame", pydnatic has "BaseModel", so the most "common" object we would be using in pydantic is a pydantic model.
- We can think of a pydantic model as a dictionary where we can access the elements like: `person.name`, NOT square brackets: `person["name"]` 
- When creating an instance, we need to pass in values like keyword arguments to a function: `Person(name="Taj", age=24)`
- Pydantic is clever and may try to case a string to an int, if the type is int for a variable. 

- The following can be used to create a dictionary like object with a set structure:
  - `from pydantic import BaseModel`
  - `class Name_Age(BaseModel):`
    -   `name : str`
    -   `age : int`

- In summary, type hints with Pydantic are essential when building API's.
- Pydantic also has a "validator" decorator which can be used to check values of attributes of the classes if the conditions aren't as straightforward as being an integer etc. Suppose you wanted an account id, which is a 9 digit number with no repeated digits. Check: `test_pydantic.py` for this example. Using this validator decorator allows you to throw specific errors and even process the input to a different value and set that as the attribute value.
- There's also a `Literal` class in the `typing` package: `from typing import Literal`, which allows you to set a permitted range of values for an attribute and throw an error if not in that list. For example: if sampling from a set of distributions: uniform/gaussian, we can use: `Literal["uniform", "gaussian"]`
- Each pydantic method has a dict and json method to cast a pydantic model to another more user friendly object:
  - `object.dict()`
  - `object.json()`
  - These work well and can handle nested pydantic models as pydantic models are essentially complex dictionaries.
- As a final point, we can also use the dataclass decorator, but this doesn't have data validation (only type hints), however the main advantage is that dataclasses ships with python. 
- To conclude: pyDantic is simply an overpowered type declaration/validator tool, which is very important in building API's. 