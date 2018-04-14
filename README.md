# Dreambox Neuron

## Synopsis

Enigma2 Remote Controll Neuron 

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
| standby          | no       |                               |                                   |                              |
| vol+             | no       |                               |                                   |                              |
| vol-             | no       |                               |                                   |                              |
| mute+            | no       |                               |                                   |                              |
| chan+            | no       |                               |                                   |                              |
| chan+            | no       |                               |                                   |                              |

## Return Values

Only necessary when the neuron use a template to say something

| name      | description                        | type       | sample                    |
|-----------|------------------------------------|------------|---------------------------|
| value_key | dictionary containing all the data | dictionary | {"name":"me", "email": 2} |
| value_key | list of value                      | list       | ["val1", "val2", "val3"]  |
| value_key | string value                       | string     | "2"                       |
|

## Synapses example

Description of what the synapse will do
```yml
 - name: "type here your name"
   signals:
     - order: "this is what I have to say to run this synapse"
   neurons:      
     - neuron_name:
        parameter: "value"
        parameter: "value"
        file_template: template_name.j2
    
```

## Templates example 

Description of the template
```
This is a var {{ var }} 
{% for item in items %}
 This is the  {{ item }}  
{% endfor %}
```

## Notes

> **Note:** This is an important note concerning the neuron

## Licence

Here define or link the licence you want to use.
