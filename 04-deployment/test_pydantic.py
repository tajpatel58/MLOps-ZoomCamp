from typing import Literal
from pydantic import BaseModel, Field, validator
from pydantic.types import constr

class Person(BaseModel):
    name : str
    age: int

# Contact Entry made up of name and 11 digit number
# Note const using partial regex matching not full.
class ContactEntry(BaseModel):
    person : Person
    phone_number: constr(regex="[0-9]{11}", max_length=11)

#Literal forces values to be out of a list.
class Account(BaseModel):
    account_id : str
    employee_size : Literal["small", "medium", "large"]

    # validator is run each time instance is instantiated, saves us a call.
    @validator("account_id")
    def account_id_validator(cls, value):
        # want account_id to be 9 digits and each number only appears once:
        list_of_digits = list(value)
        num_digits = len(list_of_digits)
        if num_digits != 9:
            raise ValueError(f"Account Id needs to be 9 characters not: {num_digits}")
        
        digits_seen = []
        for dig in list_of_digits:
            if dig in digits_seen:
                raise ValueError(f"Repeated digits not allowed: account id has digit: {dig} repeated.")
            else:
                digits_seen.append(dig)
        print(f"Account Id: {value} is acceptable")
        
        # MUST RETURN THE VALUE IF ACCEPTABLE:
        return value


p1 = Person(name="Taj", age="24")
p2 = Person(age=10, name="Taj")
phone_error = "1231"
phone_2= "01982711112"

# Following should run smoothly as phone number is valid.
try:
    contact_entry = ContactEntry(person=p2, phone_number=phone_2)
    print(f"Contact Entry Created Succesfully:")
    print(contact_entry.dict())
except Exception as e:
    print(e)

# Following should fail as phone number is valid.
try:
    contact_entry = ContactEntry(person=p2, phone_number=phone_error)
    print(f"Contact Entry Created Succesfully:")
    print(contact_entry.dict())
except Exception as e:
    print(e)

# Following should throw an error as digit 7 repeated in account_id
try:
    account_1 = Account(account_id="123456779", employee_size="small")
    print(f"Account Created:")
    print(account_1.dict())
except Exception as e:
    print(e)

# Following should throw an error as length of account id only 3 digits.
try:
    account_1 = Account(account_id="123", employee_size="small")
    print(f"Account Created:")
    print(account_1.dict())
except Exception as e:
    print(e)

# Following should throw an error as employee size is extra large which is not in list.
try:
    account_1 = Account(account_id="123456789", employee_size="extra_large")    
    print(f"Account Created:")
    print(account_1.dict())
except Exception as e:
    print(e)

# Following should throw an error as employee size is extra large which is not in list.
try:
    account_1 = Account(account_id="123456789", employee_size="small")
    print(f"Account Created:")
    print(account_1.dict())
except Exception as e:
    print(e)