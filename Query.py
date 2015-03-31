# this is the Query class

import re


def print_info(stock,duration):
    line = stock.readline()
    
    while (line != ''):
        print line
        line = stock.readline()
    return


class GetStockInfo():
    def __init__(self,name,duration,exchange="NS"):
        self.name = name
        self.duration = duration
        self.exchange = exchange
        url = "http://chartapi.finance.yahoo.com/instrument/1.0/{0}.{2}/chartdata;type=quote;range={1}/csv".format(name,duration,exchange)
        self.data = urllib2.urlopen(url)
        self.unit = []
        self.close = []
        self.high = []
        self.low = []
        self.open_s = []
        self.volume = []
        self.extract_info()
        return
                 

    def extract_info(self):
        re1=re.compile(r"volume:*")
        line = self.data.readline() # uri
        line = self.data.readline() # ticker
        self.name = self.data.readline().split(":")[1]
        line = self.data.readline() # exchange
        line = self.data.readline() # unit
        line = self.data.readline() # check
        while (not re1.match(line)):
            line = self.data.readline() # check
            
        line = self.data.readline() # data
        while (line != ''):
            unit1,close1,high1,low1,open_s1,volume1=line.split(",")
            self.unit.append(unit1)
            self.close.append(float(close1))
            self.high.append(float(high1))
            self.low.append(float(low1))
            self.open_s.append(float(open_s1))
            self.volume.append(int(volume1.split("\n")[0]))
            line = self.data.readline() # data
        return
            
            
    def print_info(self,count=10):
        line = self.data.readline()
        final = count
        count = 0
        while (line != '' and count < final):
            print line
            line = self.data.readline()
            count = count + 1
        return                     
               
        
from bokeh.plotting import *
        
class GPlot():
    color=["red","blue","green","yellow","golden"]
    def __init__(self,name):
        output_file(name+".html")
        
        return
    def line(



class Query(SimpleTask):
    def __init__(self):
        SimpleTask.__init__(self,"Query",["stock >>"])
        self.query_list={}
        return
    
    def get_stock(self,info):
        name = info[0]
        duration = info[1] # 1d-10,1m-10m,1y-5y
        exchnage = info[2]
        stock_data = GetStockInfo(name,duration,exchange)

        
