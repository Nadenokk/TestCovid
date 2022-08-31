# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreateOKI3(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_OKI3(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(10) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Создание заявки на исследование 2\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"#buttonsForm\:createOki3").click()

        driver.find_element(By.CSS_SELECTOR,"span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:labContractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id15").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id15").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id15").send_keys(u"един")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        # driver.find_element(By.CSS_SELECTOR,
        #    "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        #driver.find_element(By.CSS_SELECTOR,
        #    "#itemForm\:tabView\:materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"itemForm:tabView:materialType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:materialType_items").click()
        driver.find_element(By.ID,"itemForm:tabView:materialType_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:materialDate_input").send_keys("21.02.2021 10:00")
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").clear()
        driver.find_element(By.ID,"itemForm:tabView:lastName").send_keys(u"СаблинАнтител")
        driver.find_element(By.ID,"itemForm:tabView:firstName").click()
        driver.find_element(By.ID,"itemForm:tabView:firstName").clear()
        driver.find_element(By.ID,"itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").click()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").clear()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:birthDate_input").send_keys("08.08.1999")
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:email").click()
        driver.find_element(By.ID,"itemForm:tabView:email").clear()
        driver.find_element(By.ID,"itemForm:tabView:email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.ID,"itemForm:tabView:phone").click()
        driver.find_element(By.ID,"itemForm:tabView:phone").clear()
        driver.find_element(By.ID,"itemForm:tabView:phone").send_keys("89546521456")
        driver.find_element(By.ID,"itemForm:tabView:snils").click()
        driver.find_element(By.ID,"itemForm:tabView:snils").clear()
        driver.find_element(By.ID,"itemForm:tabView:snils").send_keys("78945212399")
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").click()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").clear()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsSeria").send_keys("745631")
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:polisOmsNumber").send_keys("147856")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:identityDocType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:identityDocType_items").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocType_1").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocSeries").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocSeries").clear()
        driver.find_element(By.ID,"itemForm:tabView:identityDocSeries").send_keys("4598")
        driver.find_element(By.ID,"itemForm:tabView:identityDocNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:identityDocNumber").send_keys("789456")
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedBy").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedBy").clear()
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedBy").send_keys(u"ОУФМС")
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:identityDocIssuedDate_input").send_keys("11.11.2015")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:addressType_label").click()
        driver.find_element(By.ID,"itemForm:tabView:addressType_label").click()
        driver.find_element(By.ID,"itemForm:tabView:addressType_1").click()
        driver.find_element(By.ID,"itemForm:tabView:country_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:country_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:country_1").click()
        driver.find_element(By.ID,"itemForm:tabView:region_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:region_items").click()
        #time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:region_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:city_input").click()
        driver.find_element(By.ID,"itemForm:tabView:city_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:city_input").send_keys(u"Ярославль"+Keys.TAB)
        #driver.find_element(By.XPATH,"//span[@id='itemForm:tabView:city_panel']/ul[1]/li[1]/span").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressBuilding_input").send_keys("1")
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressFlat").send_keys("18")
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStringValue").click()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStringValue").clear()
        driver.find_element(By.ID,"itemForm:tabView:homeAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element(By.ID,"itemForm:tabView:tempAddressStringValue").click()
        driver.find_element(By.ID,"itemForm:tabView:tempAddressStringValue").clear()
        driver.find_element(By.ID,"itemForm:tabView:tempAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:homeCityArea_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:homeCityArea_items").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:homeCityArea_1").click()
        driver.find_element(By.ID,"itemForm:tabView:orgName").clear()
        driver.find_element(By.ID,"itemForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element(By.ID,"itemForm:tabView:workPositionStringValue").click()
        driver.find_element(By.ID,"itemForm:tabView:workPositionStringValue").clear()
        driver.find_element(By.ID,"itemForm:tabView:workPositionStringValue").send_keys(u"Студент")
        driver.find_element(By.ID,"itemForm:tabView:workPhone").click()
        driver.find_element(By.ID,"itemForm:tabView:workPhone").clear()
        driver.find_element(By.ID,"itemForm:tabView:workPhone").send_keys("84561237458")
        driver.find_element(By.ID,"itemForm:tabView:workAddressCountry_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:workAddressCountry_items").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressCountry_1").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressRegion_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:workAddressRegion_items").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressRegion_1").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressCity_input").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressCity_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressCity_input").send_keys(u"Ярославль"+Keys.TAB)
        #driver.find_element(By.XPATH,"//span[@id='itemForm:tabView:workAddressCity_panel']/ul/li/span").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:workAddressFlat").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressFlat").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressFlat").send_keys("5")
        driver.find_element(By.ID,"itemForm:tabView:workAddressStringValue").click()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStringValue").clear()
        driver.find_element(By.ID,"itemForm:tabView:workAddressStringValue").send_keys(u"Ярославль, Мира 24 - 5")
        driver.find_element(By.ID,"itemForm:tabView:patientCategory").click()
        driver.find_element(By.ID,"itemForm:tabView:patientCategory_label").click()
        driver.find_element(By.ID,"itemForm:tabView:patientCategory_2").click()
        driver.find_element(By.ID,"itemForm:tabView:receiptInstitution_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:receiptInstitution_items").click()
        driver.find_element(By.ID,"itemForm:tabView:receiptInstitution_3").click()
        driver.find_element(By.ID,"itemForm:tabView:sender").click()
        driver.find_element(By.ID,"itemForm:tabView:sender").clear()
        driver.find_element(By.ID,"itemForm:tabView:sender").send_keys(u"Иванов И.И.")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:sendInstitution_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id10").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id10").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id10").send_keys(u"сбер")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:arrivalDate_input").send_keys("20.11.2020")
        driver.find_element(By.ID,"itemForm:tabView:departureCountry").click()
        driver.find_element(By.ID,"itemForm:tabView:departureCountry_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element(By.ID,"itemForm:tabView:departureCountry_2").click()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:flightNumber").send_keys(u"74ке")
        driver.find_element(By.ID,"itemForm:tabView:epidNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:epidNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:epidNumber").send_keys(u"78-41в")
        driver.find_element(By.ID,"itemForm:tabView:simptomsDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:simptomsDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:simptomsDate_input").send_keys("15.02.2021")
        driver.find_element(By.ID,"itemForm:tabView:medicalAidDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:medicalAidDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:medicalAidDate_input").send_keys("16.02.2021")
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"itemForm:tabView:complicationStringValue").click()
        driver.find_element(By.ID,"itemForm:tabView:complicationStringValue").clear()
        driver.find_element(By.ID,"itemForm:tabView:complicationStringValue").send_keys(u"Нет")
        driver.find_element(By.ID,"itemForm:tabView:hospitalDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:hospitalDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:hospitalDate_input").send_keys("17.02.2021")
        driver.find_element(By.ID,"itemForm:tabView:terapy").click()
        driver.find_element(By.ID,"itemForm:tabView:terapy").clear()
        driver.find_element(By.ID,"itemForm:tabView:terapy").send_keys(u"Нет")
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").send_keys("22.02.2021")
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys(u"Нет")
        driver.find_element(By.ID,"itemForm:tabView:patientContactsCount").click()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsCount").clear()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsCount").send_keys("2")
        driver.find_element(By.ID,"itemForm:tabView:patientContactsFullName").click()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsFullName").clear()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsFullName").send_keys(u"Иванов, Петров")
        driver.find_element(By.ID,"itemForm:tabView:patientContactsPhone").click()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsPhone").clear()
        driver.find_element(By.ID,"itemForm:tabView:patientContactsPhone").send_keys("87456911265")
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:issueDate_input").send_keys("22.02.2021 8:52")
        driver.find_element(By.ID,"itemForm:tabView:terapy").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id5").click()
        driver.find_element(By.CSS_SELECTOR,"div > div > div.ui-growl-message > p")
        time.sleep(5)

        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='3']").click()

        driver.find_element(By.ID,"itemForm:tabView:rotavirusRnaResult").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:rotavirusRnaResult_label").click()
        driver.find_element(By.ID,"itemForm:tabView:rotavirusRnaResult_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:noravirusRnaResult").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:noravirusRnaResult_label").click()
        driver.find_element(By.ID,"itemForm:tabView:noravirusRnaResult_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:astrovirusRnaResult").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:astrovirusRnaResult_label").click()
        driver.find_element(By.ID,"itemForm:tabView:astrovirusRnaResult_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:adenovirusDnaResult").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:adenovirusDnaResult_label").click()
        driver.find_element(By.ID,"itemForm:tabView:adenovirusDnaResult_2").click()
        time.sleep(2)

        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#buttonsForm\:createOki3")


if __name__ == "__main__":
    unittest.main()