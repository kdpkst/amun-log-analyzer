import analyzers.amun_request_handler_analyzer as arha
import argparse
import os


def main():
    args = argument_parser()    
    filename = args.filename
    output_dir = args.output
    logs_dir = args.recursion

    if filename is None and logs_dir is None:
        print("please specify necessary arguments [-f] [-r].")
    else:
        if filename is not None and logs_dir is not None:
            print("-f and -r cannot be used at the same time.")
        elif filename is not None:
            argument_f(filename, output_dir)
        elif logs_dir is not None:
            argument_r(logs_dir, output_dir)
 

def argument_parser():
    parser = argparse.ArgumentParser(description="Amun Log Analyzer", usage="%(prog)s [-h] -f -o")
    parser.add_argument("-f", "--filename", required=False, help="Path to the single log file")
    parser.add_argument("-o", "--output", required=False, default='./output', help="Path to the output directory")
    parser.add_argument("-r", "--recursion", required=False, help="Path to the directory storing multiple log files")

    return parser.parse_args()


def argument_f(filename, output_dir):
    if os.path.exists(filename) and os.path.isfile(filename):
        basename = os.path.basename(filename)
        if basename.startswith('amun_request_handler.log'):
            analyzer = arha.AmunRequestHandlerAnalyzer()
            analyzer.data_report(filename, output_dir)
            # analyzer.data_visulization(filename, output_dir)
        elif basename.startswith("amun_server.log"):
            pass
        elif basename.startswith("download.log"):
            pass
        elif basename.startswith("exploits.log"):
            pass
        elif basename.startswith("shellcode_manager.log"):
            pass
        elif basename.startswith("submissions.log"):
            pass
        elif basename.startswith("successfull_downloads.log"):
            pass
        elif basename.startswith("unknown_downloads.log"):
            pass
        elif basename.startswith("vulnerabilities.log"):
            pass
        elif basename.startswith("analysis.log"):
            pass
        else:
            print("wrong file type. Only amun log file is accepted.")
    else:
        print("the specified file does not exit or it is not a file.")



def argument_r(logs_dir, output_dir):
    if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        for root_path, subdirectories, files in os.walk(logs_dir):
            if len(subdirectories) != 0:
                print("the specified directory contains subdirectories. only files are accepted.")
                break
            else:
                for file in files:
                    filename = root_path + '/' + file
                    argument_f(filename, output_dir)
    else:
        print("the specified directory does not exist or it is not a directory.")


if __name__== "__main__" :
    main()
