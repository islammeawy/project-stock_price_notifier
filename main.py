from selenium import webdriver
import time
import yagmail
import os
def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
  return driver




def stock_value():
  driver = get_drvier()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
  value = element.text
  return value

def send_email():
  receiver = "05n0v56byw@spymail.one"
  
  subject = """
  stock value !
  """
  contents = """
  the stock price percent is low !
  """
  yag = yagmail.SMTP(user=os.getenv('email'), password=os.getenv('password')
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")


def sending_email_recpect_to_stock() :
  if stock_value() < '-0.10 %' :
    send_email()


sending_email_recpect_to_stock()

