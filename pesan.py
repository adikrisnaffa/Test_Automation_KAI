from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui
import pytest

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.kai.id/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.pesan_tiket
def test_pesan_tiket(context):
    stasiun_asal = context.find_element(By.ID, 'select2-origination2-container')
    stasiun_asal.click()
    time.sleep(5)
    pyautogui.typewrite('Pasar Senen')
    pyautogui.press('enter')

    stasiun_tujuan = context.find_element(By.ID, 'select2-destination2-container')
    stasiun_tujuan.click()
    time.sleep(5)
    pyautogui.typewrite('lempuyangan (LPN)')
    pyautogui.press('enter')

    tanggal = context.find_element(By.ID, 'departure_dateh2')
    tanggal.click()
    next_date_1 = context.find_element(By.XPATH, '//a[@data-handler="next"]')
    next_date_1.click()
    time.sleep(1)


    select_date = context.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]/a')
    select_date.click()
    time.sleep(1)

    select2_adult2_container = context.find_element(By.ID, 'select2-adult2-container')
    select2_adult2_container.click()
    time.sleep(1)
    input_adult = context.find_element(By.CLASS_NAME, 'select2-search__field')
    input_adult.send_keys('1 Dewasa')
    input_adult.send_keys(Keys.ENTER)
    time.sleep(1)

    pesan = context.find_element(By.ID, 'submittrain')
    pesan.click()
    time.sleep(5)

    cari_tiket = context.find_element(By.XPATH, "//div[contains(text(), 'Rp 220.000,-')]")
    cari_tiket.click()
    time.sleep(10)

    pesan_tanpa_daftar =  context.find_element(By.XPATH, "//button[contains(text(), 'Pesan Tanpa Daftar')]")
    pesan_tanpa_daftar.click()
    time.sleep(5)
    pemesan = Select(context.find_element(By.ID, 'pemesan_title'))
    pemesan.select_by_value('MR')

    nama_pemesan = context.find_element(By.ID, 'pemesan_nama')
    nama_pemesan.send_keys('...................')

    id_pemesan = context.find_element(By.ID, 'pemesan_notandapengenal')
    id_pemesan.send_keys('...................')

    no_pemesan = context.find_element(By.ID, 'pemesan_nohp')
    no_pemesan.send_keys('...................')

    email_pemesan = context.find_element(By.ID, 'pemesan_email')
    email_pemesan.send_keys('...................')

    alamat_pemesan = context.find_element(By.ID, 'pemesan_alamat')
    alamat_pemesan.send_keys('Tangerang Selatan')

    check_box = context.find_element(By.ID, 'cbCopy')
    check_box.click()

    syarat_dan_ketentuan = context.find_element(By.ID, 'setuju')
    syarat_dan_ketentuan.click()

    time.sleep(5)