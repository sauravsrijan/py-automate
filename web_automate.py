"""
A simple script to automate amazon login, and place an order for my favourite pens.
"""
from webbot import Browser
import getpass
import time

user = input('Enter your Email: ')
pswd = getpass.getpass('Password: ')
genie = Browser()
genie.go_to('amazon.in')
genie.click('Sign in')
genie.type(user+'\n', into='Email')
genie.type(pswd+'\n', into='Password')
genie.type('pilot pens \n', id='nav-searchbar')
genie.go_to('https://www.amazon.in/Pilot-Hi-Techpoint-05-1Blue-1Black/dp/B00LOD658S/ref=sr_1_6?s=office&ie=UTF8&qid=1533997262&sr=1-6&keywords=pilot+pens')
genie.click('Buy Now', id='buy-now-button')
genie.type(pswd+'\n', into='Password')
genie.click(id="pm_gc_checkbox")
genie.click(id='cashOnDeliveryCash')
genie.click(id='continue-top')
time.sleep(10)
print('placing order now')
genie.click("Place your order")
