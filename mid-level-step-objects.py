from tests.test_student_registration import registration_page

registration_page.open()
registration_page.fill_first_name(...)
registration_page.fill_last_name(...)
...
registration_page.submit()
registration_page.should_have_registered(...)