import json

class LogAnalyzer:
    def __init__(self,in_file,out_file):
        self.in_file=in_file
        self.out_file=out_file

    def read_log(self):
        try:
            with open(self.in_file,"r") as file:
                lines = file.readlines()
            return lines
        except FileNotFoundError:
            print("Log File not found")
            return []

    def log_analyze(self):
        log_count = {
            "INFO" : 0,
            "ERROR" : 0,
            "WARNING" : 0
        }
        lines = self.read_log()
        for line in lines:
            if "INFO" in line:
                log_count["INFO"] += 1
            elif "ERROR" in line:
                log_count["ERROR"] += 1
            elif "WARNING" in line:
                log_count["WARNING"] += 1
            else:
                pass
        return log_count

    def write_json(self,counts):
        with open(self.out_file,"w+") as json_file:
            json.dump(counts, json_file)

log1= LogAnalyzer("app.log","log_count1.json")
counts = log1.log_analyze()
log1.write_json(counts)
print(counts)