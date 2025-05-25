from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    
    freebies = relationship('Freebie', backref='company')

    def __repr__(self):
        return f'<Company {self.name}>'
    @property
    def devs(self):
        return [freebie.dev for freebie in self.freebies if freebie.dev is not None]

    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name=item_name, value=value, company=self, dev=dev)
    
    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()   

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'  
    @property
    def companies(self):
        return [freebie.company for freebie in self.freebies if freebie.company is not None]
    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            return True
        return False
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    def __repr__(self):
        return f'<Freebie {self.item_name}  (${self.value})>'  

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
