from pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.have_title('DEMOQA')

    registration_page.fill_first_name('Aleksandr')
    registration_page.fill_last_name('Shevchenko')
    registration_page.fill_email('a.shevchenko666@mail.com')
    registration_page.fill_gender('Male')
    registration_page.fill_phone_number('8005553535')
    registration_page.fill_birthday('24', 'December', '1995')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Music')
    registration_page.upload_file('image_1.jpg')
    registration_page.fill_current_address('SPB Russia')
    registration_page.fill_state_and_city('Haryana', 'Karnal')

    registration_page.submit_form()

    registration_page.should_have_registered(
        ('Student Name', 'Aleksandr Shevchenko'),
        ('Student Email', 'a.shevchenko666@mail.com'),
        ('Gender', 'Male'),
        ('Mobile', '8005553535'),
        ('Date of Birth', '24 December,1995'),
        ('Subjects', 'Computer Science'),
        ('Hobbies', 'Music'),
        ('Picture', 'image_1.jpg'),
        ('Address', 'SPB Russia'),
        ('State and City', 'Haryana Karnal')
    )
    registration_page.close_submit_form()
