import request

from kalliope.core.NeuronModule import NeuronModule
class Dreambox(NeuronModule):

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Dreambox(NeuronModule):
    def __init__(self, **kwargs):
        super(Dreambox, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.dreambox_ip = kwargs.get('dreambox_ip', '192.168.1.114')
        self.dreambox_port = kwargs.get('dreambox_port', 80)
        self.dreambox_login = kwargs.get('dreambox_login, None)
        self.dreambox_password = kwargs.get('dreambox_password' None)
        self.dreambox_ircommand = kwargs.get('dreambox_ircommand', '/web/remotecontrol?command=')
        self.dreambox_zap = kwargs.get('dreambox_zap', '/web/zap?sRef=')
        
        if self._is_parameters_ok():
            if self.Dreambox_login is not None:
                self.Dreambox = Dreambox_Control("http://" + str(self.dreambox_login) + ":" + str(self.dreambox_password) + "@" + str(self.dreambox_ip) + ":" + str(self.dreambox_port)
            else
                self.Dreambox = Dreambox_Control("http://" + str(self.dreambox_ip) + ":" + str(self.dreambox_port)
                
