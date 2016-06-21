from basethread import BaseThread
import urllib, urllib2
import sched, time
import xbmc

import vars
import utils


class PollingThread(BaseThread):

    def __init__(self):
        super(self.__class__, self).__init__()
        utils.log("PollingThread init")

    def run(self):
        self.scheduler = sched.scheduler(time.time, xbmc.sleep)
        self.scheduler.enter(10, 1, self.polling, ())
        self.scheduler.run()
        utils.log("PollingThread run")

    def polling(self):
        url = 'http://nlqosdrecv01.neulion.com/msdrecv/ProxyBean'
        headers = { 
            'Cookie': vars.cookies, 
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'iPad'
        }
        body = urllib.urlencode({
            'messageType': 'APP_HB',
            'convention':  '1.0',
            'productID':   'nba',
            'carrierName': 'CTCarrier (0x1577d4ab0)',
            'deviceType':  'iPhone',
            'os':  'IOS9.3',
            'clientID':    '202A68E1-31E5-434D-949D-A1C6231F897D',
            'networkType': 'wifi',
            'appType': 'iphone',
            'mode': '0',
            'siteID': 'nba',
            'updateInterval': '60',
            'appVersion':  '60419',
            'sessionID':   '1464206790',
        })

        utils.log("polling ProxyBean")

        try:
            request = urllib2.Request(url, body, headers)
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            pass

        self.scheduler.enter(3, 1, self.polling, ())