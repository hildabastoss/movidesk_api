import requests

api_url = "https://api.movidesk.com/public/v1/tickets?token=07451a55-8dee-4af4-91cc-4f92d147a6d6&$select=id,status,protocol,subject,category,urgency,createdDate,resolvedIn,owner,createdBy,serviceFull&$filter=ownerTeam eq 'Pós Vendas'&$expand=owner($select=businessName),clients($select=businessName)"

response = requests.get(api_url)