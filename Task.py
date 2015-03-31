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
