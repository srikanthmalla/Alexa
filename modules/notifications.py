import notify2

class Notification():
    def recording(self,active_module):
        notify2.init('Alexa')
        title='Recording'
        n=notify2.Notification('Recording',active_module)
        n.show()
