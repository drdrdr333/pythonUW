'''
1.
'''
import csv
import random


def fn_one():
    headers = ("question_id","question")
    data = [[12,"What is your phone number?"], [10, "What is your email?"]]
    with open('questions.csv', 'w', newline='') as q:
        writer = csv.writer(q, dialect='excel')
        writer.writerow(headers)
        writer.writerows(data)

'''
2.
'''

def add_data_to_csv(question, existing_ids, filename, data=None):
    if data is None:
        data = ()
    
    question_id = random.randint(0,100)

    for x in existing_ids:
        if x == str(question_id):
            question_id += 1

    data += (question_id, question)

    with open(filename, '+a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)

    
    
def fn_two():
    with open('questions.csv','r') as q:
        existing_ids = []
        reader = csv.reader(q, dialect='excel', delimiter=',')
        for row in reader:
            the_row = ', '.join(row)
            the_row_ = the_row.replace(", ", " ")
            existing_ids.append(the_row_[0:2])
            
        new_question = input("What question would you like to add to our trivia game?\n\n")

        add_data_to_csv(new_question, existing_ids, q.name)

'''
3.
'''

def add_data(data_to_add):
    interviewee = input("What is your name?") 
    for row in data_to_add:
            row['interviewee'] = interviewee

    with open('answers.csv', 'w', newline='') as a:
        fields = ['interviewee', 'question_id', 'answer']
        writer = csv.DictWriter(a, fieldnames=fields)

        writer.writeheader()
        writer.writerows(data_to_add)


def fn_three():
    with open('questions.csv','r') as q:
        data = []
        headers = ()

        reader = csv.reader(q)
        for row_number,row in enumerate(reader):
            if row_number == 0:
                headers += tuple(row)
            else:
                answer = input(row[1])
                data.append({headers[0]: row[0], 'answer': answer})

        add_data(data)

'''
4.
'''

def open_questions(data_to_use, filename, user_match=False):
    new_data = []

    if user_match:
        print("You've already answered our survey!!\n Here are your results:\n")

    with open('questions.csv', 'r') as q:
        reader_two = csv.reader(q)
        
        for row_num,row in enumerate(reader_two):
            if row_num == 0:
                continue
            elif row_num > 0:
                if user_match:
                    if data_to_use[row_num-1]['question_id'] == row[0]:
                        print(f"{row[1]} \t Answer: {data_to_use[row_num-1]['answer']}")
                else:
                    if data_to_use[row_num-1]['question_id'] == row[0]:
                        answer = input(row[1])
                        new_data.append({'interviewee': data_to_use[0]['interviewee'], 'question_id': data_to_use[row_num-1]['question_id'], 'answer': answer})
    if new_data.__len__() > 0:
        return new_data
    else:
        return None

def fn_four():
    with open('answers.csv', '+r', newline='') as a:
        reader = csv.reader(a)

        done = False

        the_interviewee = input("What is your name?")
        headers = ()
        existing_data = []
        some_new_data = []

        for row_num, row in enumerate(reader):
            if row_num == 0:
                headers += tuple(row)
            elif str(row[0]).lower() == str(the_interviewee).lower():
                existing_data.append({headers[0]: row[0], headers[1]: row[1], headers[2]: row[2]})
                done = True
            elif str(row[0].lower() != str(the_interviewee).lower()):
                some_new_data.append({headers[0]: the_interviewee, headers[1]: row[1]})

        if done:
            open_questions(existing_data, a.name, user_match=True)
        else:
            new_data = open_questions(some_new_data, a.name)
            
            fields = ['interviewee', 'question_id', 'answer']
            writer = csv.DictWriter(a, fieldnames=fields)
            writer.writerows(new_data)

'''
5.
'''

def print_survey(data):
    _headers = ()
    _data = []

    with open('answers.csv', 'r') as a:
        _reader = csv.reader(a)
        for row_num, row in enumerate(_reader):
            if row_num == 0:
                _headers += tuple(row)
            else:
                _data.append({_headers[0]: row[0], _headers[1]: row[1], _headers[2]: row[2]})
        
        count = 0

        # while amount_of_rows > -1:
        for row1 in _data:
            print(f"\n\n{row1['interviewee']}'s answer to:\n {count+1}. {data[count]['question']}\n\t {row1['answer']}")
            count += 1
            if count == 2:
                count = 0

def fn_five():
    with open('questions.csv', 'r') as q:
        headers = ()
        data = []

        reader = csv.reader(q)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                headers += tuple(row)
            else:
                data.append({headers[0]: row[0], headers[1]: row[1]})
        print_survey(data)


if __name__ == '__main__':
    print("********* Running the answer for assignemnt 1. ********")
    fn_one()
    print("********* END of the answer for assignemnt 1. ********")

    print("********* Running the answer for assignemnt 2. ********")
    fn_two()
    print("********* END of the answer for assignemnt 2. ********")

    print("********* Running the answer for assignemnt 3. ********")
    fn_three()
    print("********* END of the answer for assignemnt 3. ********")

    print("********* Running the answer for assignemnt 4. ********")
    fn_four()
    print("********* END the answer for assignemnt 4. ********")

    print("********* Running the answer for assignemnt 5. ********")
    fn_five()
    print("********* END of the answer for assignemnt 5. ********")