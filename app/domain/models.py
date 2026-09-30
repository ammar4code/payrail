from dataclasses import dataclass
@dataclass(frozen=True)
class Money:
    amount_minor: int
    currency: str
@dataclass(frozen=True)
class Quote:
    provider: str
    send_amount: Money
    receive_amount: Money
    fee: Money
    delivery_hours:int