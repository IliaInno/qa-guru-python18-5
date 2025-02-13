from selene import browser, have, be


def test_fill_registration_form_with_mandatory_values():
    browser.open('/')
    browser.element('#firstName').should(be.blank)

    browser.element('#firstName').type('my_firstName')
    browser.element('#lastName').type('my_secondName')
    browser.element('#gender-radio-1 + .custom-control-label').click()
    browser.element('#userNumber').type('8999123456')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2013"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="5"]').click()
    browser.element('.react-datepicker__day--021').click()

    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(have.texts(
        'my_firstName my_secondName', '', 'Male', '8999123456', '21 June,2013', '', '', '', '', ''))

    browser.element('#closeLargeModal').should(be.visible).click()
    browser.element('#firstName').should(be.blank)


def test_send_registration_form_with_all_values():
    browser.open('/')
    browser.element('#firstName').should(be.blank)

    browser.element('#firstName').type('my_firstName')
    browser.element('#lastName').type('my_secondName')
    browser.element('#userEmail').type('my_email@mail.com')
    browser.element('#gender-radio-1 + .custom-control-label').click()
    browser.element('#userNumber').type('8999123456')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2013"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="5"]').click()
    browser.element('.react-datepicker__day--021').click()

    browser.element('#subjectsInput').type('hindi').press_enter().type('maths').press_enter()
    browser.element('#hobbies-checkbox-1 + .custom-control-label').click()
    browser.element('#currentAddress').type('my_curr_address')

    browser.element('#state').click().all("#state div").element_by(have.exact_text("Uttar Pradesh")).click()
    browser.element('#city').click().all("#city div").element_by(have.exact_text("Merrut")).click()

    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(have.texts(
        'my_firstName my_secondName', 'my_email@mail.com', 'Male', '8999123456', '21 June,2013',
        'Hindi, Maths', '', '', 'my_curr_address', 'Uttar Pradesh Merrut'))
    browser.element('#closeLargeModal').should(be.visible).click()
    browser.element('#firstName').should(be.blank)


def test_send_empty_registration_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank)
    browser.element('#submit').should(be.visible).click()
    browser.element('#example-modal-sizes-title-lg').should((have.no.text('Thanks for submitting the form')))
