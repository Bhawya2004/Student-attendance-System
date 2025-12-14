from pydantic import BaseModel

class StudentData(BaseModel):
    age: int
    studytime: int
    failures: int
    absences: int
    Medu: int
    Fedu: int
    internet: int
    G1: int
    G2: int
