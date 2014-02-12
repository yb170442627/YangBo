# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import time
import login
from selenium.webdriver.support.ui import Select

class WordPressTestCase(unittest.TestCase):
    dr = None
    
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'
    
    def setUp(self):
      self.dr = webdriver.Chrome()
      #self.login_url = 'http://localhost/wordpress/wp-login.php'
      print 'sr\etup'   

    def test_login(self):
	  #self.login()
      login.login(self)
      self.dr.implicitly_wait(30)
      print self.dr.current_url
      self.assertTrue('wp-admin' in self.dr.current_url)
	  
    def test_create_post(self):
	  login.login(self)
	  self.dr.implicitly_wait(30)
	  title = self.create_post()
	  
	  self.dr.get(self.post_list_url)
	  post_list_table = self.dr.find_element_by_class_name('wp-list-table')
	  self.assertTrue(title in post_list_table.text)
 
	
    def test_delete_post(self):
       login.login(self)
       self.dr.implicitly_wait(30)
       title = self.create_post()
       self.dr.get(self.post_list_url)
       post_list_table = self.dr.find_element_by_class_name('wp-list-table')
       self.assertTrue(title in post_list_table.text)
       self.dr.find_element_by_id('cb-select-all-1').click()
       select_elmt = self.dr.find_element_by_name('action')
       select = Select(select_elmt)
       select.select_by_value('trash')
       self.dr.find_element_by_id('doaction').click()
       print "deleted successfully!"
	   
    def test_edit_post(self):
       login.login(self)
       self.dr.implicitly_wait(30)
       title = self.create_post()
       self.dr.get(self.post_list_url)
       post_list_table = self.dr.find_element_by_class_name('wp-list-table')
       self.assertTrue(title in post_list_table.text)
       self.dr.find_element_by_class_name('row-title').click()
       self.dr.find_element_by_name('post_title').clear()
       title_or_content = 'new post' + str(time.time())
       self.dr.find_element_by_name('post_title').send_keys(title_or_content)
       js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
       print js
       self.dr.execute_script(js)
       self.dr.find_element_by_id('publish').click()
       print "updated successfully!"
	   
	   
	   
    def create_post(self):
      create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
      self.dr.get(create_post_url)
      title_or_content = 'new post' + str(time.time())
      self.dr.find_element_by_name('post_title').send_keys(title_or_content)
      js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
      print js
      self.dr.execute_script(js)
      self.dr.find_element_by_name('publish').click()
      return title_or_content

    def tearDown(self):
	    sleep(3)
	    self.dr.quit()
		
if __name__ == '__main__':
    unittest.main()