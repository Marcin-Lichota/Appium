def test_find_stratus(home):
    list = home.nav_to_list_demo()
    list.find_stratus()
    text = list.getstratustext()
    print(text)
    assert "Stratus" in text