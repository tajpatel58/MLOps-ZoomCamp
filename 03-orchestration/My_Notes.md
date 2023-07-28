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


#### Prefect Deployment:

So let's summarise what we've done so far. If we're working on a pipeline project:

- We've created a series of python scripts that will fetch data, preprocess, train a model. 
- Our python scripts are setup with `@flow`, and `@task` decorators so that each "component" is setup as a flow. 
- Running these scripts will yield a series of runs on Prefect UI. 

The goal now would be to be able to run this code on a virtual machine, that way it can be orchestrated. Remember orchestration can be thought of as the process of automating the running of processes. Doing so would allow a VM to spin up and run the collection of flows, essentially like a pipeline on ADF. 

The following is a brief overview of how we can deploy our scripts. 

![alt text](./images/flow-deployment-end-to-end.png "Prefect Deployment")


The steps go:

1. Run `prefect project init`, this will setup a prefect.yaml file which will specify if we need further dependencies for our scripts to run. Eg: may need a Docker container with certain versions of packages. We also specify where code needs to be pushed to and where the code needs to be pulled/fetched from. 
2. We then go onto our Prefect UI to setup "Work Pools" which we can think of as a group of workers that are ready for tasks. A bit like you might go to B&Q for handymen, you might go to `Google Cloud Run` if you want to execute your flow runs on this platform. OR you might use Azure Container Instances if you want to run code on Azure containers. Work pools are just what we use to run our flows - can even run as a subprocess on our laptops. 
3. Then we can start our Work pools: `prefect worker start -p <pool name> -t process`. This gets our worker pool running. 
4. We can then deploy our flow (though need to specify the exact flow we want to deploy, the name of the deployment and the pool it will run on). Eg:

`prefect deploy cat_facts.py:fetch -n deployment_name -p work_pool_run_on`

5. Now our flow has been deployed onto a worker pool/(set of workers) - that are equipped with the processing/task requirements. (speficied in prefect.yaml file) So we can finally trigger the run: `prefect deployment run flow_name/deployment_name`, which will run our code/flows on a container. These runs can be tracked via Prefect UI. 

Notes:

- "Blocks" are used to secure store credentials needed. For example if we need to access data from a Datalake, we can parse the credentials for AWS/GCP using the "blocks". 
- Can schedule our Flow runs on our workers through the Prefect UI. At this point the workflow is auomated. We've essentially shcedulded a series of data preprocessing steps and model training.  