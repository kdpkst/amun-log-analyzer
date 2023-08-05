import os

class AmunLogParser:
    
    def __init__(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.filename = filename
                    content = f.read()
                    self.contentList = content.split('\n')
            except IOError:
                self.contentList = None
        else:
            self.contentList = None
				


    def amun_request_handler_log_parser(self):
        if self.contentList is None:
            print('no file or IO error')
            return None

        # the following is just a test, will be improved in the future 
        i = 0
        log_data = {}
        log_data['IP'] = {}
        log_data['Stages'] = {}
        for line in self.contentList:
            line_data = line.split(' ')
            if log_data['IP'].get(line_data[7]) is None:
                log_data['IP'][line_data[7]] = 1
            else:
                log_data['IP'][line_data[7]] = log_data['IP'].get(line_data[7]) + 1
            i = i + 1
            if i == 15:
                break
        return log_data


parser = AmunLogParser('logs/amun_request_handler.log.2023-07-27')
log_data = parser.amun_request_handler_log_parser()
IP_table = log_data['IP']
print(max(IP_table.values()))









