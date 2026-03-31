import os

from selene import browser, have, command


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
        browser.driver.execute_script("document.querySelector('footer')?.remove()")
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

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birth_date(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(str(year))
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobby(self, value):
        browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text(value)).click()
        return self

    def fill_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(f'resources/{file_name}')
        )
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_registered(self, *rows):
        table = browser.element('.table-responsive')
        for key, value in rows:
            table.element(f'//td[text()="{key}"]/following-sibling::td').should(
                have.exact_text(value)
            )