import sys
sys.path.append('common')
import log_parser
import os

class AmunRequestHandlerAnalyzer:

    def data_processing(self, filename):
        parser = log_parser.AmunLogParser(filename)
        log_data = parser.amun_request_handler_log_parser()

        # change the dictionary to sorted list
        IP_table = sorted(log_data['IP'].items(), key=lambda x: -x[1])
        port_table = sorted(log_data['port_scanned'].items(), key=lambda x : -x[1])
        stages_table = sorted(log_data['stages'].items(), key=lambda x: -x[1])

        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        basename = os.path.basename(filename)
        report_filename = 'output/statistics_' + basename 
        with open(report_filename, 'w') as f:
            f.write("attacker IP        number\n")
            for item in IP_table:
                f.write(f"{item[0].ljust(20)}{item[1]}\n")

            f.write("\nport scanned      number\n")
            for item in port_table:
                f.write(f"{str(item[0]).ljust(20)}{item[1]}\n")

            f.write("\nstages             number\n")
            for item in stages_table:
                f.write(f"{item[0].ljust(20)}{item[1]}\n")
          
                
    def data_visulization(self):
        return None



