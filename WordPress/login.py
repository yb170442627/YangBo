# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver




  
def login(self):
    login_url = 'http://localhost/wordpress/wp-login.php'
    dr = self.dr
    dr.get(login_url)
    dr.find_element_by_name('log').send_keys('adminfy')
    dr.find_element_by_name('pwd').send_keys('111111')
    dr.find_element_by_name('wp-submit').click() 