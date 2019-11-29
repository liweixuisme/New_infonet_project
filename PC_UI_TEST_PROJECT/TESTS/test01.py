class LoginBusinessView():

    def loginButtonClick(self,**dict):

        print(dict["page_name"])

if __name__ == '__main__':
    dict = {
        "page_name": "login_page"
    }
    LoginBusinessView().loginButtonClick(**dict)