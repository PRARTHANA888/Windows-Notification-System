from plyer import notification
#import requests
#from bs4 import BeautifulSoup
#from colorama import Fore, Back, Style
#from colorama import init




def notifyMe(title , message):
    notification.notify(
        title=title, 
        message=message, 
        app_icon=None ,
        timeout= 20
    )


if __name__ == "__main__":
    notifyMe("Corona Virus Status" , "Active (2.03%) : 213603 (904🠗)                            Discharged (96.52%) : 10146763 (17652🠕)                                            Deaths (1.44%) : 151727 (198🠕)                     Total No of Tests Done Till Date : 743191" )


    #myHtmlData = getData('https://www.mohfw.gov.in/')

    
    #soup = BeautifulSoup(myHtmlData , 'html.parser')
    #print(soup.prettify())
    #myDataStr = ""
    
    #for table in soup.find_all('table'):
        #print(table)

    #states = ['haryana', 'kerala', 'karanatka']
    #print(states)

        #myDataStr += tr.get_text()
    #print(myDataStr)




            

    