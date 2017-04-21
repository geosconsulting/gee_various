def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-v","--verbose", help="increase verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print "verbosity is turned on"

if __name__ == '__main__':
    main()