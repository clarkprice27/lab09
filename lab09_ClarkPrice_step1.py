import random


def convert_file_to_list(file):
    """converts open file into list with tuples"""

    questions = []

    for i, line in enumerate(file):
        if i%3 == 0 or i%3 == 2:
            line = line.split(' \n ')
            line[-1] = line[-1].replace('\n','')
            questions.extend(line)
        if i%3 == 1:
            line = line.split('._')
            line[-1] = line[-1].replace('\n','')
            line = list(line)
            questions.append(line)
        
    file_list = []
    x = 0

    while x < len(questions)-1:
        file_list.append((questions[x],questions[x+1],questions[x+2]))
        x += 3

    return file_list


def open_file():
    """opens the file and sends to conver to list"""

    try:
        file = open('Qsand0pts.txt', 'r')
    except IOError:
        print('Qsand0pts.txt does not exist')
                
    file_list = convert_file_to_list(file)
    return file_list


def print_questions(file_list):
    """prints the questions formatted for the screen"""
    
    question_num = 1
    for question in file_list:
        print('{}. {}'.format(question_num,question[0]))

        answer_num = 1
        for answer in question[1]:
            print('{:>5}){:3}{:s}'.format(answer_num,'',answer))
            answer_num += 1

        question_num += 1


def create_name_dictionary(names_file):
    """creates dictionary with students names and random questions"""

    assigned_questions = {}

    for name in names_file:
        name = name.replace('\n', '')
        
        rand_set = set()
        
        seed = random.randint(2,27)
        random.seed(seed)
        
        for x in range(0,5):
            rand_set.add(random.randint(1,28))
        assigned_questions[name] = sorted(rand_set)
        
    print(assigned_questions)


def main():
    """executes the program"""
    
    file_list = open_file()
##    print_questions(file_list)
    try:
        names_file = open('names.txt', 'r')
    except IOError:
        print('names.txt does not exist')
    create_name_dictionary(names_file)
    
    

main()





