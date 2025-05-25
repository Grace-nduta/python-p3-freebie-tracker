#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Sessionmaker = sessionmaker(bind=engine)
session = Sessionmaker()

# Companies
Company1 = Company(name="Cropnuts", founding_year=2015)
Company2 = Company(name="World plastics", founding_year=2020)
Company3 = Company(name="Kilimall", founding_year=2012)
Company4 = Company(name="Jumia", founding_year=2010)
Company5 = Company(name="Safaricom", founding_year=2000)

# Devs
Dev1 = Dev(name="John Jason")
Dev2 = Dev(name="Jay Nelson")
Dev3 = Dev(name="Yang Tao")
Dev4 = Dev(name="Vinod Goel")
Dev5 = Dev(name="Vadafone")

# Freebies
Freebie1 = Freebie(item_name="Soil_testing", value=10, company=Company1, dev=Dev1)
Freebie2 = Freebie(item_name="Plastic_bags", value=5, company=Company2, dev=Dev2)
Freebie3 = Freebie(item_name="Phone_covers", value=15, company=Company3, dev=Dev3)
Freebie4 = Freebie(item_name="Food_delivery", value=20, company=Company4, dev=Dev4)
Freebie5 = Freebie(item_name="Data_bundle", value=30, company=Company5, dev=Dev5)

# Delete existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Add new data
session.add_all([Company1, Company2, Company3, Company4, Company5, Dev1, Dev2, Dev3, Dev4, Dev5,
                 Freebie1, Freebie2, Freebie3, Freebie4, Freebie5])

# Commit the session
session.commit()
#python seed.py
print("Database seeded successfully!")

# Run this in the terminal
# python debug.py

# Freebie Tests
# freebie = session.query(Freebie).first()
# print(freebie) This will print the first Freebie object
# print(freebie.company) This will print the associated Company object
# print(freebie.dev) This will print the associated Dev object

# Dev Tests
# dev = session.query(Dev).first()
# print(dev) This will print the first Dev object
# print(dev.companies) This will print a list of associated Company objects
# print(dev.freebies) This will print a list of associated Freebie objects

# Company Tests
# company = session.query(Company).first()
# print(company) This will print the first Company object
# print(company.devs) This will print a list of associated Dev objects
# print(company.freebies) This will print a list of associated Freebie objects




