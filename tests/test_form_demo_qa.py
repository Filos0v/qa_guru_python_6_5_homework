from selene import browser, have
import os


def test_form_demo_qa():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Aleksandr')
    browser.element('#lastName').type('Shevchenko')
    browser.element('#userEmail').type('a.shevchenko666@mail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8005553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().type('December').click()
    browser.element('[class="react-datepicker__year-select"]').click().type('1995').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--024 react-datepicker__day--weekend"]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/image_1.jpg'))
    browser.element('#currentAddress').type('SPB Russia')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Aleksandr Shevchenko'))
    browser.element('.modal-body').should(have.text('a.shevchenko666@mail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('8005553535'))
    browser.element('.modal-body').should(have.text('24 December,1995'))
    browser.element('.modal-body').should(have.text('Computer Science'))
    browser.element('.modal-body').should(have.text('Music'))
    browser.element('.modal-body').should(have.text('image_1.jpg'))
    browser.element('.modal-body').should(have.text('SPB Russia'))
    browser.element('.modal-body').should(have.text('Haryana Karnal'))
