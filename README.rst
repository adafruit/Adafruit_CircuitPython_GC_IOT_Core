Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-gc_iot_core/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/gc_iot_core/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_GC_IOT_CORE/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_GC_IOT_CORE
    :alt: Build Status

Google Cloud IoT Core Client for CircuitPython


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython JWT <https://github.com/adafruit/Adafruit_CircuitPython_JWT>`_
* `Adafruit CircuitPython Logging <https://github.com/adafruit/Adafruit_CircuitPython_Logger>`_


Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-gc_iot_core/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-gc-iot-core

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-gc-iot-core

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-gc-iot-core

Usage Example
=============

Usage example within examples/ folder.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/gc_iot_core/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_GC_IOT_CORE/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

License
=======

This library was written by Google for MicroPython. We've converted it to
work with CircuitPython and made changes so it works with boards supported by
CircuitPython and the CircuitPython API.

We've added examples for using this library to transmit board telemetry data along
with sensor data to Google's Cloud Platform.

This open source code is licensed under the Apache license (see LICENSE) for details.
