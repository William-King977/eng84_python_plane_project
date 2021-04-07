# Python Plane Project
In this project, we are tasked to create a flight management system that allows airport assistants to create and manage flight bookings.

## Introduction
In this project we were asked to design a flight trip booking system for airport staff. The basic requirements
for this were outlined by several user stories. The user stories stated that staff should be able to:

- Create passengers with a name and passport number, so they can be added to a flight
- Create a flight trip with a specific destination.
- Be able to assign and/or change a plane in flight trip by inputting their password so that they can handle the problem.
- Be able to add passengers to flight trip so that they can sell tickets to them.
- Be able to generate a flight attendees list report that lists every passenger's name and passport so that their identity document can be checked.

## Tech Stack and methodologies
For this project we used the following tech stack:

- Python
- SQL lite 

The methodology that we used was:

- Test Driven Development 

## Agile and Scrum

We decided to use a Scrum framework to implement Agile. We created this board using Trello. Our board included:
- A Backlog which would outline what we want to do in the future
- User Stories, highlighting each individual user story along with their acceptance criteria and the definition of done
- Daily sprints with sprint meetings ending with sprint retrospectives.
- A Doing board for what is to be done on the day.
- A Testing board for any code which we need to test.
- A Done board for completed work.
- And finally an Important info board for any important info that we need to keep in my mind.

## Database

## Entity Relationship Diagram
To design the database we used an ERD diagram.
- This helped us visualise the database clearly, seeing how our app would connect to our database, this helped us reduce any errors.

## Git commands
### Pulling code
Execute the following commands if you are pulling the remote repository for the first time.
```
git init
git remote add origin https://github.com/William-King977/eng84_python_plane_project
git pull
```

To pull code any other time, use `git pull`.

### Pushing code
To push changes to a GitHub repository, enter the following:
```
git add .
git commit -m "describe your changes"
git push -u origin branch_name
```

To push specific files, such as README.md, use `git add README.md` instead of `git add .`.

### Branches
#### Viewing branches
 * To view the branches in your local Git repository, type `git branch`. This will only show the branches you have switched to. The output should be similar to what is shown below:
   ```
     main
   * william-branch
   ```
   **Note:** the * denotes the current branch you are working on. 
 * To view the branches on the GitHub repository, type `git branch -r`. The output should be:
   ```
   origin/andrew-branch
   origin/arun-branch
   origin/jordan-branch
   origin/main
   origin/william-branch
   ```

#### Switch branches
To switch to another branch, use `git checkout` as shown below.
```
git checkout branch_name
```

#### Creating branches
To create a new branch, use `git branch` as shown below.
```
git branch -M new_branch_Name
```

### Conflicts
The following deals with a conflict in the README.md file of both the local Git and the remote GitHub repository. The repository is named `test_repo` for this purpose.

Before we assume that there is a conflict, pull the code first by using `git pull`. If there is a conflict, you may get the following message:
```
error: Your local changes to the following files would be overwritten by merge:
        README.md
Please commit your changes or stash them before you merge.
Aborting
```

At this point, add, commit and push your changes. After executing the push command, you may get the following message:
```
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/William-King977/test_repo'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Now, use the `git pull` command to pull the changes from the remote repository (GitHub). This will merge the conflicts. 

Open the file(s) that have conflicts to resolve them. The conflicted sections will be surrounded with `<<<<<<< HEAD`, `>>>>>>>` and separated by `=======` as shown below.
```
<<<<<<< HEAD
* This is different to GitHub, from the local Git repo.
* Who won? Well, we'll find out in June! From Git repo.
=======
* The change on the main branch on GitHub
* Who's going to win WSM 2021? From GitHub test repo
>>>>>>> 327cf2f0e9025400c0a1db24d19ddbd6ae87792a
```

After you feel the conflicts have been resolved, add, commit and push your changes. The GitHub repository should now be updated with the new changes.

## Contributors
 * [Andrew Asare](https://github.com/Andrew-Asare)
 * [Arun Panesar](https://github.com/ArunPanesar42)
 * [Jordan Clarke](https://github.com/JClarke-96)
 * [William King](https://github.com/William-King977)
