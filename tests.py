import good_read

def test_goodread_open_page():
    """Test that page opened is the homepage of goodreads by checking title"""
    url = 'https://www.goodreads.com/'
    resp = good_read.open_page(url)
    raw_html = resp.parsed
    title = raw_html.find("title").getText()
    expected_title = "\nGoodreads — Share book recommendations with your friends, join book clubs, answer trivia\n"
    assert expected_title == title

def test_user_login():
    """Test to make sure that successful login finds the user login bar"""
    url = 'https://www.goodreads.com/'
    resp = good_read.open_page(url)
    resp = good_read.user_login(resp, "eugenemyu@gmail.com", "123456")
    raw_html = resp.parsed
    signin_bar = raw_html.find(attrs={"class":"siteHeader__personal"})
    assert signin_bar != None

def test_most_liked_quote():
    """Test to make sure that quotes are pulled correctly by checking most liked quote"""
    twain_url = 'https://www.goodreads.com/author/quotes/1244.Mark_Twain'
    famous_quote = ["If you tell the truth, you don't have to remember anything."]
    br = good_read.open_page(twain_url)
    quote_list = good_read.quote_page(br, twain_url)
    assert quote_list[0]["quote"] == famous_quote
