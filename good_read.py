from robobrowser import RoboBrowser
import re
import json

def get_quotes():
    url = 'https://www.goodreads.com/'
    twain_url = 'https://www.goodreads.com/author/quotes/1244.Mark_Twain'
    (USERNAME, PASSWORD) = get_credentials()
    br = open_page(url)
    user_login(br, USERNAME, PASSWORD)
    quote_page(br, twain_url)


def get_credentials():
    USERNAME = input("Please enter Username:(email) ")
    print("You entered " + str(USERNAME))
    PASSWORD = input("Please enter Password: ")
    print("Your password is " + str(PASSWORD))
    return (USERNAME, PASSWORD)

def open_page(url):
    br = RoboBrowser(history=True, parser="html.parser")
    br.open(url)
    print(br.response.url)
    return br

def user_login(br, USERNAME, PASSWORD):
    form = br.get_form()
    form['user[email]'] = USERNAME
    form['user[password]'] = PASSWORD
    br.submit_form(form)
    print(br.response.url)
    return br


def quote_page(br, twain_url):
    br.open(twain_url)
    print(br.response.status_code)
    soup = br.parsed
    quotes = soup.find_all('div', attrs={"class":"quoteDetails"})
    quote_list = []
    for quote in quotes[:10]:
        thisquote = quote.find(attrs={"class": "quoteText"}).getText()
        thisquote = (re.findall(r'“(.*?)”', thisquote))
        likes = quote.find(attrs={"title": "View this quote"}).getText()
        quote_list.append({"quote": thisquote, "likes": likes})
    print(quote_list[0]['quote'])

    with open('./output.txt', 'w') as outfile:
        json.dump({"quote": quote_list}, outfile)
    print(quote_list)
    return quote_list

get_quotes()