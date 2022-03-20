from fileinput import filename
import os

root_dir = []

def main():
    try:
        for i in os.listdir():
            if i.endswith('.lst'):
                root_dir.append(i.replace('.lst', ''))
    except Exception:
        fname=''
        while(fname not in 'Qq'):
            fname = input("Enter an lst file name('Q' to finish): ")
            root_dir = root_dir+[fname] if not fname.endswith('.lst') else root_dir+[fname.replace('.lst', '')]
            fname = root_dir[-1]

    
    global filename
    filename = input()

    show()
    inp = input("\n")
    if inp in 'Aa':
        add()
    elif inp in 'Dd':
        delete()
    elif inp in 'Qq':
        quit()
    else:
        print("\nEnter a valid input: ")
        show()
    
def show():
    #this is a change.