from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from data.models.base import AuditMixin, Base


class UserModel(Base, AuditMixin):
    __tablename__ = "user"
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4, init=False)
    username: Mapped[str] = mapped_column(unique=True)
    full_name: Mapped[str]
    hashed_password: Mapped[str]
