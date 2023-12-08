from datetime import datetime
from pydantic import BaseModel
from typing import Union
from typing import Annotated
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}


# Syntax for type hinting


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item(item: int | str):
    print(item)


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


print(get_full_name("john", "doe"))


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


# Pydantic is a Python library to perform data validation
# You declare the "shape" of the data as classes with attriubtes.
# and each attribute has a type.


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    freinds: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)

print(user)

print(user.id)


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
