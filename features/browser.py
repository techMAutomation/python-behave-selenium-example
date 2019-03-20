from selenium import webdriver
import os
import datetime
import logging


class Browser(object):

    # user_profile_path = os.getenv('HOME')
    # print(' -- UserProfile path : %s ' % user_profile_path)
    driver = webdriver.Chrome(os.path.basename('drivers') + '/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://daaz.com")
    driver.set_page_load_timeout(5)
    print(' Run started at : ' + str(datetime.datetime.now()))

    # To generate logs
    logging.basicConfig(filename='logs.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    def close(context):
        context.driver.close()

