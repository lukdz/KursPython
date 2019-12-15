import sqlite3

db = sqlite3.connect(':memory:')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
Base = declarative_base()
from sqlalchemy.orm import relationship


class Osoba(Base):
    tablename = 'Osoba'
    id = Column(Integer, primary_key=True)
    imie = Column(String(20), nullable=False)
    wiek = Column(Integer, default=18)
    # created = Column(DateTime, server_default=func.now())
    adresy = relationship('Adres')

class Adres(Base):
    __tablename__ = 'Adresy'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    miasto = Column(String)
    mieszkaniec = Column(Integer, ForeignKey("Osoba.id"))


from sqlalchemy import create_engine
engine = create_engine('sqlite:///wyklad.db', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///wyklad.db', echo=True)
Session = sessionmaker(bind=engine)
sesja = Session()

o = Osoba(imie='Debeściak')
adr1 = Adres(email='Joliot@Curie', miasto='Wrocław')
o.adresy = [adr1]
sesja.add(o)
sesja.add(adr1)
sesja.commit()