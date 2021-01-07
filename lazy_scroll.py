from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


parser = ArgumentParser(description="Lazy auto-scroller for Reddit")
parser.add_argument('--driver', type=str, default='./chromedriver')
parser.add_argument('--directory', type=str, default='/var/tmp/chrome_reddit')
parser.add_argument('--login', dest='login', action='store_true')
parser.add_argument('--no-login', dest='login', action='store_false')
parser.add_argument('--username', type=str, default='')
parser.add_argument('--password', type=str, default='')
parser.add_argument('--wait', type=int, default=3)
parser.set_defaults(login=False)
args = parser.parse_args()

options = Options()
options.add_argument('--user-data-dir=' + args.directory)
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path=args.driver, options=options)
try:
    if(args.login):
        try:
            driver.get('https://www.reddit.com/login/')
            driver.find_element_by_id('loginUsername').send_keys(args.username)
            driver.find_element_by_id('loginPassword').send_keys(args.password)
            driver.find_element_by_tag_name('button').click()
            sleep(2)
        except Exception as e:
            print('Couldnt get login page due to error: ' + str(e))
            print('Exiting...')
            driver.quit()
        while(driver.execute_script('return document.readyState')!='complete'):
            sleep(2)
    else:
        try:
            driver.get('https://www.reddit.com')
        except Exception as e:
            print('Page load failed due to error: ' + str(e))
            print('Exiting...')
            driver.quit()

    last_div = None
    while(1):
        all_divs = driver.find_elements_by_tag_name('div')
        if(last_div):
            all_divs = all_divs[all_divs.index(last_div):]
        for div in all_divs:
            try:
                if('t3_' in div.get_attribute('id')[:4]):
                    if(len(div.get_attribute('id').split('-'))>1):
                        continue
                    parent = div.find_element_by_xpath('..')
                    driver.execute_script("arguments[0].scrollIntoView({behavior: \"smooth\", block: \"center\", inline: \"nearest\"});", parent)
                    sleep(args.wait)
                last_div = div
            except:
                break
except KeyboardInterrupt:
    pass
