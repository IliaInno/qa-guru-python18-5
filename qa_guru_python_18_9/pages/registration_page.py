import os

from selene import browser, be, have


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#gender-radio-1 + .custom-control-label')
        self.user_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')
        self.day = browser.element('.react-datepicker__day--021')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbies-checkbox-1 + .custom-control-label')
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#currentAddress')
        self.city = browser.element('#currentAddress')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_male_gender(self):
        browser.element('#gender-radio-1 + .custom-control-label').click()
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def set_sport_hobbie(self):
        browser.element('#hobbies-checkbox-1 + .custom-control-label').click()
        return self

    def set_upload_picture(self, value):
        browser.element('#uploadPicture').type(os.path.abspath(value))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()
        return self

    def should_have_registered(self, first_name, last_name, email, gender, phone_number, date_of_birth, subject,
                               hobbie, picture, address, state, city):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{first_name} {last_name}', email, gender, phone_number, date_of_birth,
            subject, hobbie, picture, address, f'{state} {city}'.strip()))
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
