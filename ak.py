# from fastapi import FastAPI,HTTPException,status
# from pydantic import BaseModel
# from passlib.context import CryptContext
# from jose import jwt
# from datetime import datetime,timedelta

# app=FastAPI()
# pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")

# SECRET_KEY ="Hell's-paradise"
# ALGORITHM= "HS256"



# # password="akshi181109"
# # hashed =pwd_context.hash(password)

# # print(f"original password:{password}")
# # print(f"hased password: {hashed}")

# # correct=pwd_context.verify("akshi181109",hashed)
# # print(f"password correct: {correct}")

# # wrong=pwd_context.verify("akshith",hashed)
# # print(f"password is {wrong}")

# # hash1=pwd_context.hash("akshith")
# # hash2=pwd_context.hash("akshith")

# # print(hash1==hash2)
# # print(pwd_context.verify("akshith",hash1))
# # print(pwd_context.verify("akshith",hash2))

# def hash_password(password:str)-> str:
#     return pwd_context.hash(password)

# def verify_password(password:str,hashed_password:str)->bool:
#     return pwd_context.verify(password,hashed_password)

# users_db=[]

# class User_RL(BaseModel):
#     username:str
#     password:str
    
# @app.post("/register",status_code=201)
# def register(user:User_RL):
#     for u in users_db:
#         if u["username"]==user.username:
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Username already taken")
#     hashed=hash_password(user.password)

#     new_user={
#         "id":len(users_db)+1,
#         "username":user.username,
#         "hashed_password":hashed
#     }
#     users_db.append(new_user)
#     return {"message":f"Account created for {user.username}"}

# @app.post("/login")
# def login(user:User_RL):
#     found_user=None
#     for u in users_db:
#         if u["username"]==user.username:
#             found_user=u
#             break
#     if not found_user:
#         raise HTTPException(status_code=401,detail="Invalid username or password")
#     if not verify_password(user.password,found_user['hashed_password']):
#         raise HTTPException(status_code=401,detail="Invalid username or password")
    
#     return {"message":"login successful","username":user.username}
#     token = Create_access_token(user.username)
#     return {"Access_token": token,"token_type":"bearer"
#     ""
#     ""
#     ""}

# @app.get("/register")
# def data():
#     return users_db

# # here we create a new token for authorization
# # def Create_access_token(username:str)->str:
# #     payload = {
# #             "sub":username,
# #             "exp":datetime.utcnow()=timedelta(minutes=60)
# #             }
# #     return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    
    


