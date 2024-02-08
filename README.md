# ML Service

![Static Badge](https://img.shields.io/badge/python-3.12-green)
![Static Badge](https://img.shields.io/badge/docker_compose-red)
![Static Badge](https://img.shields.io/badge/FastAPI-green)
![Static Badge](https://img.shields.io/badge/Streamlit-red)

ML Service with HTTP API and Streamlit UI served in two separate Docker containers.

The model is a simple Logistic Regression iris classifier. You can replace it with model of your choice.

## Usage

Run the project with the following command:

```bash
docker compose up --build
```

You can also add `-d` flag to run in detached mode.

Once up and running, open [this link](http://localhost:8501) in your browser to access Streamlit UI and [this link](http://localhost:8000/docs) to access OpenAPI docs page.

## Authors

- Nick Kuzmenkov (@nickuzmenkov)
