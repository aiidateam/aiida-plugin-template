# AiiDA - Mul

A minimal plugin for aiida

* Designed to be runable on a local machine with direct scheduler.
* pip-installable from source with no dependencies except for aiida 0.8 (or later)


# Installation

```
pip install -e .  # also installs aiida, if missing
verdi quicksetup  # better to set up a new profile
verdi calculation plugins  # should now show aiida-plugin.multiply
```
