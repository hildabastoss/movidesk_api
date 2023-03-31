from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


def to_camel_case(value: str):
    words = value.split('_')
    result = words[0]
    for word in words[1:]:
        result += word.title()
    return result


class MainModel(BaseModel):
    class Config:
        alias_generator = to_camel_case


class ObjId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid id")

        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class DbModel(MainModel):
    id: ObjId = Field(alias='_id', default=None)
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        json_encoders = {ObjectId: str}
        anystr_strip_whitespace = True
