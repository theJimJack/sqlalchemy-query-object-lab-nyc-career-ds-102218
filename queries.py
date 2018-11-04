from sqlalchemy import create_engine, func
from seed import Company
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def return_apple():
    return session.query(Company).filter(Company.symbol=="AAPL")

def return_disneys_industry():
    pass

def return_list_of_company_objects_ordered_alphabetically_by_symbol():
    pass

def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending():
    pass

def return_list_of_consumer_products_companies_with_EV_above_225():
    pass

def return_conglomerates_and_pharmaceutical_companies():
    pass

def avg_EV_of_dow_companies():
    pass

def return_industry_and_its_total_EV():
    pass
