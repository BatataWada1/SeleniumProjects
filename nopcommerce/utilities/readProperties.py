import configparser

config = configparser.RawConfigParser()
print(config)
config.read(r"C:\Users\mandar_kulkarni1\PycharmProjects\nopcommerce\Configurations\config.ini")

class readConfig():

    @staticmethod
    def chrome_driver_path():
        chrome_driver = config.get('DRIVER', 'chrome')
        return chrome_driver

    @staticmethod
    def firefox_driver_path():
        firefox_driver = config.get('DRIVER', 'moziladriverpath')
        return firefox_driver

    @staticmethod
    def login_page_url():
        login_page_url = config.get('LOGINPAGE', 'baseURL')
        return login_page_url

    @staticmethod
    def login_email():
        login_email = config.get('LOGINPAGE', 'email')
        return login_email

    @staticmethod
    def login_password():
        login_password = config.get('LOGINPAGE', 'password')
        return login_password

    @staticmethod
    def screen_shots():
        screen_shots = config.get('SCREENSHOTS', 'screenshots')
        return screen_shots

print(readConfig.chrome_driver_path())
print(readConfig.login_page_url())
print(readConfig.login_email())
print(readConfig.login_password())