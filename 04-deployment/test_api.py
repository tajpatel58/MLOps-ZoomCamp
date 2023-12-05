import uvicorn
from fastapi import FastAPI
from flask import Flask
from pydantic import BaseModel


app = FastAPI()

class PredictIn(BaseModel):
    name : str
    age : int

class PredictOut(BaseModel):
    text : str

# You can think of pydantic as a type of object creator with strictness
# In this case we use it to check we have the correct keys.
@app.post("/predict")
def testing_predict(person : PredictIn) -> PredictOut:
    output_text = f"The name is: {person.name} and Age is: {person.age}"
    output = PredictOut(text=output_text)
    return output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)