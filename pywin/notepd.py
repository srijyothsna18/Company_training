import os.path
from pywinauto.application import Application

from time import sleep

class note:

    def open_npd(self):
        self.app = Application().start("notepad.exe")
        self.main_dlg = self.app.UntitledNotepad
        self.notepad_window = self.app.top_window()
    def new_file(self):
        self.notepad_window.menu_select("File->New")


    def edit(self):
        self.notepad_window.Edit.type_keys("hello guys welcome to notepad you can edit ur text using notepad,you can use font styles in notepad",with_spaces=True)
        sleep(1)

    def find(self):
        self.notepad_window.menu_select("Edit->Find")
        sleep(2)
        find_window = self.app.Find
        find_window.Edit.set_text("")
        find_window.Edit.type_keys("notepad")
        sleep(1)
        print("class -----",find_window.class_name())
        checkbox1 = find_window.CheckBox
        if checkbox1.is_checked():
            print("checkbox checked")
        else:
            print("unchecked, now checking")
            checkbox1.check()

        checkbox2 = find_window.CheckBox2
        if checkbox2.is_checked():
            print("checkbox checked")
        else:
            print("unchecked, now checking")
            checkbox2.check()

        radiobutton1 = find_window.RadioButton
        radiobutton1.click()
        sleep(2)
        find_window.FindNext.click()
        sleep(2)
        find_window.close()

    def close_npd(self):
        self.app.kill()


    def find_next(self):
        self.notepad_window.menu_select("Edit->FindNext")
        sleep(2)

    def find_previous(self):
        self.notepad_window.menu_select("Edit->FindPrevious")

    def cut_paste(self):
        self.notepad_window.menu_select("Edit->Copy")
        self.notepad_window.menu_select("Edit->Cut")
        sleep(2)
        self.notepad_window.menu_select("Edit->Paste")
        sleep(2)
    #notepad_window.menu_select("Edit->Delete")

    def delete(self):
        self.notepad_window.menu_select("Edit->Delete")
        sleep(2)

    def replace(self):
        self.notepad_window.menu_select("Edit->Replace")
        replace_dialog = self.app.Replace
        replace_dialog.Edit1.set_text("")
        sleep(1)
        replace_dialog.Edit1.type_keys("guys")
        sleep(1)
        replace_dialog.Edit2.set_text("")
        sleep(1)
        replace_dialog.Edit2.type_keys("everyone")
        sleep(1)
        replace_dialog.ReplaceAll.click()
        sleep(2)
        replace_dialog.close()

    def select_all(self):
        self.notepad_window.menu_select("Edit->SelectAll")

    def undo(self):
        self.notepad_window.menu_select("Edit->undo")

    def time(self):
        self.notepad_window.menu_select("Edit->Time/Date")
        sleep(1)
    def font(self):
        self.notepad_window.menu_select("Format->Font")
        font_window = self.app.Font
        font_window.Edit1.set_text("")
        font_window.Edit1.type_keys("calibri")
        sleep(1)
        font_window.Edit2.set_text("")
        sleep(1)
        font_window.Edit2.type_keys("italic")
        font_window.Edit3.set_text("")
        sleep(1)
        font_window.Edit3.set_text("15")
        sleep(1)
        font_window.Ok.click()
        sleep(2)

    def view(self):
        notepad = self.app.UntitledNotepad
        notepad.child_window(title="View", control_type="MenuItem").click_input()
        notepad.print_control_identifiers()
        notepad.child_window(title="Zoom", control_type="MenuItem").click_input()
        notepad.print_control_identifiers()
        notepad.child_window(title="Zoom In	Ctrl+Plus", auto_id="34", control_type="MenuItem").click_input()

    def about(self):
        self.notepad_window.menu_select("Help->About Notepad")
        sleep(1)
        self.app.AboutNotepad.close()
        #self.app.UntitledNotepad.Ok.click_input()
        sleep(1)
        #self.notepad_window.menu_select("Help->View Help")
        #self.notepad_window.menu_select("Help->Send Feedback")
        sleep(1)

    def pagesetup(self):
        self.notepad_window.menu_select("File->PageSetup")
        pagesetup_window = self.app.PageSetup

        combo_box = pagesetup_window.ComboBox1
        combo_box.select("A4")
        sleep(1)

        radio_button = pagesetup_window.RadioButton2
        radio_button.click()
        sleep(1)
        pagesetup_window.Edit1.set_text("10")
        sleep(1)
        pagesetup_window.Edit2.set_text("15")
        sleep(1)
        pagesetup_window.Edit3.set_text("20")
        sleep(1)
        pagesetup_window.Edit4.set_text("25")
        pagesetup_window.Edit5.set_text("")
        sleep(1)
        pagesetup_window.Edit5.set_text("welcome")
        sleep(1)
        pagesetup_window.Edit6.set_text("")
        sleep(1)
        pagesetup_window.Edit6.set_text("By Sri Jyothsna")
        sleep(1)
        pagesetup_window.Ok.click()

    def print(self):
        self.notepad_window.menu_select("File->Print")
        print_window = self.app.Print
        print_window.Edit1.set_text("print")
        sleep(1)
        print_window.Edit2.set_text("Hyderabad")
        sleep(1)
        print_window.Edit3.set_text("Printing using One note")
        sleep(1)
        checkbox = print_window.CheckBox
        #checkbox.check()
        print_window.Edit5.set_text("3")
        print_window.Print.click()

    def saveas(self):
        self.notepad_window.menu_select("File->Save")
        save_as_dialog = self.app.SaveAs
        print("class name-----",save_as_dialog.class_name())
        save_as_dialog.Edit.set_text("pywin")
        combo1 = save_as_dialog.ComboBox2
        combo1.select(1)
        combo2 = save_as_dialog.ComboBox3
        combo2.select(2)
        save_as_dialog.Save.click()
        sleep(1)

        if os.path.exists("pywin.txt"):
            print("file exists ,give another name.....")
            confirm = self.app.ConfirmSaveAs
            sleep(1)
            confirm.No.click_input()
        else:
            print("saved successfully")
    def zoom(self):
        self.notepad_window.menu_select("View->Zoom")
        sleep(1)
        self.notepad_window.type_keys("^+")
        sleep(1)
        self.notepad_window.type_keys("^-")
        sleep(1)
    def open(self):
        self.notepad_window.menu_select("File->Open")
        open_window = self.app.Open
        open_window.Edit.type_keys("sri")
        open_window.Open.click()
        sleep(2)
        print("\nthe content in the file is\n",self.app.Notepad.Edit.window_text())