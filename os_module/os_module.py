import os

#current working directory - os.getcwd()
print(f"current working directory is {os.getcwd()}")

#change the working directory - os.chdir()
os.chdir(os.path.join(os.getcwd(),"git_analytics_dashboard/Python_Scripting"))

#join two path - os.path.join(a,b)

print(f"new working dir is {os.getcwd()}")

#os.listdir() -function returns a list containing the names of the entries (files and directories) in the specified directory
print(f"Contents of the directory {os.getcwd()} is")
entries=os.listdir(os.getcwd())
for entry in entries:
    print(entry)

#Creating a new directory - os.mkdir() and os.makedirs()
#os.makedirs() creates all the directories in the specified path, including any parent directories that do not exist. On the other hand, os.mkdir() only creates the specified directory and expects that its parent directories already exist. If the parent directories are not present, os.mkdir() will raise a FileNotFoundError.

#exist_ok=True - if the folder already exists, it wont throw any error and will proceed
os.makedirs(f"{os.getcwd()}/test_user",exist_ok=True)

#remove a directory
os.rmdir(f"{os.getcwd()}/test_user")

#os.remove() function in Python is used to remove or delete a file. It takes a file path as an argument and attempts to delete the specified file.
#we will create a file and then proceed to delete the same.

try:
    file_path=f"{os.getcwd()}/testing.txt"
    print(f"Creating file {file_path}")

    # Use open() with mode 'w' (write) to create a new file
    with open(file_path,'w') as file:
        file.write("writing contents to newly created file")
        file.write("\n second line")

    # File is closed automatically when the 'with' block is exited
    
    print(f"file {file_path} created succesfully")



except PermissionError:
    print(f"Permission denied while creating {file_path}")
except Exception as e:
    print(f"exception occured : {e}")


#deleting the file created
#os.remove(file_path)

#os.path.join(a,b,c) - joins file
#os.path.exists() - Returns true if the path exists

if(os.path.exists(f"{file_path}")):
    print("file exists")
else:
    print("file doesnt exist")

#os.path.isfile(path): Returns True if the specified path is a regular file.

if(os.path.isfile(file_path)):
    print(f"{file_path} is a file")

#os.path.isdir(path):Returns True if the specified path is a directory.
if(os.path.isdir(f"{file_path}")):
   print(f"{file_path} is a directory")
else:
   print(f"{file_path} is not a directory")

if(os.path.isdir(os.getcwd())):
   print(f"{os.getcwd()}\tis a directory")


#os.path.abspath(path): Returns the absolute version of a path.
print(f"absolute path of f{file_path} is {os.path.abspath(file_path)}")


#os.path.basename(path):Returns the base name of a path.
print(f"base name of {file_path} is {os.path.basename(file_path)}")

#os.path.dirname(path):Returns the directory name of a path.
print(f"the directory name of {file_path} is {os.path.dirname(file_path)}")

#os.path.split(path):Returns a tuple containing the directory name and the base name of a path.
directory,base_name = os.path.split(file_path)
print(f"directory is {directory}")
print(f"base name is {base_name}")


#os.path.splitext(path):Returns a tuple containing the root and the extension of a file path.
root,extension=os.path.splitext(file_path)
print(root)
print(extension)


#display file content
with open(file_path,'r') as file:
    content=file.read()

print(content)

#read one line
with open(file_path, 'r') as file:
    content=file.readline()
print(content)


#append one line
with open(file_path,'a') as file:
          file.write("\nappended file")
          
with open(file_path,'r') as file:
    content=file.read()

print("new contents after appending is")
print(content)


for root,dirs,files in os.walk(os.getcwd(),followlinks=False):
    # 'root' is the current directory being processed
    # 'dirs' is a list of subdirectories in 'root'
    # 'files' is a list of files in 'root'

    # Perform actions on files or directories as needed
    # ...
    #print(f"root:{root}")
    #print(f"dirs: {dirs}")
   # print(f"files:{files}")
    print("ab")
    #output
  #  root:/home/ec2-user/git_analytics_dashboard/Python_Scripting
    #dirs: ['.git', 'gitpython']
    #files:['README.md', 'git_analytics.py', 'testing.txt']
    #root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git
#dirs: ['branches', 'hooks', 'info', 'refs', 'objects', 'logs']
#files:['description', 'HEAD', 'config', 'packed-refs', 'index', 'FETCH_HEAD', 'ORIG_HEAD', 'COMMIT_EDITMSG']
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/branches
#dirs: []
#files:[]
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/hooks
#dirs: []
#files:['applypatch-msg.sample', 'commit-msg.sample', 'post-update.sample', 'pre-applypatch.sample', 'pre-commit.sample', 'pre-merge-commit.sample', 'pre-push.sample', 'pre-receive.sample', 'push-to-checkout.sample', 'update.sample', 'fsmonitor-watchman.sample', 'pre-rebase.sample', 'prepare-commit-msg.sample']
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/info
#dirs: []
#files:['exclude']
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/refs
#dirs: ['heads', 'tags', 'remotes']
#files:[]
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/refs/heads
#dirs: []
#files:['main']
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/refs/tags
#dirs: []
#files:[]
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/refs/remotes
#dirs: ['origin']
#files:[]
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/refs/remotes/origin
#dirs: []
#files:['HEAD', 'main']
#root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/objects
#dirs: ['pack', 'info', 'eb', '71', '5c']
    #files:[]
    #root:/home/ec2-user/git_analytics_dashboard/Python_Scripting/.git/objects/pack
    #dirs: []

    # prints all the fils along with the path
    for root, dirs, files in os.walk(os.getcwd(),followlinks=False):
        for file in files:
            #file_path = os.path.join(root,file)
            #print(file_path)
            if file.endswith(".txt"):
                print(os.path.join(root,file))





