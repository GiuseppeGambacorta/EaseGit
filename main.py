import subprocess
import os
import copy
from datetime import datetime



# copy
# os path
# sub process run
# * args
# paramemtri funzione definire il tipo
#datetime

#nomi giusti a funzioni...oggetto_facose()
#che cosa ritornare quando eseguo o leggo lo stato di certe cose?

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)



def git_run( *args : str):
    gitargs = ["git"] 
    
    for arg in args:
        gitargs.append(arg)

    temp = subprocess.run(gitargs, capture_output=True, text=True)
    result = copy.copy(temp)
    
    result.stdout = result.stdout.strip()
    result.stderr = result.stderr.strip()
    return result



def git_repo_run(dir_path: str, *args : str):

    gitargs = ["git", "-C", dir_path] #standard call for subprocess.run, -C is for work in another directories  
    
    for arg in args:
        gitargs.append(arg)

    temp = subprocess.run(gitargs, capture_output=True, text=True)
    result = copy.copy(temp)
    
    result.stdout = result.stdout.strip()
    result.stderr = result.stderr.strip()
    return result


def git_is_there(dir_path : str):

    temp = git_repo_run(dir_path,"rev-parse","--git-dir")
    
    if temp.returncode == 0 and temp.stdout == ".git":
        return 1
    else:
        return 0


def git_init(dir_path : str):
    if git_is_there(dir_path):
        return 0

    return git_repo_run(dir_path,"init")



 
def get_name_and_email():
    name =  git_run("config","--global", "user.name")  
    email = git_run("config","--global", "user.mail")  
   

    if not email.returncode and not name.returncode:
        list = []
        list.append("name: "+ name.stdout)
        list.append("email: "+ email.stdout)
        return list


def set_name_and_email(name : str, email : str):
    nameresponse = git_run("config","--global", "user.name" , name)  
    emailresponse=  git_run("config","--global", "user.email", email)  

    if not emailresponse.returncode and not nameresponse.returncode:
        return 0
    else:
        return -1



def remote_presence(dir_path : str):
   temp = git_repo_run(dir_path, "remote")

   if temp.returncode == 0 and temp.stdout:
        return 1
   else:
        return 0
   


def Remote_Add(dir_path : str , remotename : str , url: str):
  
   if  remote_presence(dir_path) == 0:
        temp = git_repo_run(dir_path,"remote", "add", remotename , url)
        print("porcodio")



 

def fast_push(dir_path : str):
    git_repo_run(dir_path,"add",".")
    git_repo_run(dir_path,"commit", "-m" , datetime.now().strftime("%m-%d %H:%M") )

    if remote_presence(dir_path) == 1:
        git_repo_run(dir_path, "push")


Remote_Add(dir_path,"origin", "https://github.com/GiuseppeGambacorta/GitEase.git")
prova = remote_presence(dir_path)
print(prova)


fast_push(dir_path)

# Check if the .git directory exists
#result = subprocess.run(["git", "-C", dir_path, "rev-parse", "--git-dir"], capture_output=True, text=True)

'''

set_name_and_email("Giuseppe Gambacorta", "gambacortagiuseppe@outlook.it")

wewe = get_name_and_email()
print(wewe[0])




git_init(dir_path)
result = git_is_there(dir_path)

print(result)





result = subprocess.run(["git", "-C", dir_path, "remote" ], capture_output=True, text=True)

print(result.returncode)
print(result.stdout)


url = "https://github.com/GiuseppeGambacorta/GitPython.git"

if result.returncode == 0 and result.stdout:
    print("esiste")
else:
    print("non esiste")
    result = subprocess.run(["git", "-C", dir_path, "remote","add" , "origin" , url ], capture_output=True, text=True)
    

subprocess.run(["git", "-C", dir_path, "add", "."], capture_output=True, text=True)
subprocess.run(["git", "-C", dir_path, "commit", "-m", "provasubprocess"], capture_output=True, text=True)
subprocess.run(["git", "-C", dir_path, "push", "-f"], capture_output=True, text=True)


result = subprocess.run(["git","-C",dir_path, "status"], capture_output = True, text=True)

print(result.stdout)
'''