# SeleniumProjects
Small Project using (Selenium + Python)

-----Prerequisites-----
1) Python 3
2) Selenium
3) Pytest
4) pytest-html
5) pytest-xdlist
6) openpyexcel

installation steps : https://www.softwaretestinghelp.com/selenium-python-tutorial/  

----Steps to run using command prompt-------
1) Clone the repository 
2) Go to Configuration folder and edit the config.ini file
3) Go to nopcommerce\testCases and execute below command
4) Command syntax 
pytest -v -s test_name --browser name
Ex. nopcommerce\testCases>pytest -v -s test_login.py --browser chrome

Note:- If no --browser option provided, firefox is defualt 
