import git
import os
import shutil

os.getcwd()
os.makedirs('/home/ec2-user/akhil',exist_ok=True)
os.chdir('/home/ec2-user/akhil')

repo_url="https://github.com/akkv04/Python_Scripting.git"
local_path="/home/ec2-user/akhil/Python_Scripting"
branch_name="release/1.0"
try:
    if(os.path.exists(os.path.join(local_path,'.git'))):
        print(".git repo exits")
        print("Pullign the branch to get the latest changes")

        # Open the Git repository
        repo=git.Repo(local_path)

        #Pulling from the remote
        # Pull changes from the remote repository and capture the output

        print("Pullign the remote changes")
        repo.remotes.origin.pull()

        print("checking out the branch")
        #checking out a branch
        repo.git.checkout(branch_name)

        #checking the git status
        print(repo.git.status())


        print("Copying the test.py")
        shutil.copy2('/home/ec2-user/test.py',f'{local_path}/gitpython/test.py')


        print("adding the file")
        #Adding all the changes to index
        # Add all changes to the index
        repo.git.add('.')

        print(repo.git.status())

        print("Committng the changes")
        #commit the changes
        commit_message="Pushing from the EC2 instance using pyton script"
        repo.index.commit(commit_message)

        print("Pushing to the remote")
        try:
          #Pushing to the remote
            remote_name = 'origin'
            repo.remotes[remote_name].push()
        except:
            print("error during git push")

    else:
        print("cloning new repo")
        git.Repo.clone_from(repo_url,local_path)


except:
    print("Error during git clone operations")
                                                      
