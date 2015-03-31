# This is the lab.. where we test and do everything
from Task import SimpleTask

class Lab(SimpleTask):
    def __init__(self):
        SimpleTask.__init__(self,"Lab",["MadScientist >> "])
        self.add_function("print",self.print_files,"Prints the song list")
        return

    def get_stock_quote(self,info):
        # stock,duration="day",exchange="NSE"
        return
    
    def plot(self,info):
        # array of ids
        # because we will be analyzing multiple things
        # Should have provision to plot all of them
        # for e.g. overlap with oil, gold, dollar etc...
        
        # So the plan is that go ahead add each element to the plot
        # then finally plot it. with plot_show()
        return
    
    def plot_show(self,info):
        # keeping option to feed data
        return
        


