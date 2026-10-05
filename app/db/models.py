from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
class Base(DeclarativeBase):
    pass
class QuoteRecord(Base):
    __tablename__ = "quotes"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount_minor: Mapped[int] = mapped_column()
    source_currency: Mapped[str] = mapped_column()
    target_currency: Mapped[str] = mapped_column()
    source_country: Mapped[str] = mapped_column()
    target_country: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)