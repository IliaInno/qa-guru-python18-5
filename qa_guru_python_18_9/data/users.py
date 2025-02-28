import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    year: int
    month: str
    day: int
    subject: str
    picture: str
    address: str
    state: str
    city: str


user_with_all_values = User(first_name='my_firstName', last_name='my_secondName', email='my_email@mail.com',
                            phone_number='8999123456', year=2013, month='June',
                            day=21, subject='Hindi', picture='resources/python.png', address='my_curr_address', state='NCR',
                            city='Delhi')

user_with_mandatory_values = User(first_name='my_firstName', last_name='my_secondName', email='',
                                  phone_number='8999123456', year=2013, month='June',
                                  day=21, subject='', picture='', address='', state='',
                                  city='')