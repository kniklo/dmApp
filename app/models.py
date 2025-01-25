from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Criterion(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    weight: so.Mapped[float] = so.mapped_column(default=0.0)
    description: so.Mapped[str | None] = so.mapped_column(sa.String(256))
    #parent_id: so.Mapped[int | None] = so.mapped_column(sa.ForeignKey(Criterion.id)),
#                                                index=True)


class Alternative(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    description: so.Mapped[str | None] = so.mapped_column(sa.String(256))

# class Evaluation(db.Model):
#     id: so.Mapped[int] = so.mapped_column(primary_key=True)
#     criterion_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Criterion.id),
#                                                index=True)
#     alternative_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Alternative.id),
#                                                index=True)
#     score: so.Mapped[float] = so.mapped_column()  # Оценка альтернативы по критерию
