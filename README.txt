To run file:

1. Python3.6 used for testing
2. Install libraries first: pip install robobrowser (Mac os).
3. Use pip3 to install if planning to use python3
4. Type "python3 good_read.py" within bash terminal to run script.
5. Output file will be in put in current directory.

To run tests:

1. Python3.6 used for testing
2. Install libraries first: pip install pytest
3. Type pytest tests.py to run test

Additional Info:

Unlike get_post in exercise 1 which used BeautifulSoap and requests for scraping,
robobrowser was chosen due to ease of logging in for scraping by automating tokens and other hidden information.

3 unit tests were created for
1) Tests that goodread.com was successfully reached
2) Tests that logging into the webpage works as expected by finding the user bar
3) Tests that getting quotes works by checking first quote gotten

