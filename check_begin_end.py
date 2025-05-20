class check_opening:
    stack = []
    new_stack = []
    idx = 0
    rets = []

    def check(self, lists):
        if len(lists)%2 != 0:
            return False
        else:
            for l in lists:
                if l.lower() == 'begin':
                    self.stack.append(l.lower())
                else:
                    if self.stack[-1] == 'begin':                        
                        self.stack.pop()
        return True if self.stack == [] else False
    
    
    def check_and_update(self, lists, file_name):
        only_words = [l["word"] for l in lists]
        le = []
        res = self.check(only_words)
        if res != True:
            return "Begin and End mismatch"
        else:
            for l in lists:
                if l["word"].lower() == 'begin':
                    t1 = {
                        "item": l["word"],
                        "lno": l["lno"],
                    }
                    self.new_stack.append(t1)
                else:
                    self.idx += 1
                    t2 = {
                        "number": f"--{self.idx}",
                        "index": self.idx,
                        "begin_lno": self.new_stack[-1]["lno"],                        
                        "end_lno": l["lno"]
                    }
                    le.append(t2)                        
                    self.new_stack.pop()
            return le