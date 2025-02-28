import os

from selene import browser, be, have

from qa_guru_python_18_9.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#gender-radio-1 + .custom-control-label')
        self.phone_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')
        self.day = browser.element('.react-datepicker__day--021')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbies-checkbox-1 + .custom-control-label')
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#state')
        self.city = browser.element('#city')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def set_male_gender(self):
        self.gender.click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.year.type(year)
        self.month.type(month)
        self.day.click()
        return self

    def fill_subject(self, value):
        self.subjects_input.type(value).press_enter()
        return self

    def set_sport_hobbie(self):
        self.hobbies.click()
        return self

    def set_upload_picture(self, value):
        self.upload_picture.type(os.path.abspath(value))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def fill_state(self, value):
        self.state.click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        self.city.click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()
        return self

    def should_have_registered(self, user: User):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}', user.email, 'Male', user.phone_number, user.year, user.month,
            user.day, user.subject, 'Sports', user.picture, user.address, f'{user.state} {user.city}'.strip()))
        return self

    def click_close_button(self):
        browser.element('#closeLargeModal').should(be.visible).click()
        return self

    def should_be_blank(self, value):
        browser.element(f'#{value}').should(be.blank)
        return self

    def should_have_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))
        return self

    def should_have_no_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should((have.no.text(value)))
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.set_male_gender()
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.year, user.month, user.day)
        self.fill_subject(user.subject)
        self.set_sport_hobbie()
        self.set_upload_picture(user.picture)
        self.fill_current_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.click_submit_button()
        return self
