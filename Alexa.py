from scripts.record import *
hot_word=False
process={}
while(1):
    try:
        if hot_word==True:
            p,t=record_command()
            if t=='stop':
                process[p].stop()
                del process[p]
            elif t is not 0:
                process[p]=t
                print(process[p])
            print("total no of processes:",len(process)) 
            hot_word=False
        else:
            print('recording..')
            hot_word=record_alexa()
    except (KeyboardInterrupt, SystemExit):
        raise
