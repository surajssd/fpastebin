#!/usr/bin/python
import requests
import sys
import json
import os

def print_usage():
    usage = """Usage:
    $ fpastebin -h               Show this help.
    $ fpastebin --help           Show this help.
    $ <command> | fpastebin      Paste the <command output> online.
    $ fpastebin <path_to_file>   Paste the file data online.
    Examples:
    $ cat data.txt | fpastebin   Paste the 'data.txt' online.
    $ ifconfig | fpastebin       Paste 'ifconfig' output data online.
    $ fpastebin data.txt         Paste the 'data.txt' online.
    """
    print usage
    sys.exit(0)


def upload(text):
    """
    text: Any data to be uploaded.
    Return: Link to uploaded data.
    """
    if len(text) == 0:
        print_usage()
    try:
        url = 'http://paste.fedoraproject.org/'
        data = {

            'paste_data': text,
            'paste_lang': None,
            'api_submit': True,
            'mode': 'json'
        }
        reply = requests.post(url, data=data).text
        result = json.loads(reply)
        return 'http://paste.fedoraproject.org/' + result['result']['id']

    except ValueError as e:
        print "Error:", e
        print "Raw Reply:", reply
    except requests.exceptions.ConnectionError as e:
        print 'Error:', e
    except KeyboardInterrupt:
        print "Try again!!"
        sys.exit(0)


def main():
    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            # Need Help
            print_usage()
        elif os.path.exists(sys.argv[1]):
            # Path to text file specified
            f = open(sys.argv[1])
            text = f.read()
            f.close()
        else:
            # Nothing specified
            print 'Error: Unknow option mentioned.'

    except IndexError:
        # When tried to pipe in input and no option was specified, trying
        # to use sys.argv will throw exception.
        try:
            text = sys.stdin.read()
        except KeyboardInterrupt:
            print 'Error: No Input given.'
            print_usage()

    print upload(text)


if __name__ == '__main__':
    main()
