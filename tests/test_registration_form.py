from qa_guru_python_18_9.pages.registration_page import RegistrationPage


def test_fill_registration_form_with_mandatory_values():
    registration_page = RegistrationPage()
    (registration_page.open()
     .fill_first_name('my_firstName')
     .fill_last_name('my_secondName')
     .set_male_gender()
     .fill_mobile_number('8999123456')
     .fill_date_of_birth(2013, 'June', 21)
     .click_submit_button()
     .should_have_text('Thanks for submitting the form')
     .should_have_registered('my_firstName', 'my_secondName', '', 'Male', '8999123456', '21 June,2013', '', '', '', '',
                             '', '')
     .click_close_button()
     .should_be_blank('firstName'))


def test_send_registration_form_with_all_values():
    registration_page = RegistrationPage()
    (registration_page.open()
     .fill_first_name('my_firstName')
     .fill_last_name('my_secondName')
     .fill_email('my_email@mail.com')
     .set_male_gender()
     .fill_mobile_number('8999123456')
     .fill_date_of_birth(2013, 'June', 21)
     .fill_subject('Hindi')
     .fill_subject('Maths')
     .set_sport_hobbie()
     .set_upload_picture('resources/python.png')
     .fill_current_address('my_curr_address')
     .fill_state('NCR')
     .fill_city('Delhi')
     .click_submit_button()
     .should_have_text('Thanks for submitting the form')
     .should_have_registered('my_firstName', 'my_secondName', 'my_email@mail.com', 'Male', '8999123456', '21 June,2013',
                             'Hindi, Maths', 'Sports', 'python.png', 'my_curr_address', 'NCR', 'Delhi')
     .click_close_button()
     .should_be_blank('firstName'))


def test_send_empty_registration_form():
    registration_page = RegistrationPage()
    (registration_page.open()
     .should_be_blank('firstName')
     .click_submit_button()
     .should_have_no_text('Thanks for submitting the form'))
