import time
import names
import proxymanager
import threading
from utils import*
import requests
import random
import pip
pip.main(["install", 'requests'])
pip.main(["install", 'termcolor'])
pip.main(["install", 'colorama'])
pip.main(["install", 'names'])




delay = 0



url = "https://www.subtypestore.com/sean/"
size = '4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15'.split(',')

class entry(threading.Thread):
        def __init__(self,taskNum):
                threading.Thread.__init__(self)
                self.taskNum = taskNum
                self.s = requests.Session()
                self.s.headers = {
                                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                        }
                self.s.headers.update()

                self.firstName = names.get_first_name()
                self.lastName = names.get_first_name()
                self.zipcode = zipcode
                self.names = names.get_full_name()
                self.size = random.choice(size)

                if catchall:
                        self.email = self.firstName + '.' + self.lastName + '@' + domain
                else:
                        self.email = baseEmail + "+{}@gmail.com".format(random.getrandbits(20))

                if name:
                        self.names = ('{} {}'.format(firstn, lastn))
                else:
                        self.names = self.names

                self.data = {
                        'cm-name':self.names,
                        'cm-udkhtty-udkhtty':self.email,
                        'cm-f-dyidtltu':phone,
                        'cm-f-dyidtlil':self.size,
                        'cm-f-dyidtlik':self.zipcode
                        }

        def run(self):
                self.proxy = random.choice(pm.formattedProxies)
                self.re = self.s.post(url, data=self.data, proxies=self.proxy)
                self.re.status_code
                if "Thanks for contacting us" in self.re.text:
                    taskCLog(self.taskNum, "{}- Succesful".format(self.email), "green")
                    f = open("logs.txt", "a")
                    f.write('{} | {} | {} | {} |\n'.format(phone,self.names,self.email,self.size))
                    f.close()
                else:
                    taskCLog(self.taskNum,"[{}] - {} - Failed".format(self.re.status_code,self.email), "cyan")
                    print(self.re.text)


if(__name__ == "__main__"):

        pm = proxymanager
        pm.importProxies('proxies')

        strnames = input('Real Name? "yes" or "no":')
        if strnames.lower() == 'yes':
                firstn = input("First Name:")
                lastn = input("Last Name:")
                name = True
        else:
                name = False

        zipcode = input("Zip: ")
        strCatchAll = input('Catchall domain? "yes" or "no":')
        if strCatchAll.lower() == 'yes':
                catchall = True
                domain = input('domain: (dont include the @): ')

        else:
                gmail = input('What is your full gmail?: ')
                baseEmail = gmail.split('@')[0]
                domain = gmail.split('@')[1]
                catchall = False
        phone = int(input('Phone Number:'))
        entries = input('Number of entries: ')
        delay = float(input('delay: '))

        for taskNum in range(0, int(entries)):
                t= entry(taskNum)
                t.start()
                time.sleep(delay)
