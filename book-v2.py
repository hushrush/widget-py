import  selenium
from selenium import webdriver
import time
import sys
import logging


def book():
    bookTime = sys.argv[1]
    index = sys.argv[2]  # 9点 1140
    logging.basicConfig(filename='my.log' + bookTime + '-' + index, level=logging.ERROR)

    browser = getbrowser()

    day = '日'
    wednesday = False
    while not wednesday:
        try:
            browser.refresh()
            dateList = browser.find_elements_by_class_name('date-item')
            for date in dateList:
                if day in date.text:
                    date.click()
                    wednesday = True
                    print(time.asctime(time.localtime(time.time())) + "got wednesday")
                    logging.error(time.asctime(time.localtime(time.time())) + "got wednesday")
                    break
        except selenium.common.exceptions.TimeoutException as e:
            logging.exception(e)
            logging.error("wrong...")
            browser = getbrowser()
        except Exception as e:
            print("wrong..")
            print(e)
            logging.error("wrong..")
            logging.exception(e)
        time.sleep(0.1)
        print(time.asctime(time.localtime(time.time())) + "no wednesday")
        logging.error(time.asctime(time.localtime(time.time())) + "no wednesday")

    booked = False
    exception = False
    while True:
        try:
            if exception:
                browser.refresh()
                dateList = browser.find_elements_by_class_name('date-item')
                exception = False
            if dateList is None or dateList.__len__() == 0:
                logging.ERROR("no date got.")
                exception = True

            for date in dateList:
                if day in date.text:
                    date.click()
                    break
                print(time.asctime(time.localtime(time.time())) + "date click refresh..")
                logging.error(time.asctime(time.localtime(time.time())) + "date click refresh..")
                time.sleep(0.1)

            itemList = browser.find_elements_by_class_name("venuePrice")
            for item in itemList:
                print("venueid" + item.get_attribute('venueid'))
                logging.error(bookTime == item.get_attribute('starttime'))
                if bookTime == item.get_attribute('starttime') and item.text != '':
                    # 1140 1200
                    print('find')
                    logging.error('find')
                    item.click()
                    print(time.asctime(time.localtime(time.time())) + 'Book!')
                    logging.error(time.asctime(time.localtime(time.time())) + 'Book!')
                    siteSubmit = browser.find_element_by_id('submitVenue')
                    siteSubmit.click()
                    print(time.asctime(time.localtime(time.time())) + 'submit!')
                    logging.error(time.asctime(time.localtime(time.time())) + 'submit!')
                    booked = True
                    break
            print(time.asctime(time.localtime(time.time())) + "finding..")
            logging.error(time.asctime(time.localtime(time.time())) + "finding..")
        except Exception as e:
            print("wrong...")
            print(e)
            logging.exception(e)
            logging.error("wrong...")
            logging.error(browser.execute_script("return window.performance.memory"))
            exception = True
    if not booked:
        raise RuntimeError('未定到指定场地')


def getbrowser():
    browser = webdriver.Chrome()
    browser.get(
        'https://www.chn-hyd.com/hw/AppVenue/VenueBill/VenueBill?VenueTypeID=d8ce3f86-e2d2-4049-8cfc-7d0b9dd47f9d')
    browser.maximize_window()
    f = open(r'cookie.txt', 'r')
    cookie = {}
    for line in f.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookie['name'] = name
        cookie['value'] = value
        browser.add_cookie(cookie)
    browser.implicitly_wait(10)
    browser.refresh()
    return browser


def clear(browser):
    now = time.localtime()
    if int(time.strftime("%M%S", now)) == 2005:
        browser.execute_script('window.localStorage.clear();')
        logging.error(time.asctime(time.localtime(time.time())) + "clear..")


if __name__ == '__main__':
    book()
