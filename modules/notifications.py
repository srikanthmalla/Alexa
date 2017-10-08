import pynotify

class Notification():
    def recording(self,active_module):
        pynotify.init('Alexa')
        title='Recording'
        n=pynotify.Notification('Recording',active_module)
        n.show()
