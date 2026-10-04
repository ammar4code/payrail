from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
class Base(DeclarativeBase):
    pass
class QuoteRecord(Base):
    __tablename__ = "quotes"
    id: Mapped[int] = mapped_column(primary_key=True)