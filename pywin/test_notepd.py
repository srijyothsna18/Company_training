from notepd import note
from time import sleep
obj = note()

def test_open():
    obj.open_npd()
    sleep(1)
    obj.new_file()
    obj.close_npd()

def test_edit():
    obj.open_npd()
    sleep(1)
    obj.edit()
    obj.close_npd()

def test_cut_paste():
    obj.open_npd()
    obj.edit()
    obj.find()
    obj.cut_paste()
    obj.close_npd()


def test_replace():
    obj.open_npd()
    obj.edit()
    obj.replace()
    obj.close_npd()

def test_select_and_delete():
    obj.open_npd()
    obj.edit()
    obj.select_all()
    obj.delete()
    obj.close_npd()

def test_undo():
    obj.open_npd()
    obj.edit()
    obj.select_all()
    obj.delete()
    sleep(1)
    obj.undo()
    sleep(1)
    obj.close_npd()

def test_time():
    obj.open_npd()
    obj.new_file()
    obj.time()
    obj.close_npd()
def test_zoom():
    obj.open_npd()
    obj.edit()
    obj.zoom()
    obj.close_npd()
def test_font():
    obj.open_npd()
    obj.new_file()
    obj.edit()
    obj.font()
    obj.close_npd()

def test_about():
    obj.open_npd()
    obj.about()
    obj.close_npd()

def test_pagesetup():
    obj.open_npd()
    obj.edit()
    obj.pagesetup()
    obj.close_npd()
def test_print():
    obj.open_npd()
    obj.edit()
    obj.print()
    obj.close_npd()

def test_save_as():
    obj.open_npd()
    obj.edit()
    obj.saveas()
    obj.close_npd()

def test_open():
    obj.open_npd()
    obj.open()
    obj.close_npd()


"""def test_view():
    obj.open_npd()
    obj.new_file()
    obj.edit()
    obj.view()
"""

"""def test_find():
    obj.open_npd()
    obj.edit()
    obj.find()
    obj.close_npd()"""

"""def test_delete():
    obj.open_npd()
    obj.edit()
    obj.find()
    obj.delete()
    obj.close_npd()"""

"""def test_find_next():
    obj.open_npd()
    obj.edit()
    obj.find_next()
    sleep(2)
    obj.close_npd()"""
