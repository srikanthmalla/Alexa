from modules.youtube import *
def process_command(splitted):
    command=splitted[0]
    if command.lower() =='youtube':
        yt_link=ytsearch(splitted[1:None])
        p=videoplay(yt_link)
        p.start()
        p.run()
        return p
    elif (command.lower()=='music'):
        yt_link=ytsearch(splitted[1:None])
        p=musicplay(yt_link)
        p.start()
        p.run()
        return p
    else:
        print('wrong command')
        return 0
