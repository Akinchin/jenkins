
import allure
import os

import pytest
from selene import browser, have, be, by

@allure.title("Successful fill form demoqa")
def test_demoqa():
    with allure.step("Open form"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
    with allure.step("Data entry"):
        browser.element('input[placeholder="First Name"]').type('vasya')
        browser.element('input[placeholder="Last Name"]').type('ivanov')
        browser.element('input[placeholder="name@example.com"]').type('pupalupa@mail.ru')
        browser.element('label[for="gender-radio-1"]').click()
        browser.element('input[placeholder="Mobile Number"]').type('9099099090')
        browser.element('input[id="dateOfBirthInput"]').click()
        browser.element('select[class="react-datepicker__year-select"]').click()
        browser.element('option[value="1992"]').click()
        browser.element('select[class="react-datepicker__month-select"]').click()
        browser.element('option[value="5"]').click()
        browser.element('div[class="react-datepicker__day react-datepicker__day--012"]').click()
        browser.element('input[id="subjectsInput"]').type('Maths').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('textarea[placeholder="Current Address"]').type('Санкт-Петербург')
        browser.element('#state').click().element(by.text('NCR')).click()
        browser.element('#city').click().element(by.text('Delhi')).click()
        browser.element('#submit').click()
    with allure.step("Cheking table"):
        browser.element('.table').should(have.text('vasya ivanov'))
        browser.element('.table').should(have.text('pupalupa@mail.ru'))
        browser.element('.table').should(have.text('Male'))
        browser.element('.table').should(have.text('9099099090'))
        browser.element('.table').should(have.text('12 June,1992'))
        browser.element('.table').should(have.text('Maths'))
        browser.element('.table').should(have.text('Sports'))
        browser.element('.table').should(have.text('Санкт-Петербург'))
        browser.element('.table').should(have.text('NCR Delhi'))

    browser.quit()
