from pydantic import BaseModel, Field
from pydantic.types import constr

class Person(BaseModel):
    name : str
    age: int

# Contact Entry made up of name and 11 digit number
# Note const using partial regex matching not full.
class ContactEntry(BaseModel):
    person : Person
    phone_number: constr(regex="[0-9]{11}", max_length=11)


p1 = Person(name="Taj", age="24")

p2 = Person(age=10, name="Taj")
phone_2= "01982711112"

contact_entry = ContactEntry(person=p2, phone_number=phone_2)
print(contact_entry.phone_number)
print(contact_entry.person.name)
