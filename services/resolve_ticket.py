from models.main_model import MainModel
from models.movidesk import Person, Ticket
from datetime import datetime
from typing import List
from pydantic import validator

class TicketOutput(MainModel):
    created_date: datetime
    resolved_in: datetime = None
    urgency: str = None
    protocol: str
    subject: str = None
    status: str = None
    created_by: str = None
    clients: List[Person]
    nf: object
    order_id: object
    problem_type: object
    integrator_cnpj: object
    
    @validator('nf', 'order_id', 'problem_type', 'integrator_cnpj')
    def validate(cls, object):
        try:
            return object[0].value
        except Exception:
            return None
    
def resolve_ticket(tickets:List[Ticket]):
    outputs = []
    for ticket in tickets:
        nf = list(filter(lambda x:x.custom_field_id == 121853, ticket.custom_field_values))
        order_id = list(filter(lambda x:x.custom_field_id == 139052, ticket.custom_field_values))
        problem_type = list(filter(lambda x:x.custom_field_id == 121860, ticket.custom_field_values))
        integrator_cnpj = list(filter(lambda x:x.custom_field_id == 121854, ticket.custom_field_values))
        ticket_output = TicketOutput(
            protocol=ticket.protocol,
            createdDate=ticket.created_date,
            resolved_in=ticket.resolved_in,
            urgency=ticket.urgency,
            subject=ticket.subject,
            status=ticket.status,
            created_by=ticket.created_by,
            clients=ticket.clients,
            nf=nf,
            order_id=order_id,
            problem_type=problem_type,
            integratorCnpj=integrator_cnpj
        )
        outputs.append(ticket_output)
    return outputs