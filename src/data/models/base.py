from datetime import UTC, datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


def now_utc():
    return datetime.now(UTC)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class AuditMixin(MappedAsDataclass):
    created_at: Mapped[datetime] = mapped_column(
        default_factory=now_utc,
        init=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=now_utc,
        onupdate=now_utc,
        init=False,
    )
