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

Prefect is a tool that we can use to accomplish these tasks and build these workflows. 