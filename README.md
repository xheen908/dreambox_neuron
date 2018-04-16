# Dreambox Neuron

## Control Enigma2 based STB with Kalliope using openwebif API

## Installation
```bash
kalliope install --git-url https://github.com/xheen908/dreambox_neuron.git
```

## Options

| parameter        | required | default                       | choices                           | comments                     |
|------------------|----------|-------------------------------|-----------------------------------|------------------------------|
| ip               | yes      | 192.168.1.2                   |                                   |                              |
| port             | no       | 80                            |                                   |                              |
| user             | no       |                               |                                   |                              |
| pass             | no       |                               |                                   |                              |

## Synapses example

```yml
  - name: "channel"
    signals:
      - order: "{{ channel }}"
    neurons:
      - enigma:
          ip: 192.168.1.2
          channel: "{{ channel }}"
          file: "resources/neurons/enigma/channels.yml"
  
  - name: "command"
    signals:
      - order: "{{ cmd }}"
    neurons:
      - enigma:
          ip: 192.168.1.2
          command: "{{ cmd }}"
          file: "resources/neurons/enigma/commands.yml"

```

## Notes

> **Note:** This is an important note concerning the neuron

## Licence

Here define or link the licence you want to use.
