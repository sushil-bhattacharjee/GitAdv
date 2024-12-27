# Question: A developer has issued the git add file1 file2 test.py command to add three files for the next commit 
# but then decides to exclude test.py from this commit. Which command needs to be used to exclude test.py from this 
# commit but keep the
rest of the files?

A. git stash -- file1 file 2
B. git clean -- test.py
C. git checkout -- file1 file2
D. git reset -- test.py

Ans: git reset -- test.py

##### 

sushil@sushil:~/GitAdv$ git status
On branch main

Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file.txt
        file2.txt
        test.py

nothing added to commit but untracked files present (use "git add" to track)
######
sushil@sushil:~/GitAdv$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   file.txt
        new file:   file2.txt
        new file:   test.py

############

sushil@sushil:~/GitAdv$ git reset -- test.py
sushil@sushil:~/GitAdv$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   file.txt
        new file:   file2.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.py