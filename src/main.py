from fastapi import FastAPI, Depends, Request
from sqlmodel import Session
from models import CreateUpdateChurn, Churn, ChurnDriftInput
from config import load_model_from_s3
from database import get_db, engine
import pandas as pd
from scipy.stats import ks_2samp
import models

## Load Model

model = load_model_from_s3()
 
app = FastAPI() 


######################################
## ENDPOINTS #########################
######################################
@app.get("/")
def root_endpoint():
    return {"message": "Hello Churn Prediction API!"}
 
@app.post("/prediction/churn")
async def predict_churn(request: CreateUpdateChurn,
                        fastapi_req: Request,
                        db: Session = Depends(get_db) 
                         ) -> dict:
    prediction = make_churn_prediction(model, request.dict())   
    inserted_record = insert_request_to_db(request=request.dict(),prediction=prediction,client_ip=fastapi_req.client.host,db=db)
    return  {"inserted_record": inserted_record}
 
@app.post("/drift/advertising")
async def detect(request: ChurnDriftInput):
    # Select training data
    train_df = pd.read_sql("select * from churntrain", engine)

    # Select predicted data last n days
    prediction_df = pd.read_sql(f"""select * from churn 
                                    where prediction_time >
                                    current_date - {request.n_days_before}""",
                                engine)
    
    #CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Exited
    creditScore_drift = detect_drift(train_df.creditScore, prediction_df.creditScore)
    balance_drift = detect_drift(train_df.balance, prediction_df.balance)
    estimatedSalary_drift = detect_drift(train_df.estimatedSalary, prediction_df.estimatedSalary)

    return {"creditScore_drift": creditScore_drift, "balance_drift": balance_drift, "estimatedSalary_drift": estimatedSalary_drift}

######################################
## FUNCTIONS #########################
######################################
def make_churn_prediction(model, request):
    #parse input from the request
    creditScore = request["creditScore"]
    geography = request['geography']
    gender = request['gender']
    age = request['age']
    tenure = request['tenure']
    balance = request['balance']
    numOfProducts = request['numOfProducts']
    hasCrCard = request['hasCrCard']
    isActiveMember = request['isActiveMember']
    estimatedSalary = request['estimatedSalary']
    
    # Make an input vector
    person = [[creditScore, geography, gender, age, tenure, balance, numOfProducts, hasCrCard, isActiveMember, estimatedSalary]]
    
    # Predict
    prediction = model.predict(person) 
    return prediction[0]

def insert_request_to_db (request, prediction, client_ip, db):
    new_churn = Churn(
        creditScore=request["creditScore"],
        geography=request['geography'],
        age = request['age'],
        tenure = request['tenure'],
        balance = request['balance'],
        numOfProducts = request['numOfProducts'],
        hasCrCard = request['hasCrCard'],
        isActiveMember = request['isActiveMember'],
        estimatedSalary = request['estimatedSalary'],
        prediction=prediction,
        client_ip=client_ip
    )

    with db as session:
        session.add(new_churn)
        session.commit()
        session.refresh(new_churn)

    return new_churn

def detect_drift(data1, data2):
    ks_result = ks_2samp(data1, data2)
    if ks_result.pvalue < 0.05:
        return "Drift exits"
    else:
        return "No drift"

