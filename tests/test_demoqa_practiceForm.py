from selene.support.shared import browser
from selene import have, be


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))

