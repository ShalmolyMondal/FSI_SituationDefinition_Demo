# from typing import Union

# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     context_attribute:str
#     fuzzy_set:str


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/get_fuzzy_output")
# async def getFuzzyOutput(a: Item):
#     # print(a.name, a.age, a.dict())
#     #collect the inputs
#     name, age = a.context_attribute, a.context_attribute
#     print(a.dict())
#     b = {}
#     b["hello"] = 100
#     return b


# # density from front end and speed is also from front end
# # set in backend where we will have to find

# density_less={
#     20:0.3,
#     ...
# },
# set values:{
#     o.3:'low traffic'
# }
# var something=density['20'] => 0.3

# reuturn values[something] => lowtraffic;
# # density :{

# # }
# # from dd => a{
# #     density : 'less',
# #     speed: 'slow',
# # }
