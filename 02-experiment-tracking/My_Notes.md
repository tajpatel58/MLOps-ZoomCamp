### Experiment Tracking Notes: 

There are many packages that can assist with experiment tracking, for this section I'll be using Mlflow. We've previously used TensorFlow extended. 

#### Key Concepts:

- ML Experiment: The process of building an ML model. 
- Experiment Run: Is a model training process with some set of hyperparameters and some set of data. (An ML experiment is a collection of experiment runs)
- Run Artifact: A file that is associated with an ML run, eg: could be a config file of hyperparams, or if data is queried from a SQL database then could be a file with the query used. 
- Experiment Metadata: Summary stats/metrics of the experiment run eg: the accuracy, F1 score, time to train, time for inference etc. 

#### Motivations for Experiment Tracking:

- Reproducibility: once we've built a model we want to be able to recreate this model in a production environment - experiment tracking keeps track of the training data used, hyperparams, model architecture, model params.. etc. 
- Orgnisation/Optimisation: Allows team members to know which model runs have been done and what other models we wish to try to improve on current version. 

#### MlFlow:

Installation and basics:

- MlFlow can be installed using pip. 
- Check installation with "mlflow" in terminal. 
- Running "mlflow ui" in terminal will start the local version of mlflow and can open a webpage for the mlflow gui. 
- Recall from our ML Ops course with Andrew Ng, packages like mlflow and TFX have a metadata store. A metadata store is a sql database that stores the data lineage. Ie: as data passes from component to component we want to keep track of the steps used, this tracking is done using s SQL database. 
- To ensure mlflow runs with this backend database we need to use the command: "mlflow ui --backend-store-uri sqlite://mlflow.db" Also need to set this in python if using within a notebook. 
- When using mlflow within a notebook, we need to set the "ML Experiment" that we are working in. This is so mlflow can store our models/experiment runs under the correct project. 

#### Logging Hyperparams and Metrics:

- To begin using mlflow once imported, within our training block of code, we need to wrap it in a special mlflow context manager. 
- Some common logging syntax within the mlflow context manager: "mlflow.log_param(""PARAMETER_NAME"", ""PARAMETER_VALUE"")
- Similarly: mlflow.log_metric(""METRIC_NAME"", ""METRIC_VALUE"")

