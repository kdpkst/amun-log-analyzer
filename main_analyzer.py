import analyzers.amun_request_handler_analyzer as arha
import argparse
import os


def main():
    args = argument_parser()    
    filename = args.filename
    output_dir = args.output
    logs_dir = args.recursion

    if filename is None and logs_dir is None:
        print("please specify necessary arguments.")
    else:
        if filename is not None and logs_dir is not None:
            print("-f and -r cannot be used at the same time.")
        elif filename is not None:
            argument_f(filename, output_dir)
        elif logs_dir is not None:
            argument_o(logs_dir, output_dir)
 

def argument_parser():
    parser = argparse.ArgumentParser(description="Amun Log Analyzer", usage="%(prog)s [-h] -f -o")
    parser.add_argument("-f", "--filename", required=False, help="Path to the single log file")
    parser.add_argument("-o", "--output", required=False, default='./output', help="Path to the output directory")
    parser.add_argument("-r", "--recursion", required=False, help="Path to the directory storing multiple log files")

    return parser.parse_args()


def argument_f(filename, output_dir):
    if not os.path.exists(filename):
        print("the specified file does not exit.")
    else:
        basename = os.path.basename(filename)
        if basename.startswith('amun_request_handler'):
            analyzer = arha.AmunRequestHandlerAnalyzer()
            analyzer.data_report(filename, output_dir)


def argument_o(logs_dir, output_dir):
    for root_path, subdirectories, files in os.walk(logs_dir):
        if not os.path.exists(root_path):
            print("the specified directory does not exit.")
            break
        elif len(subdirectories) != 0:
            print("the specified dir can only contain log files")
            break
        else:
            for file in files:
                filename = root_path + '/' + file
                argument_f(filename, output_dir)


if __name__== "__main__" :
    main()
