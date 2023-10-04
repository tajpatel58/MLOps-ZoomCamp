# MLOps ZoomCamp:

- This repository is a fork of MLOps Zoomcamp, designed to educate individuals about the various components of MLOps. In each section, I'll closely follow the YouTube videos and course materials while documenting my insights in dedicated subdirectory files labeled as "My_Notes.md." This approach enables me to capture my learning and provides a handy reference for future reflection.

- Concurrently with this course, I will develop a sentiment analysis model to assess the emotions expressed in reviews for my portfolio website's Chatbot. I intend to leverage the knowledge acquired in this course to streamline the model's deployment and productionization process.

## Module 1: Introduction
- What is MLOps
- MLOps maturity model
- Running example: NY Taxi trips dataset
- Why do we need MLOps
- Course overview
- Environment preparation

## Module 2: Experiment tracking and model management
- Experiment tracking intro
- Getting started with MLflow
- Experiment tracking with MLflow
- Saving and loading models with MLflow
- Model registry
- MLflow in practice

## Module 3: Orchestration and ML Pipelines
- Workflow orchestration
- Prefect 2.0
- Turning a notebook into a pipeline
- Deployment of Prefect flow

## Module 4: Model Deployment
- Three ways of model deployment: Online (web and streaming) and offline (batch)
- Web service: model deployment with Flask
- Streaming: consuming events with AWS Kinesis and Lambda
- Batch: scoring data offline

## Module 5: Model Monitoring
- Monitoring ML-based services
- Monitoring web services with Prometheus, Evidently, and Grafana
- Monitoring batch jobs with Prefect, MongoDB, and Evidently

## Module 6: Best Practices
- Testing: unit, integration
- Python: linting and formatting
- Pre-commit hooks and makefiles
- CI/CD (Github Actions)
- Infrastructure as code (Terraform)