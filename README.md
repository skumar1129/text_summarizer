# Text Summarizer Fast API 

## Project Background
The goal of this project was to combine knowledge of basic machine learning as well as backend services. To do that I created a FastAPI service that has one endpoint that takes in a large amount of text and returns a summarization of the text. Uses SpaCy and TFIDF algorithm to summarize text

## Tech Stack
Python, FastAPI, SpaCy

## Set Up

### Create Virtual ENV
```python3 -m venv env```

### Activate Virutal ENV
```source env/bin/activate```
### Install dependencies
```pip install -r requirements.txt```
### Run the app
```uvicorn main:app --reload```

### Swagger UI
Navigate to localhost:8000/docs and can directly use the endpoint there