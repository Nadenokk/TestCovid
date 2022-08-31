# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
import sys
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class NewTablet(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_new_tablet(self):
        driver = self.driver
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()

        # Копируем номер штрихкода
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(12) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск штрих-кодов\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"filtersform:j_idt87").click()
        time.sleep(25)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = \
            driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text
        #планшеты
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a > div > div.layout-tabmenu-tooltip-text").click()
        #driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.ID,"j_idt78").click()
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").send_keys("01.11.2021 10:10")
        time.sleep(2)
        #driver.find_element(By.ID,"itemForm:tabView:compileDate_input").send_keys("01.11.2021 10:10")
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:patientCategories_panel").click()
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-icon-left.ui-icon.ui-c.fa.fa-ellipsis-h").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(3)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        #проба
        driver.find_element(By.XPATH,
            "//ul[@class='ui-tabs-nav ui-helper-reset ui-widget-header ui-corner-all']").click()
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()

        driver.find_element(By.ID,"itemForm:tabView:j_idt115").click()
        driver.find_element(By.ID,"addByBarcodeForm:j_idt348").send_keys(barcode+Keys.ENTER)
        time.sleep(12)
        driver.find_element(By.CSS_SELECTOR,"span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-labContractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(4)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        #driver.find_element(By.CSS_SELECTOR,
        #    "#covidResearchForm\:tabView\:covid-researches-materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-materialType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-materialType_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-materialType_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-materialDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-materialDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-materialDate_input").send_keys("21.02.2021 10:00")
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-lastName").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-lastName").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-lastName").send_keys(u"СаблинАнтител")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-firstName").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-firstName").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-firstName").send_keys(u"Роман")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patronymicName").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patronymicName").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patronymicName").send_keys(u"Евгеньевич")
        driver.find_element(By.CSS_SELECTOR,
            "#covidResearchForm\:tabView\:covid-researches-sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-birthDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-birthDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-birthDate_input").send_keys("11.02.1999")
        #for date in "08911111":
        #    driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        #driver.find_element(By.ID,"covidResearchForm:tabView:j_id150_content").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-email").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-email").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-phone").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-phone").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-phone").send_keys("89546521456")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-snils").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-snils").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-snils").send_keys("78945212399")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsSeria").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsSeria").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsSeria").send_keys("745631")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsNumber").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsNumber").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-polisOmsNumber").send_keys("147856")
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-identityDocType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-identityDocType_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocType_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocSeries").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocSeries").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocSeries").send_keys("4598")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocNumber").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocNumber").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocNumber").send_keys("789456")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedBy").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedBy").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedBy").send_keys(u"ОУФМС")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-identityDocIssuedDate_input").send_keys("11.11.2015")
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-addressType_label").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-addressType_label").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-addressType_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-country_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-country_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-country_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-region_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-region_items").click()
        #time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-region_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-city_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-city_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-city_input").send_keys(u"Ярославь"+Keys.TAB)
        #time.sleep(1)
        #driver.find_element(By.XPATH,"//span[@id='covidResearchForm:tabView:covid-researches-city_panel']/ul[1]/li[1]/span").click()
        #driver.find_element(By.CSS_SELECTOR,"span.ui-autocomplete-query").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStreet_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStreet_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressBuilding_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressBuilding_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressBuilding_input").send_keys("1")
        time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressFlat").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressFlat").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressFlat").send_keys("18")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStringValue").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStringValue").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-homeAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-tempAddressStringValue").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-tempAddressStringValue").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-tempAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-homeCityArea_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-homeCityArea_items").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-homeCityArea_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-orgName").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-orgName").send_keys(u"Институт")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPositionStringValue").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPositionStringValue").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPositionStringValue").send_keys(u"Студент")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPhone").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPhone").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workPhone").send_keys("84561237458")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressCountry_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-workAddressCountry_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressCountry_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressRegion_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-workAddressRegion_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressRegion_1").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressCity_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressCity_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressCity_input").send_keys(u"Ярославль"+Keys.TAB)
        #driver.find_element(By.XPATH,"//span[@id='covidResearchForm:tabView:covid-researches-workAddressCity_panel']/ul/li/span").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStreet_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStreet_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStreet_input").send_keys(u"Мира")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressBuilding_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressBuilding_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressFlat").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressFlat").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressFlat").send_keys("5")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStringValue").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStringValue").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-workAddressStringValue").send_keys(u"Ярославль, Мира 24 - 5")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientCategory").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientCategory_label").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientCategory_2").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-receiptInstitution_label").click()
        driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-receiptInstitution_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-receiptInstitution_3").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-sender").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-sender").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-sender").send_keys(u"Иванов И.И.")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-sendInstitution_selectBtn").click()
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
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-arrivalDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-arrivalDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-arrivalDate_input").send_keys("20.11.2020")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-departureCountry").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-departureCountry_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#covidResearchForm\:tabView\:covid-researches-departureCountry_items").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-departureCountry_2").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-flightNumber").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-flightNumber").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-flightNumber").send_keys(u"74ке")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-epidNumber").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-epidNumber").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-epidNumber").send_keys(u"78-41в")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-simptomsDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-simptomsDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-simptomsDate_input").send_keys("15.02.2021")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-medicalAidDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-medicalAidDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-medicalAidDate_input").send_keys("16.02.2021")
        driver.find_element(By.CSS_SELECTOR,
            "#covidResearchForm\:tabView\:covid-researches-medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#covidResearchForm\:tabView\:covid-researches-medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-complicationStringValue").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-complicationStringValue").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-complicationStringValue").send_keys(u"Нет")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-hospitalDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-hospitalDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-hospitalDate_input").send_keys("17.02.2021")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-terapy").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-terapy").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-terapy").send_keys(u"Нет")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").send_keys("22.02.2021 8:52")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-description").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-description").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-description").send_keys(u"Нет")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsCount").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsCount").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsCount").send_keys("2")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsFullName").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsFullName").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsFullName").send_keys(u"Иванов, Петров")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsPhone").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsPhone").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-patientContactsPhone").send_keys("87456911265")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").click()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").clear()
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-issueDate_input").send_keys("22.02.2021 8:52")
        driver.find_element(By.ID,"covidResearchForm:tabView:covid-researches-terapy").click()
        #driver.find_element(By.CSS_SELECTOR,"body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        #time.sleep(2)
        driver.find_element(By.ID,"covidResearchForm:j_idt612").click()
        time.sleep(20)

        driver.find_element(By.ID,"itemForm:j_id4").click()

        time.sleep(2)

        driver.find_element(By.ID,"j_idt78")

if __name__ == "__main__":
    unittest.main()






