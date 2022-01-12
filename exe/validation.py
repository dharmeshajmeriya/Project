import re
import datetime

class Validator:

    def phono(self,phone):
        rphone = r"(0|91)?[7-9][0-9]{9}"

        if(re.search(rphone, phone)):
            return phone
        else:
            print("not valid")

    def mail(self,email):
        remail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if(re.fullmatch(remail,email)):
            return email
        else:
            print("not valid")

    def name(self,name):
        rname = r"^[A-z][A-z|\.|\s]+$"

        if(re.search(rname,name)):
            return name
        else:
            print("not valid")

    def date(self, date):
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            if date_obj.date() < date.today():
                print("The date cannot be in the past!")
            else:
                return date_obj
        except Exception as e:
            print(e)
