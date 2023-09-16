from .. import interface

def sendmessage():
    
    config={
      	
      'message':'hallo',
      	
    }
    interface.outbox('openmessage', data=config)