'''
1.
'''
import csv
import random
import re
import copy

def more_questions():
    another_question = input("Would you like to have another question on the survey? Please type 'yes' or 'no'.\n")
    stopper = True

    while stopper:
        if another_question.lower() == "yes" or another_question.lower() == "no":
            break
        else:
            print("Please type 'yes' or 'no'. Thank you.")
            another_question = input("Would you like to have another question on the survey? Please type 'yes' or 'no'.\n")

    count = None

    if another_question == "yes":
        stop = True
        while stop:
            count = input("How many questions would you like to add?\n")
            try:
                count = int(count)
                stop = False
            except ValueError:
                print("Please type a number without a decimal.")
        
        new_questions = []

        while count > 0:
            

            new_question_ = input("Please type your question.\n")

            while len(new_question_) > 30 or len(new_question_) < 10:
                print("Question does not meet required length. Please retry.")
                new_question_ = input("Does not meet valid question parameters. What question would you like to ask?\n")

            q_id = random.randint(30, 100)
    
            for item in data:
                while int(item['question_id']) == q_id:
                    q_id = random.randint(30,100)

            new_questions.append({'question_id': q_id, 'question': new_question_})

            count -= 1

        with open("questions.csv", 'a', newline='') as question_add:
            writer = csv.DictWriter(question_add, fieldnames=headers)

            writer.writerows(new_questions)


def fn_one():

    '''
    Opens file, loops thru and splits between column headers and data, each into lists.
    Loops thru the data, gathers a response from the user, validates the response based upon a conditional.

    Loops thru data again, gathers a response from the user, validates the response based upon a conditional - removes the element in the list if necessary.

    We then write the data to our file.


    Leverage function more_questions() to gather more user input, based upon that input and the amount of questions they'd like to add we create a sequence of dictionary mappings for a new question. Prior to adding the data to the sequence we run some validataions.

    We then write the data to our file

    '''

    headers = []
    data = []

    with open('questions.csv', 'r') as q:
        reader = csv.reader(q)

        for row_num, row in enumerate(reader):
            if row_num == 0:
                headers += row[0],row[1]
            else:
                data.append({'question_id': row[0], 'question': row[1]})

    for item in data:
        print(f"One of the current questions in the survey is:\n {item['question']}")
        response = input(f"\nHow satisfied are you with this question? Please type 'yes' or 'no'.\n")

        if response.lower() == "yes":
            continue
        else:
            new_question = input("What question would you like to ask in place of the question you are not satisfied with?\n")
            while len(new_question) > 30 or len(new_question) < 10:
                print("Question does not meet required length. Please retry.")
                new_question = input("What question would you like to ask in place of the question you are not satisfied with?\n")
            item['question'] = new_question

    for item_ in data:
        is_needed = input(f"Is '{item_['question']}' a question that you want to keep?\n")
        flagger = True

        while flagger:
            if is_needed.lower() == "yes" or is_needed.lower() == "no":
                break
            else:
                print("Please type 'yes' or 'no'. Thank you.")
                is_needed = input(f"Is '{item_['question']}' a question that you want to keep?\n")
        
        if is_needed.lower() == "no":
            double_check = input(f"Are you sure you want to remove the question:\n '{item_['question']}'\n")
            
            if double_check.lower() == "yes":
                data.remove(item_)



    with open("questions.csv", "w", newline='') as new:
        writer = csv.DictWriter(new, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    #Function for more questions
    more_questions()

'''
2.
'''

def get_question_id_data(filename):
    data = []
    with open(filename, 'r', newline='') as q:
        reader = csv.DictReader(q)
        for row_num,row in enumerate(reader):
            if row_num == 0:
                pass
            else:
                data.append({'question_id': row['question_id'], 'question': row['question']})
    
    return data


def write_final(filename, data, columns):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

def fn_two():

    '''
    Setup an email to validate against. 
    Setup sequences to store data - headers, & row data.

    Open file, loop & store data in sequence via dictionary mapping, loop again for validation of email using the answer key of the dictionary mapping.

    Gather the question data via function get_question_id_data(), create a list comprehension specifically for the answer sheet question ids to validate against the question sheet question ids.

    Check any unanswered questions and get the user input, leverage write_final() function to write back to the answers sheet.
    '''

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    answer_headers = []
    answer_data = []

    with open('answers.csv', 'r', newline='') as a:
        reader = csv.reader(a)

        for row_num, row in enumerate(reader):
            if row_num == 0:
                answer_headers += row[0],row[1],row[2]
            else:
                answer_data.append({'interviewee': row[0], 'question_id': row[1], 'answer': row[2]})
        
    for item in answer_data:
        if str(item['answer']).__contains__('@'):
            while not EMAIL_REGEX.match(item['answer']):
                print(f"Your email listed as {item['answer']} is invalid.")
                item['answer'] = input("Please add a valid email address.\n")
    
    all_questions = get_question_id_data('questions.csv')
    all_answers = [item['question_id'] for item in answer_data]

    for item in all_questions:
        if item['question_id'] not in all_answers:
            unanswered = input(f"{item['question']}\n")
            answer_data.append({'interviewee': answer_data[0]['interviewee'], 'question_id': item['question_id'], 'answer': unanswered})
    
    write_final('answers.csv', answer_data, answer_headers)


'''
3.
'''
def fn_three():

    '''
    Open questions, get the headers and the row data into seperate sequences.

    Repeat that action with the answers sheet.

    Sort the answer data & create a copy.

    Loop thru the copy and read the questions and answers if the question ids of each respective sequence match - if they dont, then create a new sequence on the original data where that answer that does not have a matching question gets removed.

    Write the data back to answers sheet with all superfluous data removed.
    '''
    with open('questions.csv', 'r', newline='') as q:
        reader = csv.DictReader(q)
        question_data = [{'question_id': row['question_id'], 'question': row['question']} for row in reader]
    question_headers = list(question_data[0].keys())

    with open('answers.csv', 'r', newline='') as a:
        reader = csv.DictReader(a)
        answer_data = [{'interviewee': row['interviewee'], 'question_id': row['question_id'], 'answer': row['answer']} for row in reader]
    answer_headers = list(answer_data[0].keys())

    answer_data = sorted(answer_data, key=lambda k: k['interviewee'])
    answer_data_copy = copy.deepcopy(answer_data)

    for item in range(len(answer_data_copy)):
        
        if answer_data_copy[item]['question_id'] in [value['question_id'] for value in question_data]:
            print(f"{str(answer_data_copy[item]['interviewee']).title()}'s answer to {str([question['question'] for question in question_data if question['question_id'] == answer_data_copy[item]['question_id']]).replace('[','').replace(']','')} is:\n {answer_data_copy[item]['answer']}")

        elif answer_data_copy[item]['question_id'] not in [value['question_id'] for value in question_data]:
            print(f"invalid answer at: {answer_data_copy[item]['question_id']} from the interviewee, {answer_data_copy[item]['interviewee']} \n ***** NOW DELETING FROM ANSWERS ******")
            answer_data = [answer for answer in answer_data if answer['question_id'] != answer_data_copy[item]['question_id']]

    with open('answers.csv', 'w', newline='') as final:
        writer = csv.DictWriter(final, fieldnames=answer_headers)
        writer.writeheader()
        writer.writerows(answer_data)

if __name__ == '__main__':
    print("********* Running the answer for assignemnt 1. ********")
    fn_one()
    print("********* END of the answer for assignemnt 1. ********")
    print("********* Running answer for assignment 2 **********")
    fn_two()
    print("********* End of assignment for assignment 2 *********")
    print("********* Running answer for assignment 3 **********")
    fn_three()
    print("********* End of assignment for assignment 3 *********")
