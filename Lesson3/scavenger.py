import os


path_to_file = "C:/"
directory = os.listdir(path_to_file)


data = []
for file in directory:
    if file.endswith(".csv"):
        full_path = path_to_file+file
        with open(full_path,'r') as f:
            for number, line in enumerate(f.readlines()):
                if number == 0:
                    headers = (line)
                else:
                    data.append(line)