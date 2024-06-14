from fastapi import FastAPI
from datetime import datetime, timezone
from dateutil.tz import tzutc
from pydantic import BaseModel
import boto3

app = FastAPI()

class Item(BaseModel):
  hour: int
  access_key: str
  secret_key: str
    
@app.post("/list")
async def get_iam_user_list(item: Item):
  item_dict = item.model_dump()
  client = boto3.client('iam', aws_access_key_id=item_dict["access_key"], aws_secret_access_key=item_dict["secret_key"])
  user_list = client.list_users()
  now_utc = datetime.now().astimezone(tzutc())
  data = []
  
  for user in user_list["Users"]:
    access_key_list = client.list_access_keys(UserName=user["UserName"])
    
    for access_key in access_key_list["AccessKeyMetadata"]:
      diff_hour = (now_utc - access_key["CreateDate"]).total_seconds() / 3600
      
      if diff_hour > item_dict["hour"]:
        dict = {'UserID': user["UserId"], "Access Key ID": access_key["AccessKeyId"]}
        data.append(dict)
  return data