from pages.registration_page import RegistrationPage


registration_page = RegistrationPage()


def test_student_registration():
    (
        registration_page
        .open()
        .fill_first_name('Leonid')
        .fill_last_name('Chaliy')
        .fill_email('leonid@example.com')
        .fill_gender('Male')
        .fill_phone_number('1234567890')
        .fill_birth_date('28', 'August', 2004)
        .fill_subject('Maths')
        .fill_hobby('Sports')
        .fill_picture('avatar.png')
        .fill_current_address('Moscow')
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit()
    )

    registration_page.should_have_registered(
        ('Student Name', 'Leonid Chaliy'),
        ('Student Email', 'leonid@example.com'),
        ('Gender', 'Male'),
        ('Mobile', '1234567890'),
        ('Date of Birth', '28 August,2004'),
        ('Subjects', 'Maths'),
        ('Hobbies', 'Sports'),
        ('Picture', 'avatar.png'),
        ('Address', 'Moscow'),
        ('State and City', 'NCR Delhi'),
    )