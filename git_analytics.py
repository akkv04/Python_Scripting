import git
import os
import shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime

def print_tree(tree,indent=0):
    try:
        for item in tree:
            if(item.type == "tree"):
                print('  ' * indent + f'📁 {item.name}')
                print_tree(item,indent+1)
            else:
                print('  ' * indent + f'📄 {item.name}')
    except:
        print("Error during print_tree function")

def git_clone(repo_url,local_path):
    try:
        if(os.path.exists(os.path.join(os.path.join(local_path,'Python_Scripting'),'.git'))):
            print(".git repo exists, pulling the repo to the latest")
            repo.remotes.origin.pull()
            print("==============================")
            print(repo.git.status())

        else:
            print("git repo doesn't exist")
            print("Cloning the repo")
            git.Repo.clone_from(repo_url,os.path.join(local_path,'Python_Scripting'))
            print("current repo status is")
            print(repo.git.status())
    except:
        print("error during git clone operations")

def basic_repo_details():
    print("===============================================")
    #currently this is for one branch, make changes to go through each branch and get the details
    print("Fetching the repo details")
    print("======Repo_details========")
    total_commits=sum(1 for _ in repo.iter_commits())
    print(f"1.Number of commits ={total_commits}")
    print(f"2.Number of branches = {len(repo.heads)}")
    contributors=set(commit.committer.email for commit in repo.iter_commits())
    print(f"3.Number of contributors= {len(contributors)}")

def analyze_repository():
    
    #function to find the most active contributor and their stats
    contributor_stats={}

    #iterating through the commits
    for commit in repo.iter_commits():
        # Extract the author's email from the commit
        author_email=commit.author.email

        #commit.author.name = commitname
        #commit.author.email = commit email
        #commit.authored_datetime = commit date time
        #commit.message = commit message
        #commit.hexsha = commit sha value

        contributor_stats.setdefault(author_email,{'commits':0,'lines_added':0,'lines_deleted':0})
        contributor_stats[author_email]['commits'] += 1

        # # Retrieve diff statistics for the commit
        diff_stats = commit.stats.total
        
        contributor_stats[author_email]['lines_added'] += diff_stats['insertions']
        contributor_stats[author_email]['lines_deleted'] += diff_stats['deletions']
        
    print(contributor_stats)
     # Sort contributors by total commits
    sorted_contributors = sorted(contributor_stats.items(), key=lambda x: x[1]['commits'], reverse=True)

    #Printing the most active contributor
    for contributors,stats in sorted_contributors[:5]:
        print(f"contributer name: {contributors}, author_commits:{stats['commits']}, lines added:{stats['lines_added']}, lines deleted {stats['lines_deleted']} ")
     
     # Plot the commit timeline
    plot_commit_timeline(repo)

def plot_commit_timeline(repo):
    commit_dates = [commit.authored_datetime for commit in repo.iter_commits()]
    commit_dates.sort()
    
    print("Commit Dates:", commit_dates)
    plt.figure(figsize=(10, 6))
    plt.plot_date(commit_dates, range(len(commit_dates)), '-')
    plt.title('Git Commit Timeline')
    plt.xlabel('Commit Date')
    plt.ylabel('Number of Commits')
    plt.grid(True)
    plt.show()
    
    # Save the plot to a file (optional)
    plt.savefig('commit_timeline.png')

    # Clear the figure to release resources (optional)
    plt.clf()



print(f"current working directiory is {os.getcwd()}")

print("Cloning the repo")
repo_url="https://github.com/akkv04/Python_Scripting.git"
local_path=f"{os.getcwd()}"
print(f"local path is {local_path}")

git_clone(repo_url,local_path)
repo=git.Repo(os.path.join(local_path,'Python_Scripting'))

#to get the tree, we need the latest commit of the repo
latest_commit=repo.head.commit
print(f"the latest commit is {latest_commit}")
#from the latest commit, we are getting the tree
latest_commit_tree=latest_commit.tree

#calling the print_commit_tree_function
print("==========================================")
print("*******************************************")

print_tree(latest_commit_tree)


print("getting the basic repo details")
basic_repo_details()


#Most active contributors and contributions in a graphical format
analyze_repository()
