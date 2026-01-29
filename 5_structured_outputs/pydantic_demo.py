from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # name: str
    name: str = 'Aritri'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student') # Field is used to set constraints


# new_student= {'name': 'Aritri'}
new_student={'age': 22, 'email': 'abc@gmail.com', 'cgpa': 8} #pydantic has build-in validation system i.e. when the email is not given in its proper format, it throws error
#new_student={'age': '22'} #even when the numerical value is passed as a string , pydantic implicitly converts it into integer and then returns the value

student= Student(**new_student)

print(student)
student_dict= dict(student)
print(student_dict['name'])

#student_json=student.model_dump_json()

# print(student.name)
# print(type(student))