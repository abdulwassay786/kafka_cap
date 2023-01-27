import logging
import pandas as pd
from fastapi import FastAPI
import uvicorn
from sensorsmock.service import SensorService

app = FastAPI()

sensor_service = SensorService()


@app.get("/api/luxmeter/{room_id}")
def get_luxmeter(room_id: str):
    if not sensor_service.is_allowed_room(room_id):
        return {"error": f"Room {room_id} not exists!"}
    data = sensor_service.get_lux_meter_data(room_id)
    return data

# @app.get("/data")
# def sample():
#     data = {"temp":"22"}
#     df = pd.DataFrame.from_dict(data, orient='index')
#     df.to_csv('./app', header=False)
#     return data


@app.post("/moisturemate")
def moisture_mate():	
	return {"Data": "Received"}

@app.post("/carbonsense")
def carbon_sense():	
	return {"Data": "Received"}
	
	



@app.on_event("startup")
async def startup():
    await sensor_service.start()


def run_app():
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=3000)


if __name__ == "__main__":
    run_app()
    





# import requests
# url = "http://host.docker.internal:3000/api/luxmeter/kitchen"
# x=requests.get(url)
# white_check_mark
# eyes
# raised_hands





# 10:29
# url ko change kar lijiye ga
# 10:29
# host.docker.internal ko localhost kar lain