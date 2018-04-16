# -*- coding: iso-8859-1 -*-
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from kalliope import Utils
import requests
import yaml



class Enigma(NeuronModule):
    def __init__(self, **kwargs):
        super(Enigma, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.ip = kwargs.get('ip', None)
        self.port = kwargs.get('port', 80)
        self.login = kwargs.get('login', None)
        self.password = kwargs.get('passwort', None)
        self.command = kwargs.get('command', None)
        self.channel = kwargs.get('channel', None)
        self.file = kwargs.get('file', None)
        
        if self._is_parameters_ok():
            path = Utils.get_real_file_path(self.file)
            file = None
            found = False
            
            if self.login:
                url = "http://" + self.login + ":" + self.password + "@" + str(self.ip) + ":" + str(self.port)
            else:
                url = "http://" + str(self.ip) + ":" + str(self.port)
            
            if self.channel:
                url = url + "/web/zap?sRef="
                file = open(path, "r")
                channels = yaml.load(file)
                for channel in channels:
                    if channel == self.channel:
                        Utils.print_info("Channel found: " + channel)
                        url = url + channels[channel]
                        found = True
                        break
                if not found:                
                    Utils.print_info("Channel : " + self.channel + " not found")
                        
            else:
                url = url + "/web/remotecontrol?command="
                file = open(path, "r")
                cmds = yaml.load(file)
                for cmd in cmds:
                    if cmd == self.command:
                        Utils.print_info("Command found: " + cmd)
                        url = url + cmds[cmd]
                        found = True
                        break        
                if not found:                
                    Utils.print_info("Command : " + self.command + " not found")
            
            if found:
                Utils.print_info("Sending: " + url)
                try:
                    requests.post(url)
                except requests.exceptions.ConnectionError:
                    Utils.print_info("Failed to establish a new connection")
                    
                
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """
        if self.ip is None:
            raise MissingParameterException("You must set the IP address")
        elif self.file is None:
            raise MissingParameterException("You must set the the file name")
        elif self.login and not self.password:
            raise MissingParameterException("You forgot the password")            
        return True
