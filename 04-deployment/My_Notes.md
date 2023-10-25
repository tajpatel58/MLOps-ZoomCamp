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


### Flask + Docker:

- Flask lets you build an API.
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

- Our predict method should be provided with a Flask decorator to tell the API how to deal with requests on this route, like below:

    - `@app.route('/predict', methods=["POST"])`

- We should add a debug mode incase we want to test out application locally like below. The debug method means that once the code is updated, the endpoint is also updated without having to restart the server.  
    - `app.run(debug=True, host="0.0.0.0", port=9696)`

- Once we run our python script with this, the server begins to run. We can then use CURL to send requests with data. As mentioned above CURL requests need to be in a particular format: 

     - `curl -X POST "localhost:9696/predict" -H 'Content-Type: application/json' -d'
{
  "review": "This Chatbot is amazing"
}'`

- Note we can also use requests to exchange data with a web server. 