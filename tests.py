import good_read

def test_goodread_open_page():
    url = 'https://www.goodreads.com/'
    br = good_read.open_page(url)
    assert br.url == url

def test_user_login():
    url = 'https://www.goodreads.com/'
    failed_login = 'https://www.goodreads.com/user/sign_in?source=home'
    br = good_read.open_page(url)
    br = good_read.user_login(br, "", "")
    assert br.url == failed_login

def test_most_liked_quote():
    twain_url = 'https://www.goodreads.com/author/quotes/1244.Mark_Twain'
    famous_quote = ["If you tell the truth, you don't have to remember anything."]
    br = good_read.open_page(twain_url)
    quote_list = good_read.quote_page(br, twain_url)
    assert quote_list[0]["quote"] == famous_quote
