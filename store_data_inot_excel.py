import pandas as pd
import os


def DataStore(name, phone_number, email, occupation):
    if os.path.isfile("user_data.xlsx"):
        df = pd.read_excel("user_data.xlsx")
        df.append([name, phone_number, email, occupation])
        df.to_excel("user_data.xlsx", index=False)
    else:
        df = pd.DataFrame([name, phone_number, email, occupation],
                          columns=["name", "phone_number", "email", "occupation"])
        df.to_excel("user_data.xlsx", index=False)

