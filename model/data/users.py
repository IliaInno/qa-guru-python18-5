import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year: str
    month: str
    day: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='my_firstName', last_name='my_secondName', email='my_email@mail.com',
            gender='Male', phone_number='8999123456', year='2013', month='June', day='21',
            subject='Hindi',
            hobby='Sports', picture='python.png', address='my_curr_address', state='NCR',
            city='Delhi')