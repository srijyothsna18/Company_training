from pywinauto.application import Application
app = Application().start("Notepad.exe")
app.Notepad.edit.TypeKeys("sriii")
#app.Notepad.MenuSelect("File ->SaveAs")
#app.SaveAs.edit.SetText("pywin.txt")
#app.SaveAs.Save.click()
app.Notepad.MenuSelect("View ->Zoom")
app.Zoom.Zooomin.click()