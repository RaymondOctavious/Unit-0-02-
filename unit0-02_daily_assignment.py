#created by raymknd octavious
#created on september 2017
#created for ics3u
#created for daily assignment 
#this program displays name, city, address

import ui

def click_button_touch_up_inside(sender):
	
    view['name_label'].text = "Raymond Octavious"
    view['city_label'].text = "Ottawa"
    view['address_label'].text = "Ontario"

view = ui.load_view()
view.present('sheet')
