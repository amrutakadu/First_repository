from django.dispatch import Signal, receiver

ping_signal = Signal()      # (providing_args=["context"])        # creating a custom signal
print(ping_signal)

class SignalDemo(object):           # sender
    """
    function to send signal
    """
    def ping(self):
        print('PING')
        ping_signal.send(sender=self.__class__, PING=True,val = 25)          # self.__class__ is same as SignalDemo


@receiver(ping_signal)
def pong(**kwargs):     
    """
    Function to receive signal
    """
    if kwargs.get('PING'):          # kwargs['PING']:       -- this will generate KeyError if we do not pass kwargs but get will not raise error
        print('PONG')
        # print(kwargs)

# demo = SignalDemo()
# demo.ping()