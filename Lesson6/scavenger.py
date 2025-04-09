import os



def add_data(first_list, second_list):
    row = {}
    for i in range(len(second_list)):
        row[first_list[i]] = second_list[i]
    return row


def main():
    data = []
    the_path = os.getcwd()

    for subdir, dirs, files in os.walk(the_path):
        for file in files:
            if file.endswith(".csv"):
                full_path = os.path.join(the_path, file)

    with open(full_path, 'r') as f:
        for row_num, row in enumerate(f):
            if row_num == 0:
                
                #remove new line '\n'
                row = row.rstrip('\n')

                #split the string of the row by ',' to create a new row
                headers = row.split(',')
            else:
                row = row.rstrip('\n')

                data_to_add = row.split(',')

                data.append(add_data(headers, data_to_add))

    print(data)


if __name__ == '__main__':
    main()
