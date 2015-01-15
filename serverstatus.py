#coding=utf-8
from BeautifulSoup import BeautifulSoup     # For processing HTML
import urllib2
import time

myserver = raw_input('Input the server name:\n')
#myserver = '银月'

def Appsleep(func):
    def wrapper(myserver):
        time.sleep(5)
        ret = func(myserver)
        return ret
    return wrapper


@Appsleep
def CheckServStatus(myserver): 
    html_doc = urllib2.urlopen(r"http://www.battlenet.com.cn/wow/zh/status").read()
    soup = BeautifulSoup(html_doc)
    servers = soup.findAll('tr',attrs = {'class':'row1'}) + soup.findAll('tr',attrs = {'class':'row2'})
    for server in servers:
        servername = server.findAll('td',attrs = {'class':'name'})
        status = server.findAll('div')
        #print servername[0].getText() + ': ' + status[0]['data-tooltip'] 
        if myserver == servername[0].getText().encode('utf-8'):
            if '正常' == status[0]['data-tooltip'].encode('utf-8'):
                print '上线啦'
                return 1
            else:
                #print myserver  , status[0]['data-tooltip'].encode('utf-8') ,time.ctime()
                return 0  

while 0 == CheckServStatus(myserver):
    CheckServStatus(myserver)

