from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float
    
class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
    
cars_db: List[Car] = []

@app.get("/ping")
def ping():
    return "pong"   

@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars_db.append(car)
    return car

@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars_db

@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
    for car in cars_db:
        if car.identifier == id:
            return car

    raise HTTPException(status_code=404, detail="Car with the provided id does not exist or was not found.")
@app.put("/cars/{id}/characteristics", response_model=Car)
def update_car_characteristics(id: str, characteristics: Characteristic):
    for car in cars_db:
        if car.identifier == id:
            car.characteristics = characteristics
            return car
    raise HTTPException(status_code=404, detail="Car with the provided id does not exist or was not found.")


