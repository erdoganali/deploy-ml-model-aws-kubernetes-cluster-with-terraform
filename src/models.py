from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field 

class Churn(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creditScore: int
    geography: str
    gender: str
    age: int
    tenure: int
    balance: float
    numOfProducts: int
    hasCrCard: int
    isActiveMember: int
    estimatedSalary: float 
    prediction: int
    prediction_time: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    client_ip: str


class ChurnTrain(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creditScore: int = Field(default=None)
    geography: str = Field(default=None)
    gender: str = Field(default=None)
    age: int = Field(default=None)
    tenure: int = Field(default=None)
    balance: float = Field(default=None)
    numOfProducts: int = Field(default=None)
    hasCrCard: int = Field(default=None)
    isActiveMember: int = Field(default=None)
    estimatedSalary: float = Field(default=None)
    exited:int= Field(default=None)


class CreateUpdateChurn(BaseModel):
    creditScore: int
    geography: str
    gender: str
    age: int
    tenure: int
    balance: float
    numOfProducts: int
    hasCrCard: int
    isActiveMember: int
    estimatedSalary: float

 
    class Config:
        schema_extra = {
            "example" : {
                "creditScore": 619, 
                "geography" : "France",
                "gender" : "Female",
                "age" : 42,
                "tenure" : 2,
                "balance" : 0.0,
                "numOfProducts" : 1,
                "hasCrCard" : 1,
                "isActiveMember" : 1,
                "estimatedSalary" : 101348.88
            }
        }

class ChurnDriftInput(SQLModel):
    n_days_before: int

    class Config:
        schema_extra = {
            "example": {
                "n_days_before": 5,
            }
        }