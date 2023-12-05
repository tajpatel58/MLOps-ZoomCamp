### Deployment

- Deployment of your model is making it available to make predictions. 
- The type of deployment we need will depend on our use case, the forms are batch prediction, web service and streaming. 

##### Batch Predictions:

- Batch predictions are typically done by storing data in a database that need predictions, then running a "Scoring job" that fetches the data from the database and runs the predictions. 
- For now, it's a debate as to whether we should use a SQL database or just log data from a bucket. 

##### Web Service:

- Model is deployed as a web service and we can send requests to the endpoint to make predictions. 
- This is done in real time, hence the model needs to be available 24/7. 
- Can think of this as 1-1, one datapoint is sent to one endpoint for predictions. 

##### Streaming: 

- Here the data for predictions is being sent to a "Producer" initially which we can think of as a tunnel absorbing/streaming the data. 
- We then setup "Consumers" which consume the data from the "Producer" for predictions/etc. 
- This can be a many-many relationship, as we have multiple producers and multiple consumers. 
- The terminology here sounds very Data Engineery so might be quite interesting to do a project in it later. 
- Streaming is necessary when multiple data components need to be run on the data being streamed in. 


### Flask/FastAPI + Docker:

- Flask/FastAPI lets you build an API.
- Both packages are great for API development but FastAPI is the more modern tool. 
- We know API’s are like servers in a restaurant, they are built to deal with types of requests and determine who 2 machines talk to each other. 
- There are 4 main operations:
  - GET: An operation that involves obtaining data from a resource.
  - POST: An operation that submits data to be processed. Eg prediction of a datapoint.
  - DELETE: An operation that deletes a resource/data from a resource.
  - PUT: Updates a resource with new data.  
- In our Flask App, data is typically sent as a JSON and prediction is returned as JSON, so we should use the jsonify function from Flask in our prediction function.
    - `jsonify({"prediction" : predicted_output})`
- CURL, can be used to send data to the endpoint. 
- CURL requires:
  - Content type of what is being sent. 
  - The actual data being sent. 
  - The endpoint that the request should be sent to. 
- We can use Pickle to store models, vectorizers, scalers and any further preprocessing variables needed. 
- Our Flask app is created with the Flask method, and we pass the app name into the initializer. 

    - `app = Flask("TextReviewsModel")`
    - `app = FastAPI("TextReviewsModel")`

- Our predict method should be provided with a Flask decorator to tell the API how to deal with requests on this route, like below:

    - `@app.route('/predict', methods=["POST"])`

- We should add a debug mode incase we want to test out application locally like below. The debug method means that once the code is updated, the endpoint is also updated without having to restart the server.
    - `app.run(debug=True, host="0.0.0.0", port=9696)`

  - The command to run your app is different when using FastAPI, we run the following in terminal, then changes can be saved in API can be saved and API updates, it's the same as running Flask in debug mode:

    - `uvicorn test_api:app --reload`

- Clever feature of FastAPI, we can go on endpoints/docs and it will show the documentation for using the API, eg:

  - `http://127.0.0.1:8000/docs`

- Once we run our python script with this, the server begins to run. We can then use CURL to send requests with data. As mentioned above CURL requests need to be in a particular format: 

     - `curl -X POST "localhost:9696/predict" -H 'Content-Type: application/json' -d'
{
  "review": "This Chatbot is amazing"
}'`

- Note we can also use requests to exchange data with a web server. 

### PyDantic:

- Here we take a small detour on pydantic, which is a package used to enforce structure of inputs and outputs in our API methods. 
- So why might this be useful? 
  - Well suppose we get a "PUT" method to update the entry into a database. Database have schemas so we can't simply add any data into a particular table. Hence we pydantic to ensure that the correct keys are present. 
  - It provides input and output valdation of methods. Eg if a POST method should return an int, and we return a float, then that's a problem. 
- A bit like the base class of Pandas is: "DataFrame", pydnatic has "BaseModel", so the most "common" object we would be using in pydantic is a pydantic model.
- We can think of a pydantic model as a dictionary where we can access the elements like: `person.name`, NOT square brackets. 
- When creating an instance, we need to pass in values like keyword arguments to a function, 
- Pydantic is clever and may try to case a string to an int, if the type is int for a variable. 

- The following can be used to create a dictionary like object with a set structure:
  - `from pydantic import BaseModel`
  - `class Name_Age(BaseModel):`
    -   `name : str`
    -   `age : int`

- In summary, type hints with Pydantic are essential when building API's.