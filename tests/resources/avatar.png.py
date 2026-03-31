import os

from selene import browser


def fill_picture(self, file_name):
    browser.element('#uploadPicture').send_keys(
        os.path.abspath(f'resources/{file_name}')
    )
    return self