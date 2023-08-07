import analyzers.amun_request_handler_analyzer as arha

def main():
    analyzer = arha.AmunRequestHandlerAnalyzer()
    analyzer.data_processing('./amun_request_handler.log.2023-07-23')
    

if __name__== "__main__" :
    main()
