import re
em = 'tima.krupeev@gmail.com'
ma = 'prikol@gmailcom'


def email_parse(email_address):
    data1 = re.compile("([A-Za-z._+-]+)@([A-Za-z-]+[.](\w){2,6})")
    name = re.compile("([A-Za-z._+-]+)@")
    domen = re.compile("@([A-Za-z-]+[.]\w{2,6})")
    if data1.fullmatch(email_address):
        dic = {}
        dic["username: "+str(name.findall(email_address))] = "domen: "+str(domen.findall(email_address))
        print(dic)
    else:
        print("wrong email: <email_address>")


email_parse(em)
email_parse(ma)