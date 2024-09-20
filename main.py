
from fastapi import FastAPI

from aiohttp_client import fetch_data
from data.pydantics_models import Item
from data.repositories.TestRepository import get_servers_by_flow_id
from service.VehicleService import get_vehicle_models_by_year, get_vehicle_models_not_sold

app = FastAPI()


@app.get("/")
async def root():
    # data = await get_vehicle_models_by_year(2021)
    # print(data)
    # for item in data['Results']:
    #     print(item['Model_Name'])

    data = await get_vehicle_models_not_sold()
    print(data)
    return "success"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/test")
async def get_third_party_api():
    get_servers_by_flow_id("test")
    data = await fetch_data("https://my-json-server.typicode.com/typicode/demo/posts")
    return data

@app.post("/test")
async def post_test(item: Item):
    return {"item": item.dict()}


@app.get("/get_models/{year}")
async def get_models(year):
    results = []
    data = await get_vehicle_models_by_year(2021)
    for item in data['Results']:
       results.append(item['Model_Name'])
    return { 'results': results }



@app.get("/get_discontinued_models")
async def get_discontinued_models():
    data = await get_vehicle_models_not_sold()
    return { 'results': data }

