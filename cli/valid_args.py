'''
Functions validating command line arguments
'''
import argparse
import os

def valid_filename(filename: str):
    '''
    Validate filename command line argument.
    '''
    if not os.path.isfile(filename):
        raise argparse.ArgumentTypeError(f"File {filename} doesn't exist or is not accessible.")
    return filename

def valid_count(count: str):
    '''
    Validate count command line argument.
    '''
    try:
        count = int(count)
        if count < 1:
            raise argparse.ArgumentTypeError("Cannot have a count of less than 1.")
        return count
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Count must be of type int with value greater than 1.") from exc