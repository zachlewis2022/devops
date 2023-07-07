def write_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')


def main():
    filename = input("Enter the label filename: ")
    question = input("Enter the question text: ")
    labeltext= input("Enter labels separated by spaces for the question text: ")
    labels = labeltext.split(" ")
    labelprefix = "__label__"
    labelline = ""
    for label in labels:
        labelline = labelline + labelprefix + label + " " 
    write_to_file(filename, labelline + question)
    print("Label Added")
    

if __name__ == '__main__':
    main()

