#!/usr/bin/env python
"""
Simple example

Usage:
    simple.py -f INPUT_FILE -n NUMBER [options]
    simple.py (-h | --help)

Options:
    --dry           Dry run.
    -h --help       Show this screen.
"""

def main():
    from docopt import docopt
    args = docopt(__doc__)

    input_filename = args.get('INPUT_FILE')
    max_iterations = int(args.get('NUMBER'))
    dry_run        = args.get('--dry')
    
    print(f'Mock script to process {input_filename} with {max_iterations} iterations')

    if dry_run:
        print("This script will run in dry (read only) mode.")
    
if __name__ == '__main__':
    main()
