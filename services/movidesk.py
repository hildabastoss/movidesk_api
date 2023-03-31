import requests
from models.movidesk import Ticket
# from pprint import pprint
# from json import load
from services.resolve_ticket import resolve_ticket

base_url = 'https://api.movidesk.com/public/v1'
movidesk_token = '07451a55-8dee-4af4-91cc-4f92d147a6d6'
api_url = f"{base_url}/tickets?token={movidesk_token}&$select=id,createdDate,status,subject,category,urgency,resolvedIn,protocol,customFieldValues&$expand=customFieldValues($expand=items),clients&$filter=ownerTeam eq 'Pós Vendas'"
response = requests.get(api_url)

def get_data_movidesk():
    if response.status_code == 200:
        datas = response.json()
        # pprint(datas)
        tickets = [Ticket(**data) for data in datas]
        return resolve_ticket(tickets=tickets)
        
    else: 
        print('Errou miserávi')
    

   
   
   
   
   
   
        # with open(file='request_response.json', mode='r') as file:
        #     datas = load(file)
    # tickets = [Ticket(**data) for data in datas]
    # return tickets
    # pprint(tickets)
    # if response.status_code == 200:
    #     datas = response.json()
    #     pprint(datas)
    # # else: 
    #     print('Errou miserávi')
        
        
        
    