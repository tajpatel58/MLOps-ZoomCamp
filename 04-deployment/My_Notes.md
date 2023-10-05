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