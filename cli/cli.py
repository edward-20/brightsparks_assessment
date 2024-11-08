'''
CLI Tool main
'''

import argparse
import cli.csv_parse
import top_n_list.TopNList

def main():
    '''
    main
    '''
    # parse the command line arguments
    parser = argparse.ArgumentParser(
        prog="CsvRecordsToYaml",
        description='''
        Takes csv records of individual's performances and outputs to stdout the
        top c (default 3) performing individuals based on division and points.
        ''',
        formatter_class=argparse.RawTextHelpFormatter
        )

    parser.add_argument('filename')
    # how many individuals you want to output, default is 3
    parser.add_argument('-c', '--count', help="the number of records you want to output", default=3)
    # sort by alternative field than division and points
    parser.add_argument('-s', '--sort-by', action="append", choices=['firstName', 'lastName', 'date', 'division', 'points'],
                        help='''
                        choose an alternative way to sort the records. Options include
                        - firstName
                        - lastName
                        - date
                        - division
                        - points

                        default being by division then points

                        you can use this optional argument multiple times, the
                        order in which you specify the arguments matters

                        Example:
                        python3 main.py -s firstName -s lastName file.csv

                        would mean that the records would be sorted by firstName and in the event of equality, sort by lastName
                        ''',
                        )
    args = parser.parse_args()

    filename = args.filename
    if not sort_by:
        sort_by = ["division", "points"]
    cli.csv_parse.Record.sort_by = args.sort_by

    
    # retains top records as python dictionaries in order from greatest to lowest
    top_parsed_records = top_n_list.TopNList(args.count)

    with open(filename, "r", encoding='utf-8') as file:
        # read and verify the first line
        first_line = file.readline()
        headers = None
        try:
            headers = cli.csv_parse.verify_header_line(first_line)
        except cli.csv_parse.IncorrectHeaders as e:
            print(f'An error occurred: {e}')

        # parse each line of the csv into a python object and then determine if it
        # breaks into the top count records
        for line in file:
            try:
                parsed_record = cli.csv_parse.parse_csv_record(headers, line)
                print(parsed_record)
                    
                top_parsed_records.add(parsed_record)
                    
            except cli.csv_parse.ImproperRecord as e:
                print(f'An error occurred: {e}')


    # output as yaml

if __name__ == "__main__":
    main()