#!/usr/bin/python3

import webbrowser
import sys

def main():
    
    try:
        webbrowser.get('firefox').open(str(sys.argv[1]))

    except webbrowser.Error:
        print('firefox not found')

if __name__ == "__main__":
    main()
