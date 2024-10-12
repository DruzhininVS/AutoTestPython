from checkers import checkout, getout, checkout_negative

folder_in = "/home/user/Pycharm/tst"
folder_out = "/home/user/Pycharm/out"
folder_ext = "/home/user/Pycharm/folder1"
folder_full_ext = "/home/user/Pycharm/folder2"

def test_step1():
    checkout('mkdir {} {} {}'.format(folder_out, folder_ext, folder_full_ext), "Create_Folders")
    res1 = checkout("cd {}; 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx2.7z")
    assert res1 and res2, "test1 FAIL"
def test_step2():
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1")
    res3 = checkout("ls {}".format(folder_ext), "checkers")
    assert res1 and res2 and res3, "test2 FAIL"
def test_step3():
    assert checkout("cd {}; 7z t arx2.7z".format(folder_out), "Everything is Ok"), "test3 FAIL"
def test_step4():
    assert checkout("cd {}; 7z u arx2.7z".format(folder_in), "Everything is Ok"), "test4 FAIL"
def test_step5():
    res1 = checkout("cd {}; 7z l arx2.7z".format(folder_in, folder_ext), "test1.py")
    res2 = checkout("cd {}; 7z l arx2.7z".format(folder_in, folder_ext), "checkers.py")
    assert res1 and res2, "test5 FAIL"
def test_step6():
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(folder_out, folder_full_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_full_ext), "test1.py")
    res3 = checkout("ls {}".format(folder_full_ext), "checkers.py")
    assert res1 and res2 and res3, "test6 FAIL"
def test_step7():
    res1 = checkout("cd {}; 7z h test1.py".format(folder_in), "Everything is Ok")
    hash = getout("cd {}; crc32 test1.py".format(folder_in)).upper()
    res2 = checkout("cd {}; 7z h test1.py".format(folder_in), hash)
    assert res1 and res2, "test7 FAIL"
def test_step8():
    assert checkout("cd {}; 7z d arx2.7z".format(folder_out), "Everything is Ok"), "test8 FAIL"
    checkout('rm -rf {} {} {}'.format(folder_out, folder_ext, folder_full_ext), "Clean_Folders")
def test_negative_step1():
    assert checkout_negative("cd {}; 7z e arx_er.7z -o{} -y".format(folder_in, folder_ext), "ERROR:"), "test1_negative FAIL"
def test_negative_step2():
    assert checkout_negative("cd {}; 7z t arx_er.7z".format(folder_in), "ERROR:"), "test2_negative FAIL"
