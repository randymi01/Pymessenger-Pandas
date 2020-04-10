import os


#goal: change directory to folder inside of the text-emailer which contains a csv file

def getcsvdir():
    cwd=os.getcwd()
    csvexist=False
    for root, dirs, files in os.walk(cwd, topdown=False):
        for name in files:
            file = list(os.path.join(root,name))
            if file[len(file)-3:]==['c','s','v']:
                csvfile=''.join(file)
                csvexist=True
                return os.path.dirname(csvfile)
    if csvexist is False:
        print('\nNo CSV file found')
        x=input()

dir=getcsvdir()
os.chdir(dir)

#os.path.exanduser('~/'+'')
#turns ~ into default user. same as join but can comprehend
