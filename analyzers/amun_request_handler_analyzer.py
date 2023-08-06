import sys
sys.path.append('common')
import log_parser

class request_handler_analyzer:

    def data_processing(self, filename):
        parser = log_parser.amun_log_parser(filename)
        log_data = parser.amun_request_handler_log_parser()

        IP_table = log_data['IP']
        print(max(IP_table.values()))
        stages_table = log_data['stages']
        port_table = log_data['port_scanned']
        entry_num = log_data['entry_num']



