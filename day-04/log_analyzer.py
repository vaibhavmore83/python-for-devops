def read_log():
    try:
        with open("app.log", "r") as file:
            line = file.readlines()
        return line
    except FileNotFoundError:
        print("File not found")
        return []

def log_analyze(lines):
    log_count = {
        "INFO" : 0,
        "ERROR" : 0,
        "WARNING" : 0
    }
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

def write_json(counts):
    with open("log_count.json", "w+") as json_file:
        import json
        json.dump(counts, json_file)

lines = read_log()
print(lines)
counts = log_analyze(lines)
print (counts)
write_json(counts)

#readlines from 09:00 to 09:20 only
def read_log_timeframe(start_time, end_time):
    try:
        with open("app.log", "r") as file:
            lines = file.readlines()
        filtered_lines = []
        for line in lines:
            if ":" in line:
                time_part = line.split(" ")[1]  # Assuming time is the first part of the log line
            if start_time <= time_part <= end_time:
                filtered_lines.append(line)
        return filtered_lines
    except FileNotFoundError:
        print("File not found")
        return []
        
tflines = read_log_timeframe("09:00:00", "09:20:00")
counts = log_analyze(tflines)
print (counts)