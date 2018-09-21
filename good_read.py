from robobrowser import RoboBrowser
import re
import json

def get_quotes():
    """Head function to run all the other functions"""
    USERNAME, PASSWORD = "", ""
    url = 'https://www.goodreads.com/'
    twain_url = 'https://www.goodreads.com/author/quotes/1244.Mark_Twain'
    (USERNAME, PASSWORD) = get_credentials()
    br = open_page(url)
    br = user_login(br, USERNAME, PASSWORD)
    raw_html = br.parsed
    signin_bar = raw_html.find(attrs={"class":"siteHeader__personal"})
    print(signin_bar)
    quote_page(br, twain_url)


def get_credentials():
    """Get the username and password via commandline input"""
    USERNAME = input("Please enter Username:(email) ")
    print("You entered " + str(USERNAME))
    PASSWORD = input("Please enter Password: ")
    print("Your password is " + str(PASSWORD))
    return (USERNAME, PASSWORD)

def open_page(url):
    """Opens the goodreads homepage for login"""
    br = RoboBrowser(history=True, parser="html.parser")
    br.open(url)
    return br

def user_login(br, USERNAME, PASSWORD):
    """Logs into the goodreads homepage using robobrowser"""
    form = br.get_form()
    form['user[email]'] = USERNAME
    form['user[password]'] = PASSWORD
    br.submit_form(form)
    return br


def quote_page(br, twain_url):
    """Checks the Mark Train Quotes Page and scrapes the top 10 quotes"""
    br.open(twain_url)
    soup = br.parsed
    quotes = soup.find_all('div', attrs={"class":"quoteDetails"})
    quote_list = []
    for quote in quotes[:10]:
        thisquote = quote.find(attrs={"class": "quoteText"}).getText()
        thisquote = (re.findall(r'“(.*?)”', thisquote))
        likes = quote.find(attrs={"title": "View this quote"}).getText()
        quote_list.append({"quote": thisquote, "likes": likes})

    with open('./output.txt', 'w') as outfile:
        json.dump({"quote": quote_list}, outfile)
    print("Mark Twain top 10 posts have been saved to output.txt locally")
    return quote_list

if __name__ == "__main__":
    get_quotes()