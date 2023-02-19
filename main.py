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
#controllare meglio che un comando sia andato a buon fine controllando anche sterror,
#nel caso ci sia un errore bisogna stamparlo, e usare i try per non fermare il programma

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
      



 

def fast_push(dir_path : str, force:int = 0):
  
    git_repo_run(dir_path,"add",".")
    git_repo_run(dir_path,"commit", "-m" , datetime.now().strftime("%m-%d %H:%M") )

    if remote_presence(dir_path) == 1:
        if force ==0:
            temp = git_repo_run(dir_path, "push")
        if force == 1:
            temp = git_repo_run(dir_path, "push", "-f")
       



Remote_Add(dir_path,"origin", "https://github.com/GiuseppeGambacorta/GitEase.git")
prova = remote_presence(dir_path)
print(prova)


fast_push(dir_path,1)

