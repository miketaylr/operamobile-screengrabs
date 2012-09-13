#!/usr/bin/env python
#coding: utf-8

import os
import urlparse
import time
import shutil
from selenium import webdriver, selenium
from datetime import date

date = date.today().isoformat()
SITELIST = os.path.dirname(__file__) + "sites.txt"
webdriver.DesiredCapabilities.OPERA["opera.product"] = "mobile"
webdriver.DesiredCapabilities.OPERA["opera.binary"]  = "/Applications/Opera Mobile Emulator.app/Contents/Resources/Opera Mobile.app/Contents/MacOS/Opera Mobile"
operadriver = webdriver.Opera(desired_capabilities=webdriver.DesiredCapabilities.OPERA)

#todo?
#selenium.add_custom_request_header
#selenium.add_script to futz with navigator.userAgent object
    
def takeScreengrab(uri):
    "take a screenshot for a specific uri"
    operadriver.get(uri)
    
    # without this sleep call, i'm getting timeout exceptions. ¯\_(ツ)_/¯
    time.sleep(1)
    domain = urlparse.urlparse(uri).netloc
    operadriver.save_screenshot('grabs/' + domain + '-' + date + '.png')
      
def main():
    # we load the reference of the file
    
    if os.path.exists('grabs'):
      pass
    else:
      os.mkdir('grabs')
      
    with open(SITELIST) as f:
        #we read the file line by line to not have it in memory
        for uri in f:
            # remove leading, trailing spaces
            uri = uri.strip()
            # ignore line starting with #, allowing comments
            if uri.startswith("#"):
                continue
            # take a screenshot
            takeScreengrab(uri)
            
    operadriver.close()
    
    # i want to do this now. lrn2shut_down
    # selenium.shut_down_selenium_server(sel)

if __name__ == '__main__':
    main()
