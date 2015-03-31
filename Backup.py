import os
import fnmatch
from multiprocessing import process
import subprocess

def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

def print_list(alist,cols):
    count=0
    cols=cols-1
    if len(alist) == 0:
        return

    for i in alist:
        print i,
        if (count - cols) == 0:
            print ""
            count=0
        else:
            count=count+1
    print ""    
    return


def find_songs(path):
    files=recursive_glob(path,"*.m4a")
    return files


def print_list_with_number(alist,cols):
    count=0
    cols=cols-1
    if len(alist) == 0:
        return
    
    number=0

    for i in alist:
        print "{0} : {1}".format(number,i),
        if (count - cols) == 0:
            print ""
            count=0
        else:
            count=count+1
        number=number+1
    print ""    
    return

def print_list_wl(alist_wl):
    
    alist = alist_wl[0]
    cols  = alist_wl[1]
    count=0
    cols=cols-1
    if len(alist) == 0:
        return

    for i in alist:
        print i,
        if (count - cols) == 0:
            print ""
            count=0
        else:
            count=count+1

    print ""    
    return

class WorkerLoop_v1:
    def __init__(self,prompt,functions,data):
        self.prompt=prompt # it is an array for prompts at different levels
        self.functions=functions # dictionary of functions
                                 # Should have help and exit
        self.max_level=len(prompt)-1
        self.data=data     # again a dictionary of data
        return

    def run(self):
        level = 0
        cond =True
        while cond:
            cmd_string=raw_input(self.prompt[level])
            cmd=cmd_string.split()
            try:
                function=self.functions[cmd[0]]
                if len(cmd) > 1:
                    data = self.data[cmd[1]+" "]
                    cond=function(data)
                else:
                    cond=function()


            except KeyError:
                if level >= self.max_level:
                    level=self.max_level
                else:
                    level=level+1
                try:
                    functions['help']()
                except KeyError:
                    print "Bloody hell - you didn't give a help/usage function"


class SimpleTask:
    def __init__(self,name,prompt):
        self.functions={
                        'help': [self.help1,"Help routine"],
                        'exit' : [self.exit,"Exit routine"]
        }
        self.name=name
        self.prompt=prompt # it is an array for prompts at different levels
        self.max_level=len(prompt)-1
               
        return
    
       
    def help1(self):
        for funcname, funcdetails in self.functions.items():
            print " {2} : {0} -> {1}".format(funcname,funcdetails[1],self.name)
        return True

    def exit(self):
        print "Exiting module -> {0} ".format(self.name)
        return False
    
    def add_function(self,name,function,description):
        self.functions[name]=[function,description]
        return 
    

    def run(self):
        level = 0
        cond =True
        while cond:
            cmd_string=raw_input(self.prompt[level])
            cmd_list=cmd_string.split()
            cmd=cmd_list[0]
            args=False
            if len(cmd_list) > 1:
                args=cmd_list[1:]
                

            try:
                if not args:
                    function=self.functions[cmd]
                    cond=function[0]()
                else:
                    function=self.functions[cmd]
                    cond=function[0](args)
                    

            except KeyError:
                if level >= self.max_level:
                    level=self.max_level
                else:
                    level=level+1
                try:
                    function=self.functions['help']
                    function[0]()
                except KeyError:
                    print "Bloody hell - you didn't give a help/usage function"    
                    

                    
class MediaPlayer(SimpleTask):
    def __init__(self):
        SimpleTask.__init__(self,"media player",["rihanna >> "])
        self.file_list=[]
        self.add_function("print",self.print_files,"Prints the song list")
        self.add_function("find",self.find_files,"Finds the songs and adds to list")
        self.add_function("play",self.play_file,"Play a particular file number")
        self.add_function("what",self.playing,"Print name of file which is playing")
        self.add_function("stop",self.stop,"Stop the current playing file")
        self.p1=None
        self.playing=None
        self.playlist=[]
        return
    
    def print_files(self):
        print_list_with_number(self.file_list,1)
        return True
    
    def find_files(self):
        self.file_list=find_songs("C:\Dropbox\Audacious\songs")
        return True
    
    def play_file(self,number):
        self.p1=subprocess.Popen(["C:/Dropbox/audacious-3.5.2-win32/bin/audacious.exe",self.file_list[int(number[0])]])
        #Not joining here
        self.playing=int(number[0])
        return True
    
    def exit(self):
        print "New exit : waiting for task to join"
        if self.p1:
            self.stop()
            
        return False
        
    def stop(self):
        print "Stopped playing song -> {0}".format(self.file_list[self.playing])
        self.playing=None
        self.p1.terminate()
        return True
    
    def playing(self):
        print "Playing song -> {0}".format(self.file_list[self.playing])
        return True
        
    def add_play_queue(self,number):
        return True
        
        
    
    
        
mp=MediaPlayer()
    
