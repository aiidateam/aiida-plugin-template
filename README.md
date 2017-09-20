# AiiDA - Mul

A minimal plugin for aiida

* can be pip-installed from source with no dependencies except for aiida 0.8 (or later)
* can be run on a local machine with direct scheduler for easy testing


# Installation

```shell
$ pip install -e .  # also installs aiida, if missing
$ verdi quicksetup  # better to set up a new profile
$ verdi calculation plugins  # should now show aiida-plugin.multiply
```

# Usage

```shell
$ verdi code setup  # need to set up code
At any prompt, type ? to get some help.
---------------------------------------
=> Label: aiida_mul
=> Description: aiida template plugin
=> Local: True
=> Default input plugin: plugin.multiply
=> Folder with the code: /path/to/aiida_mul
=> Relative path of the executable: code.py
=> Text to prepend to each command execution
FOR INSTANCE, MODULES TO BE LOADED FOR THIS CODE:
   # This is a multiline input, press CTRL+D on a
   # empty line when you finish
   # ------------------------------------------
   # End of old input. You can keep adding
   # lines, or press CTRL+D to store this value
   # ------------------------------------------
=> Text to append to each command execution:
   # This is a multiline input, press CTRL+D on a
   # empty line when you finish
   # ------------------------------------------
   # End of old input. You can keep adding
   # lines, or press CTRL+D to store this value
   # ------------------------------------------
Code 'aiida_mul' successfully stored in DB.
pk: 1, uuid: 7627c747-b7f2-4717-b0fa-94e53915e422

$ verdi computer setup
At any prompt, type ? to get some help.
---------------------------------------
=> Computer name: localhost
Creating new computer with name 'localhost'
=> Fully-qualified hostname: localhost
=> Description: my local machine
=> Enabled: True
=> Transport type: local
=> Scheduler type: direct
=> AiiDA work directory: /tmp
=> mpirun command:
=> Default number of CPUs per machine: 4
=> Text to prepend to each command execution:
   # This is a multiline input, press CTRL+D on a
   # empty line when you finish
   # ------------------------------------------
   # End of old input. You can keep adding
   # lines, or press CTRL+D to store this value
   # ------------------------------------------
=> Text to append to each command execution:
   # This is a multiline input, press CTRL+D on a
   # empty line when you finish
   # ------------------------------------------
   # End of old input. You can keep adding
   # lines, or press CTRL+D to store this value
   # ------------------------------------------
Computer 'localhost' successfully stored in DB.
pk: 1, uuid: a5b452f0-ec1e-4ec2-956a-10a416f60ed3
Note: before using it with AiiDA, configure it using the command
  verdi computer configure localhost
(Note: machine_dependent transport parameters cannot be set via
the command-line interface at the moment)

$ verdi run examples/script.py
```

