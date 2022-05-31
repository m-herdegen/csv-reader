#import data

def csv_reader():
    # take user input
    user_input = input("Please type in either cats or dogs: \n")

    # handle bad input
    # if ('cats' not in user_input) and ('dogs' not in user_input):
    #     raise Exception(f"Sorry, we don't have any {user_input} here.")
    file_test = 'data/' + user_input + ".csv"

    # with open(file_test, 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    # for row in csv_reader:
    #     print(row[0])
    
    try:
        open(file_test)
    except:
        print(f"Sorry, we don't have any {user_input} here.")

    # display information about the animal
    return False

csv_reader()