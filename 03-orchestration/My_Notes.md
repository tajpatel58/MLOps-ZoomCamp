### Orchestration and ML Pipelines:

- We can think orchestration as the task of "automating" something using a tool.
- ML Pipelines are similar to data pipelines on Azure Data Factory, in the sense that each component has a task. However I think the key difference is that ML pipelines involve training/deploying models as opposed to data manipulation. 

##### Common ML Engineer Tasks:

The goal of this chapter will be to learn some of the responsibilities of an ML engineer. We know from our ML Ops course on DeepLearning.AI that some of the responsibilities of an ML Engineer would be:

- Setting up a training pipeline. 
- Implementing logging of metrics/parameters. 
- Creating a dashboard from logged data.
- Ensure this pipeline automatically retries incase of failures and provides email updates when components complete/fail. 
- Implement caching, in the sense of if inputs don't change or some computation is already done then we use the cached data. 

##### Introduction to Prefect:

Prefect is a tool that we can use to accomplish these tasks and build these workflows. We can install this as a python package and use some of it's functionality through decorators. 

Some Prefect terminology:

These will make more sense once we practice and may not be entirely correct:

- Task: A python function used to to carry out some "work". 
- Flow: A flow is another python function which calls a set of tasks. These flows can be setup to know the dependencies needed to run a task. Eg. If live weather data needs to be fetched, then we can create a flow to run tasks only once the live weather data is available. 
- SubFlow: A subflow is a flow that will be called upon by another "parent" flow. 

Much like mlFlow Prefect is installed via pip, then we can run a server locally to gain access to the Prefect UI. 

Start Prefect UI: `prefect server start`

Note the server will start on a particular port and pipeline metadata will be stored in SQLite database (like Mlflow). We need to make sure our UI starts correctly and knows where the database is located. 

- The "cat_facts.py" gives a basic example of a task and flow within Prefect. We can simply run the scripts once the flows/tasks are setup and the "flow" run will appear on our Prefect UI. 

Log Prints: `@flow(log_prints=True)` means when we log any print statements within a flow. 

- Each "flow" within a Python script appears within our Prefect UI. Maybe we have a script for all preprocessing on data? Each preprocessing component is a "task" and all the calls are contained within a "flow". 

- We might have preprocessing in one flow, and training in another flow. Think of ADF - the more granular we get the easier it is to track failures/runs. 

- We can also have flows called from other flows. Eg say to preprocess some weather data - we would have a flow that fetches live weather information and we'd call this flow within the "preprocessing" flow. To call a flow we simply call the function that has the `@flow` decorator.


#### Prefect Usage/Tips:

- Some flows/tasks might be fetching data via an API, it's best to set a few retries on this as often data fetching can fail:

`@task(retries=4, retry_delay_seconds=0.3)`

