import secrets
import uuid

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query

femail = 'cea'
fphone = 'eca'
fpassword = 'ceb'
engine = create_engine('postgresql://server:24030dan@localhost/meal_app', echo=True) # <- настройки и логин в бд
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Userbase(Base):
    __tablename__ = 'registered_users'
    uid = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)

    def __init__(self, uid, email, phone, password):
        self.uid = uid
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f'<{self.__class__.__name__} #{self.uid}#{self.email}#{self.phone}#{self.password}>'


# ruid = secrets.token_urlsafe(10) <- если uuid4 не сработает.


def fill_data():
    with Session() as session:
        insertion = Userbase(f'{uuid.uuid4()}', f'{femail}', f'{fphone}', f'{fpassword}')
        session.add(insertion)
        session.commit()


def main():
    fill_data()


if __name__ == '__main__':
    main()
#Base.metadata.create_all(engine) - создать Базу данных
