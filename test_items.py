import pytest
import time

def test_to_find_button_add_to_basket(browser):
    #time.sleep(10)
    assert browser.find_element_by_class_name( 'btn-add-to-basket' )
