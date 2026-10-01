#uvicorn and fastapi third party modules
#pip install uvicorn
#pip install fastapi
#python -m pip install uvicorn fastapi
#py -m pip install uvicorn fastapi
SUPABASE_URL="https://ypylxazeorlsvsmtcsiv.supabase.co"
SUPABASE_KEY="sb_publishable_KNgEvspvzkn-zg1az35BeQ_UdrC8LNk" 
 
from fastapi import FastAPI #importing Fastapi class
from supabase import create_client
fastapi_obj=FastAPI()  #creating fastapi object
#how to start backend server be
#uvicorn main:fastapi_obj --reload
supabase_obj=create_client(SUPABASE_URL,SUPABASE_KEY)
@fastapi_obj.post("/register")
def user_registration(new_user:dict):
    print("reg function")
    print(new_user)
    res=supabase_obj.table("users").insert(new_user).execute()
    return{
        "msg":"reg done successfully",
        "data":res.data
    }
