import time
def timeme (func) :
    def decorate(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print ("Total time", end-start)
    return decorate