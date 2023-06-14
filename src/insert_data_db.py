import pandas as pd 
from sqlalchemy.sql import text as sa_text
from database import engine
from models import ChurnTrain
from sqlmodel import Session

# read data
df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/Churn_Modelling.csv")
print(df.head())

# Truncate table with sqlalchemy
with Session(engine) as session:
    session.execute(sa_text(''' TRUNCATE TABLE churntrain  '''))
    session.commit()

# Insert training data
records_to_insert = []
 
for df_idx, line in df.iterrows():
    records_to_insert.append(
                    ChurnTrain(
                                creditScore=line[1],
                                geography=line[2],
                                gender=line[3],
                                age=line[4],
                                tenure=line[5],
                                balance=line[6],
                                numOfProducts=line[7],
                                hasCrCard=line[8],
                                isActiveMember=line[9],
                                estimatedSalary=line[10],
                                exited=line[11]
                                )
    )

session.bulk_save_objects(records_to_insert)
session.commit()
# Ends database insertion
