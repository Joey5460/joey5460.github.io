Get Started
-----------

git init : first time of using git

git add .

git ls-files

git status

git commit -am "message"

git log

git reset --hard

git push
    - git push origin master
    - git push --force origin master

git branch
    - git branch -v
    - git branch -D
    - git branch -d (safe if not merged)


git checkout
    - git checkout -b

git merge remote_branch_name
 
git request-pull https://stackoverflow.com/questions/34945947/git-request-pull-how-to-create-a-github-pull-request-on-the-command-line

gti rm filename

git clean -f -d

git config --global user.name "zhouyu"
    - git config --global user.email "zhouyu5460@gmail.com"

git clone 
   - git clone https://github.com/Joey5460/joey5460.github.io.git 

git archive (archive0_)
    - git archive --format zip --output /full/path/to/zipfile.zip master 


.. _archive0: https://stackoverflow.com/questions/160608/do-a-git-export-like-svn-export#163769

Progressive
-----------
git config 
    - git config --list ------check
    - .gitconfig ------config file 

git add -u: update

git commit --amemd -m "message"
    - git commit HEAD@{1}  (commit0_) 

git push origin --delete <branch_name>

git checkout
    - git checkout --patch branch_name path (merge0_)  
    - git checkout branch_name file_path (merge0_)  
    - git checkout HEAD -- my-file.txt (checkout0_)
    - git checkout branch_name -- dirname (checkout1_) 

git diff
    - git diff 0da94be  59ff30c
    - git diff branchA branchB -- file (diff0_)
    - git diff --name-status master..yourBranchName (diff1_)
git apply 
    - git apply -3 patch.diff (apply0_)

.. _apply0: https://stackoverflow.com/questions/15993861/git-create-patch-with-diff

git tag tagname
    - git tag --delete tagname

git reset HEAD^/HEAD~1
    - git reset --hard 59ff30c (reset0_)

git describe --abbrev=0 --tags (describe0_) 

git config credential.helper store

git mergetool (conflict0_ conflict1_ mergetool0_) 
  - :diffg RE  " get from REMOTE
  - :diffg BA  " get from BASE
  - :diffg LO  " get from LOCAL
  - ]c --- Jump to the next change.
  - [c --- Jump to the previous change. 

git init --bare (for center server) 

git submodule
    - git submodule init
    - git submodule update
    - git submodule add repo_url

git remote
    - git remote rename
    - git remote remvoe

git clone      
   - git clone  ssh://zhouyu5460@127.0.0.1:2222/~/ex4 (clone0_)

.. _clone0: https://stackoverflow.com/questions/5767850/git-on-custom-ssh-port#5767880
.. _commit0: http://stackoverflow.com/questions/6759791/how-do-i-move-forward-and-backward-between-commits-in-git
.. _conflict0: https://stackoverflow.com/questions/161813/how-to-resolve-merge-conflicts-in-git#163659 
.. _conflict1: http://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/
.. _describe0: http://stackoverflow.com/questions/1404796/how-to-get-the-latest-tag-name-in-current-branch-in-git
.. _merge0: https://stackoverflow.com/questions/18115411/how-to-merge-specific-files-from-git-branches#33168094
.. _diff0: https://stackoverflow.com/questions/4099742/how-to-compare-files-from-two-different-branches 
.. _diff1: https://stackoverflow.com/questions/822811/showing-which-files-have-changed-between-two-revisions#822859
.. _checkout0: https://stackoverflow.com/questions/7147270/hard-reset-of-a-single-file#7147320
.. _checkout1: https://stackoverflow.com/questions/2668886/git-copy-all-files-in-a-directory-from-another-branch#2668947
.. _reset0: https://stackoverflow.com/questions/4114095/how-to-revert-git-repository-to-a-previous-commit
.. _mergetool0: https://gist.github.com/karenyyng/f19ff75c60f18b4b8149

More
====

- git filter-branch_  --index-filter \
    'git rm --cached --ignore-unmatch path/to/mylarge_50mb_file' \
    --tag-name-filter cat -- --all

.. _filter-branch: https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery#Removing-Objects

Delete
======
- git push origin --delete <branch_name>
- git branch -D branch_name

Q&A：
=====
Q: `How to remove file from historical commit <https://stackoverflow.com/questions/8740187/git-how-to-remove-file-from-historical-commit>`_
A:

.. code-block::

    git filter-branch --index-filter \
        'git rm --cached --ignore-unmatch path/to/mylarge_50mb_file' \
        --tag-name-filter cat -- --all

Q: `You can undo git add before commit with <http://stackoverflow.com/questions/348170/how-to-undo-git-add-before-commit#348234>`_
A: git reset filename
