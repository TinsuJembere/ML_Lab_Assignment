# you can see it live on:
- for logistics app: https://ml-lab-assignment.onrender.com
- for decision tree app: https://ml-lab-assignment-1.onrender.com

# ML Model Deployment Project

## Overview
This project demonstrates end-to-end ML deployment using:
- Logistic Regression
- Decision Tree

Both models have separate:
- Backend (FastAPI)
- Frontend (HTML forms)

## Setup
### Create virtual invironment
`python -m venv venv`

### Install dependencies
`cd logistic_app`

`pip install -r requirements.txt`

`cd ../decision_tree_app`

`pip install -r requirements.txt`


### Run the apps
`uvicorn main:app --host 127.0.0.1 --port 9050 # Logistic Regression`

`uvicorn main:app --host 127.0.0.1 --port 9051 # Decision Tree`

## Usage
1. Open the frontend URL
2. Enter values in the form
3. Click Predict

