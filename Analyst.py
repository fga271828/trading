
#http://real-chart.finance.yahoo.com/table.csv?s=ZYLOG.NS&d=2&e=26&f=2015&g=d&a=7&b=17&c=2007&ignore=.csv

# http://chartapi.finance.yahoo.com/instrument/1.0/WIPRO.NS/chartdata;type=quote;range=1d/csv
import nsetools
import pprint as pp
import unittest

# Get all the stock names in NSE

class TAGS():
    # TAGS - dict of tags
    #        each tag dict of company codes
    def __init__(self):
        self.tagd={}
        return
    def add_tag_stock(self,tag,stock_code):
        if self.tagd.has_key(tag):
            temp=self.tagd[tag]
            temp[stock_code]=None
            self.tagd[tag]=temp
        else:
            self.tagd[tag]={stock_code:None}
        return
    def list_tags(self):
        keys = self.tagd.keys()
        pp.pprint(keys)
        return
    def list_stocks_in_tag(self,tag):
        temp = self.tagd[tag]
        pp.pprint(temp.keys())
        return 
    def filter_companies(self,tag):
        # tag has to be a regular expression
        # need to evolve on this part later
        # such that we can give complex tag information
        return self.tagd[tag].keys()
    def remove_tag_stock(self,tag,stock_code):
        temp = self.tagd[tag]
        temp.pop(stock_code)
        self.tagd[tag]=temp
        return


class Test_TAGS(unittest.TestCase):
    def setUp(self):
        self.test1 = TAGS()
        self.test1.add_tag_stock("blue_chip","INFY")
        self.test1.add_tag_stock("blue_chip","INFY") # there should be only one
        self.test1.add_tag_stock("midcap","AMTEK")
        self.test1.add_tag_stock("midcap","SUZLON")
    def test_db(self):
        self.assertEquals(self.test1.tagd,{'blue_chip': {'INFY': None}, 'midcap': {'AMTEK': None, 'SUZLON': None}})
    def test_list_tags(self):
        self.assertEquals(self.test1.list_tags(),"['blue_chip', 'midcap']")
    def test_list_stocks_in_tag(self):
        self.assertEquals(self.test1.list_stocks_in_tag("midcap"),['AMTEK', 'SUZLON'])
    def test_filter_companies(self):
        self.assertEquals(self.test1.filter_companies("midcap"),['AMTEK', 'SUZLON'])
    def test_remove_tag_stock(self):
        self.test1.remove_tag_stock("midcap","AMTEK")
        self.test1.remove_tag_stock("midcap","SUZLON")
        self.assertEquals(self.test1.tagd,{'blue_chip': {'INFY': None}, 'midcap': {}})
    def tearDown(self):
        self.test1 = None
#if __name__ == '__main__':
#    unittest.main()
#
#suite = unittest.TestLoader().loadTestsFromTestCase(Test_TAGS)
#unittest.TextTestRunner(verbosity=2).run(suite)            
        
class Company():
    def __init__(self,nse_code,name):
        self.nse_code = nse_code
        self.name = name
        return
    

    


class Print():
    def print_a(self,line,level):
        print line
        return

class StockDB():
    def __init__(self):
        self.nse_stock_codes=None
        self.stocks_all={}
        return
    def get_nse_list(self):
        temp = nsetools.Nse()
        stock_codes=temp.get_stock_codes()
        if self.nse_stock_codes == None:
            self.nse_stock_codes = stock_codes
        else:
            # Check if any new code got added in the list
            # if so print a warning and add it to the list
            for key, value in stock_codes.get_items():
                if not self.nse_stock_codes.has_key(key):
                    self.nse_stock_codes[key]=value
                    Print.print_a("{0} added to list".format(key),0)
        return
    def update_stock_info(self):
        if self.nse_stock_codes == None:
            Print.print_a("NSE stock code not present")
            return
        else:
            for key, value in self.nse_stock_codes.items():
                # The reason to have a stock hash with value as a parameter
                # in the list is for regex match when I forget, can use nse
                # list as well.. but will keep nse_stock_codes only to be
                # used here. Everywhere else use stocks_all
                self.stocks_all[key]=[value,Company(key,value)]
                # Creating a separate Company datastructure such that
                # all future information regarding Company can go in it
                # it is not merely stock price.. everythin else
        return
        
    



