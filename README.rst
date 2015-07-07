=========
fpastebin
=========

This a tool to paste any text to http://paste.fedoraproject.org/.

Make a git clone and start using right away. Or you can install it on your system using pip.

::

    $ sudo pip install fpastebin

Usage
-----

::

    Usage:
    $ fpastebin -h               Show this help.
    $ fpastebin --help           Show this help.
    $ <command> | fpastebin      Paste the <command output> online.
    $ fpastebin <path_to_file>   Paste the file data online.
    Examples:
    $ cat data.txt | fpastebin   Paste the 'data.txt' online.
    $ ifconfig | fpastebin       Paste 'ifconfig' output data online.
    $ fpastebin data.txt         Paste the 'data.txt' online.

