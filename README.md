# Dreambox Neuron

## Control Enigma2 based STB with Kalliope using openwebif API

## Installation
```bash
kalliope install --git-url https://github.com/xheen908/dreambox_neuron.git
```

## Options

| parameter        | required | default                       | choices                           | comments                     |
|------------------|----------|-------------------------------|-----------------------------------|------------------------------|
| dream_ip         | yes      | 192.168.1.2                   |                                   |                              |
| dream_port       | no       | 80                            |                                   |                              |
| dream_user       | no       | root                          |                                   |                              |
| dream_pass       | no       |                               |                                   |                              |

## Synapses example

```yml
 - name: "zapto"
   signals:
     - order: "zap to {{ channel }}"
   neurons:      
     - dreambox:
         input_action: "{{ channel }}"
    
 - name: "standby"
   signals:
     - order: "switch tv off"
   neurons:      
     - dreambox:
         input_action: "standby"

 - name: "mute"
   signals:
     - order: "switch sound on"
     - order: "switch sound off"
   neurons:      
     - dreambox:
         input_action: "mute"
 
 - name: "volup"
   signals:
     - order: "tv volume up"
   neurons:      
     - dreambox:
         input_action: "volup"

 - name: "voldown"
   signals:
     - order: "tv volume down"
   neurons:      
     - dreambox:
         input_action: "volup" 

 - name: "setvol"
   signals:
     - order: "set volume {{ percent }}%"
   neurons:      
     - dreambox:
         input_action: "setvol"

 - name: "back"
   signals:
     - order: "back"
   neurons:      
     - dreambox:
         input_action: "back"

 - name: "timeshift"
   signals:
     - order: "timeshift"
   neurons:      
     - dreambox:
         input_action: "timeshift"

```

## Notes

> **Note:** This is an important note concerning the neuron

## Licence

Here define or link the licence you want to use.
