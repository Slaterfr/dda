from datetime import datetime, timezone
from sqlmodel import SQLModel as sqlm
from sqlmodel import Field, SQLModel, Column, DateTime, func


class coin_history(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    coin_id : str
    price : float
    market_cap : float
    volume : float
    timestamp : datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            nullable=False, 
            server_default=func.now()
        )
    )

class coin_current(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    coin_id : str
    price : float
    market_cap : float
    volume : float
    last_update: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            nullable=False, 
            server_default=func.now(), 
            onupdate=func.now()
        )
    )

class events(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    coin_id : str
    type : str
    value : str
    timestamp : datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            nullable=False, 
            server_default=func.now()
        )
    )