from pywinauto.application import Application
from PIL import Image
app = Application().start("notepad.exe")

notepad_window = app.top_window()
#notepad_window.menu_select("Help->View Help")
"""window_image = notepad_window.capture_as_image()
window_image.save("image.png")

image_path = "image.png"
path = Image.open(image_path)
path.show()
"""

"""edit_control = notepad_window.child_window(class_name="Edit")
client_rect = edit_control.rectangle()
screen_point =edit_control.client_to_screen((client_rect.left,client_rect.top))
print(screen_point)
print(client_rect.left,client_rect.top)
notepad_window.print_control_identifiers()"""

"""num_controls = notepad_window.control_count()
print("no of controls are ",num_controls)

print(type(num_controls))

# we can get the control id of control and we can use that id to use that control

edit_control = notepad_window.child_window(class_name = "Edit")
id = edit_control.control_id()
print("id of edit_control is",id)

notepad_window.print_control_identifiers()
edit_control1 = notepad_window.child_window(control_id=15)
edit_control1.set_text("sri")

descendent_genetaror = edit_control1.descendants()
for descendent in descendent_genetaror:

    print("----------",descendent.control_id())
#we can also use like this simply
#notepad_window.Edit.set_text("sri")


#h = edit_control.drag_mouse_input(dst=(200,300),src=None,button="left")
#h.double_click_input()

print("info-----",edit_control.element_info)

print(edit_control.friendly_class_name())
"""


"""notepad_window.menu_select("File->PageSetup")
page_setup_dialog = app.PageSetup
combo = page_setup_dialog.ComboBox

print(combo.class_name())
print(combo.friendly_class_name())
print("is dialog",page_setup_dialog.is_dialog())
print(combo.get_properties())

print(notepad_window.is_maximized())
notepad_window.maximize()
print(notepad_window.is_maximized())


print("is enabled",find_what_dialog.verify_enabled())
print("is enabled",page_setup_dialog.is_enabled())
print("is enabled",find_what_dialog.is_enabled())
print("is enabled",page_setup_dialog.is_enabled())

print("is visible",find_what_dialog.is_visible())
print("is enabled",page_setup_dialog.is_visible())

print("is dialog",edit_control.is_dialog())

print(edit_control.is_visible())

print("parent ",edit_control.parent())
print("parent",find_what_dialog.parent())
print("parent",radio2.parent())
print("parent",combo.parent())
print("parent",combo.top_level_parent())
find_what_dialog.close()
page_setup_dialog.close()


child_list = notepad_window.children()
for child in child_list:
    print("Class Name:", child.class_name())
    print("Control ID:", child.control_id())
    print("Text:", child.window_text())
    print("----------")


for child in notepad_window.iter_children():
    print("Class Name:", child.class_name())
    print("Control ID:", child.control_id())
    print("Text:", child.window_text())
    print("----------")

notepad_window.menu_select("Format->Font")
font_dialog = app.Font

des = font_dialog.descendants()
for child in des:
    print("id",child.control_id)
    print("type",child.control_type())
    print("class name",child.class_name())
"""

import logging
logging.basicConfig(filename='pywinauto_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("aplication started")

edit_control = notepad_window.child_window(class_name="Edit")
edit_control.set_text("sri")
print(notepad_window.is_in_taskbar())
notepad_window.hide_from_taskbar()
print(notepad_window.is_in_taskbar())

find_what = notepad_window.menu_select("Edit->FindWhat")
find_what_dialog = app.Find
check1 = find_what_dialog.CheckBox1
find_what_dialog.show_in_taskbar()
print("is in taskbar",find_what_dialog.is_in_taskbar())
# the difference between class_name() and friendly_class_name() is class_name() gives normal answer like it is button while
#friendly class name gives exact ans and helps user like it gives output as it is checkbox or radio button etcc
print(check1.class_name())
print(check1.friendly_class_name())


find_what_dialog.CheckBox1.uncheck()
find_what_dialog.CheckBox2.check()

radio = find_what_dialog.RadioButton1
print("type",edit_control.control_type())
print("is radio button enabled",radio.is_enabled())

radio2 = find_what_dialog.RadioButton2
print("infooo----------",radio2.elementinfo)
radio2.click()
print("is radio button enabled",radio2.is_enabled())

print(radio.class_name())
print(radio.friendly_class_name())
print(radio.get_properties())
print("is dialog",find_what_dialog.is_dialog())
#find_what_dialog.close()

font = notepad_window.fonts()
print(font)
print(notepad_window.get_active())
print("state",notepad_window.get_show_state())
print("toolbar",find_what_dialog.get_toolbar())
print("menu",notepad_window.menu_items())
extended_styles = notepad_window.exstyle()
print("style",hex(extended_styles))

print(edit_control.expand())
logging.info("closing application")
app.kill()


