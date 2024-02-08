from fastapi import FastAPI
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

data = load_iris()
X = data["data"]
y = data["target"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

app = FastAPI()


@app.get("/predict")
def predict(
    petal_height: float,
    petal_width: float,
    sepal_height: float,
    sepal_width: float,
):
    predict = model.predict(
        [[sepal_width, sepal_height, petal_width, petal_height]]
    )
    return data["target_names"][predict][0]
