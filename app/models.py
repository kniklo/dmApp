from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    class Criterion(db.Model):
        id: so.Mapped[int] = so.mapped_column(primary_key=True)
        name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
        weight: so.Mapped[float] = so.mapped_column(default=0.0)
        description: so.Mapped[str | None] = so.mapped_column(sa.String(256))
        #parent_id: so.Mapped[int | None] = so.mapped_column(sa.ForeignKey('criterion.id'))

    class Alternative(db.Model):
        id: so.Mapped[int] = so.mapped_column(primary_key=True)
        name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
        description: so.Mapped[str | None] = so.mapped_column(sa.String(256))

    # class Evaluation(db.Model):
    #     id: so.Mapped[int] = so.mapped_column(primary_key=True)
    #     criterion_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('criterion.id'))
    #     alternative_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('alternative.id'))
    #     score: so.Mapped[float] = so.mapped_column()  # Оценка альтернативы по критерию

    def __repr__(self):
        return '<User {}>'.format(self.username)