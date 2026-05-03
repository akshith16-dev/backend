# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
from database import Base, engine
from routers import auth, students

# Create all tables on startup — safe to call every time (IF NOT EXISTS)
# IMPORTANT: Import models before calling create_all so Base knows about them
import models.user     # noqa: F401 — registers User with Base
import models.student  # noqa: F401 — registers Student with Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API", version="1.0.0")

# CORS — allows the React frontend (Day 9) to call this API
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://frontend-mocha-nine-1.vercel.app",
        "https://frontend-miqcqw6pk-akshith16-devs-projects.vercel.app",
        os.getenv("FRONTEND_URL", "")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/students", tags=["Students"])

@app.get("/")
def root():
    return {"message": "Student API is running"}

# Run with: uvicorn main:app --reload
# API docs: http://localhost:8000/docs


# from fastapi import FastAPI,HTTPException,status
# from pydantic import BaseModel
# from typing import Optional


# students=[{"name":"akshith","age":20,"id":1,"city":"Kuppam"},
#          {"name":"uday","age":20,"id":2,"city":"Kuppam"},
#          {"name":"raghav","age":21,"id":3,"city":"Kuppam"},
#          {"name":"kumaresh","age":22,"id":4,"city":"Kuppam"},
#          {"name":"bharath","age":30,"id":5,"city":"Kuppam"}
#          ]

# app=FastAPI(title="Ak-server")

# # @app.get("/students")
# # def students_list():
# #     return students

# # @app.get("/students/{sid}")
# # def get_id(sid:int):
# #     for student in students:
# #         if student["id"]==sid:
# #             return student
# #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"the student with the id {sid} no found")

# # @app.get("/students/count")
# # def counting():
# #     count=0
# #     result = []
# #     for student in students:
# #         if student["id"]>203:
# #             count=count+1
# #             result.append(student)
# #     return {"students":result, "count": count}
# #     # return {f"total":{count}}

# # students=[]
# next_id=4

# # class Student(BaseModel):
# #     name: str
# #     age : int
# #     city: str

# # @app.put("/students",status_code=201)
# # def create_student(student:Student):
# #     global next_id
# #     new_student={
# #         "id": next_id,
# #         "name" :student.name,
# #         "age":student.age,
# #         "city":student.city
# #     }

# #     students.append(new_student)
# #     next_id+=1

# #     return students


# # @app.get("/students")
# # def student():
# #     global students
# #     return students
# # @app.put("/students/{student_id}")
# # def update(student_id:int):
# #     for i,s in enumerate(students):
# #         if s["id"]==student_id:
# #             students[i]={
# #                 "id": student_id,
# #                 "name":student.name,
# #                 "age":student.age,
# #                 "city":student.city
# #             }
# #             return students[i]
# #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with the {student_id} is not found")

# class Createstudents(BaseModel):
#     name:str
#     age:int
#     city:str

# @app.get("/students")
# def get_students():
#     return students

# @app.get("/students/{student_id}")
# def get_student_id(student_id=int):
#     for s in students:
#         if s["id"]==student_id:
#             return s
        
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the student with the {student_id} is not found")

# @app.post("/students",status_code=201)
# def create_students(Student:Createstudents):
#     global next_id
#     new={"id":next_id,
#          "name":student.name,
#          "age":student.age,
#          "city":student.city
#          }
#     students.append(new)
#     next_id+=1
#     return new

# # @app.put("/students/{student_id}")
# # def update_Student(studetn_id:int,student:StudentCreate):
#     # 