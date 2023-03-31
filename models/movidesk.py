from .main_model import MainModel
from pydantic import validator
from typing import List
from datetime import datetime

class Item(MainModel):
    custom_field_item: str = None
    person_id: str = None
    storage_file_guid: str = None

class Movidesk(MainModel):
    custom_field_id: int = None
    custom_field_rule_id: int = None
    items: List[Item]
    line: int = None
    value: str = None

class Person(MainModel):
    business_name: str = None
    
class Ticket(MainModel):
    protocol: str
    created_date: datetime
    resolved_in: datetime = None
    urgency: str = None
    protocol: str
    subject: str = None
    status: str = None
    created_by: str = None
    clients: List[Person]
    custom_field_values: List[Movidesk]
    


   
    
    
    # category: str = None
    # clients: List[Person] = None
    # protocol: str = None
    # resolved_in: str = None
    # service_full: list = None
    # status: str = None
    # subject: str = None
    # urgency: str = None
    # id: int = None
    # owner: str = None
    
    # @validator('owner', pre=True)
    # def valid_owner(cls, value):
    #     try:
    #         name = Person(**value)
    #         return name.business_name
    #     except:
    #         return None
        
