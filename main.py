from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/cars", status_code=201)
def create_car(car: dict):
    return car

@app.get("/cars")
def list_cars():
    return {"cars": [{"car_id": 1, "make": "toyota", "model": "corolla"}]
            [{"car_id": 2, "make": "honda", "model": "civic"}]}
    
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    return{"car_id": car_id}

@app.put("/cars/{car_id}")
def update_car(car_id: int, car: dict):
    return {"car_id": car_id, **car}

