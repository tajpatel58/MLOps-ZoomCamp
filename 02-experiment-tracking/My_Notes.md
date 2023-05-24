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
- To ensure mlflow runs with this backend database we need to use the command: "mlflow ui --backend-store-uri sqlite:///mlflow.db" Also need to set this in python if using within a notebook. (mlflow.set_tracking_uri("sqlite:///mlflow.db"))
- Once we start using the mlflow within a notebook, the "mlflow.db" file should be created and running mlflow ui command in terminal will start the mlflow interface with the data from the database.
- When using mlflow within a notebook, we need to set the "ML Experiment" that we are working in. This is so mlflow can store our models/experiment runs under the correct project. 

#### Logging Hyperparams and Metrics:

- To begin using mlflow once imported, within our training block of code, we need to wrap it in a special mlflow context manager. 
- Some common logging syntax within the mlflow context manager: "mlflow.log_param(""PARAMETER_NAME"", ""PARAMETER_VALUE"")
- Similarly: mlflow.log_metric(""METRIC_NAME"", ""METRIC_VALUE"")
- For logging artifacts like a pickle'd version of a model we have: mlflow.log_artifact(""LOCAL_PATH"", ""ARTIFACT_PATH"")
- You can add tags to model runs, based on the type of model: eg if we only wanted to look at tree based models could do: mlflow.set_tag("model_type", "tree")
- In the Mlflow ui can use: tags.model_type = "tree", to see all models that are tree based.
- Within the Mlflow UI can see the different combinations of hyperparameters used, and how this has affected the logging metrics. Eg: if we wanted to see how learning rate has impacted the RMSE. 
- For some ML frameworks: sci-kit learn, XGBoost, PyTorch, TensorFlow etc we have "AutoLogging" so if a model is trained using any of these frameworks can enable automatic logging in MlFlow. eg for XGBoost we would use: mlflow.xgboost.autolog().
- AutoLogging is super powerful in the sense that it will track all hyperparams, metrics and even creates an MLFLow Model so we can deploy, a requirements.txt and even information on feature importance. 

If correctly setup we should have something like:

![alt text](./images/MlFlow_Runs.png "MlFlow Runs")


#### Model Management:

- As mentioned previously we can save models using the pickle library. To make this file shareable we can use the log_artifact method of mlflow to store this on our UI and furthermore make it available to other data scientists. 
- Though logging artifacts is okay, what if we had multiple versions pickled? What was the environment used to create the model? What preprocessing was needed? 
- To account for this, we can use built in methods for Mlflow. The format goes: "mlflow.xgboost.log_model(model_object, artifact_path)" - changing the framework from xgboost to whatever has been used. This like autologging, tracks the dependencies, environemtn information, and also the model artifact. 
- Can we also use the mlflow.log_artifact method to store python objects needed for Preprocessing: eg: OneHotEncoders, RobustScalers etc.
- By managing our models like this, then we have everything we need to provide inference and track models. 
- Furthermore, this method provides an API to Pandas and PySpark: by using the run URI (unique resource identifier), we can load the model into Python and use it for inference on PySpark and Pandas dataframes. (Loads into PySpark as a UDF)
- We can also load the model in as a Python function OR as an object of the framework we used to train. Eg: can load an XGBoost model as a python function OR as an XGBoost model. (These are calls "model flavours". - either as a Python function or a model from the framework we used.)
