import os.path
from os import path, chdir, getcwd
from selene.support.shared import browser
from selene import have, command


res_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'resources/test_image.png'))


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Egor')
    browser.element('#lastName').type('Egorov')
    browser.element('#userEmail').type('egor@oz.ru')
    browser.all('.custom-radio').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('1111111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{1999}"]').click()
    browser.element('.react-datepicker__month-select').element(f'[value="{5}"]').click()
    browser.element('.react-datepicker__day--003').click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(res_dir)
    browser.element('#currentAddress').type('Ukraine')
    browser.element('#state').element('input').type('Haryana').press_enter()
    browser.element('#city').element('input').type('Karnal').press_enter()
    browser.element('#submit').perform(command.js.click)

    browser.all(".modal-dialog").all("table tr")[1].all("td").should(have.exact_texts('Student Name', 'Egor Egorov'))
    browser.all(".modal-dialog").all("table tr")[2].all("td").should(have.exact_texts('Student Email', 'egor@oz.ru'))
    browser.all(".modal-dialog").all("table tr")[3].all("td").should(have.exact_texts('Gender', 'Female'))
    browser.all(".modal-dialog").all("table tr")[4].all("td").should(have.exact_texts('Mobile', '1111111111'))
    browser.all(".modal-dialog").all("table tr")[5].all("td").should(have.exact_texts('Date of Birth', '03 June,1999'))
    browser.all(".modal-dialog").all("table tr")[6].all("td").should(have.exact_texts('Subjects', 'Physics'))
    browser.all(".modal-dialog").all("table tr")[7].all("td").should(have.exact_texts('Hobbies', 'Sports'))
    browser.all(".modal-dialog").all("table tr")[8].all("td").should(have.exact_texts('Picture', 'test_image.png'))
    browser.all(".modal-dialog").all("table tr")[9].all("td").should(have.exact_texts('Address', 'Ukraine'))
    browser.all(".modal-dialog").all("table tr")[10].all("td").should(have.exact_texts('State and City',
                                                                                       'Haryana Karnal'))

