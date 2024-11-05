import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CsvRecordsToYaml", 
        description="Takes csv records of individual's performances and outputs to stdout the top 3 performing individuals based on division and points.")

    parser.add_argument('filename')
    # how many individuals you want to output, default is 3
    parser.add_argument('-c', '--count')

    parser.print_help()

    # args = parser.parse_args()
    # print(args.filename, args.count)