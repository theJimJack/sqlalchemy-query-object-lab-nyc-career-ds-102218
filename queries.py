from sqlalchemy import create_engine, func
from seed import Company
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def return_apple():
    return session.query(Company).filter(Company.company=="Apple").first()

def return_disneys_industry():
    disney = session.query(Company).filter(Company.company=="Walt Disney").first()
    return disney.industry

def return_list_of_company_objects_ordered_alphabetically_by_symbol():
    return session.query(Company).order_by(Company.symbol).all()

def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending():
    tech = session.query(Company).filter_by(industry="Technology").order_by(Company.enterprise_value.desc()))
    list = []
    for c in tech:
        obj = {'company':c.company,'EV':c.enterprise_value}
        list.append(obj)
    return list
    
def return_list_of_consumer_products_companies_with_EV_above_225():
    pass

def return_conglomerates_and_pharmaceutical_companies():
    pass

def avg_EV_of_dow_companies():
    pass

def return_industry_and_its_total_EV():
    pass
