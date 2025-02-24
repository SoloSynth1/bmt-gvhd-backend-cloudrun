import pickle
from typing import List, Dict, Optional

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    instances: List[List[float]]

app = FastAPI()

model_path = "models/logreg_v1.pkl"
model = pickle.load(open(model_path, 'rb'))

@app.post("/predict")
def predict(request: PredictionRequest) -> Optional[Dict]:
    predictions = model.predict(request.instances)
    predictions = predictions.astype(np.int32).tolist()
    return {
        'predictions': predictions,
        'deployedModelId': "cloudrun_model",
        'model': model_path,
        'modelDisplayName': model_path,
        'modelVersionId': "1"
    }