# Final project - DT042G

## Instructions for running the program

This is a version of the classic Hangman game, built with a GUI and MVC architecture. When starting the game, there are two menu buttons - “Play” and “Exit”. Press Play to start a new game. A random word will be selected from the other/words.json file - and you will have 8 tries to guess the correct word - either by entering a single letter and slowly progressing towards filling out the entire word - or by boldly guessing the whole word. If you try to guess the whole word and guess wrong though, you lose instantly. After winning/losing press Play again to start a new game. At any point - you can exit the program by pressing “Exit”.

### Running the program
The program can be executed by moving into the project folder and typing any of the listed commands below. Which one is correct depends on your Python installation and OS:

```python3.11 -m src.hangman```
```python3 -m src.hangman```
```python -m src.hangman```
```py -m src.hangman```

## Environment & Tools
> - **Language**: Python
> - **Version control**: Git
> - **Testing framework**: Unittest
> - **Project management tool**: Trello

### Samuel Thand

> - **OS**: Ubuntu 20.04
>- **IDE**: PyCharm 2021.2.1 (Professional Edition)
>- **Language**: Python version: 3.11
>- **Version control**: Git version: 2.25.1

### Tobias Hansson

#### System 1: Laptop

> - **OS**: Windows 10 Home (64-bit)
>- **IDE**: PyCharm 2022.3.2 (Professional Edition)
>- **Language**: Python version: 3.11
>- **Version control**: Git version: 2.33.0.windows.2

#### System 2: Desktop

> - **OS**: Windows 10 Home (64-bit)
>- **IDE**: PyCharm 2022.3.2 (Professional Edition)
>- **Language**: Python version: 3.11
>- **Version control**: Git version: 2.30.1.windows.1

## Purpose

The purpose of this project is to utilize tools and methods used in collaborative software development while developing a hangman game in python. We aim to utilize the principles of Test Driven Development (TDD) methodology, feature branch workflow, documentation, and collaboration while sticking to the guidelines and conventions provided by the course. To manage our project, we will use Trello, which enables us to create a Kanban board to lay out the plan and structure the workflow during development.

The Kanban board must initially be set up with at least five different lists; Manifest, Backlog, In progress, Review, and Completed. Manifest will contain details about the conventions to follow while working on this project including; general information about the project, git and Trello workflow, coding workflow, task guidelines, peer review guidelines, code conventions, and documentation guidelines. This will provide a quick reference to the team members about the project workflow and its requirements. The backlog contains all the tasks that need to be completed in the project. In progress contains the tasks that are currently being worked on by the team members. The review contains tasks that have been completed and are ready for review. Completed contains the tasks that have been successfully reviewed and merged into the master branch.

During application development, test-driven development methodology should be followed to ensure that the production code meets the requirements and that errors and bugs can be caught early in the process. A feature branch workflow should also be followed and the branches should have a connection to the tasks they are related to.

The concrete goals were:

* Work in a pair
* Java or Python project
* Unittesting with unittest module for Python
* The solution needs to compile and be functional
* Kanban board for the project with sections:
  * Manifest
    * General information
    * Git workflow
    * Coding workflow
    * Task guidelines
    * Peer review guidelines
    * Code conventions
    * Documentation guidelines
  * Backlog
  * In Progress
  * Review
  * Complete
* Information stated in the different manifest cards needs to be adhered to during the project development
* Git feature branch workflow, with pull requests and peer reviews
* The kanban board needs to show the state of the project throughout development
* Test driven development with tests developed first
* Full test coverage
* Commit messages with body and header
* Separate production code from tests

## Procedures
### Project management
The project was managed using Trello, with every action step in the development mirrored by a step taken on the board. For tasks in the project, we had four different cards:

* Feature
* Patch
* Technical
* Issue
 
Feature was used to describe new features for the program, the patch was for patches that needed to be done, technical for meta-tasks regarding project structure or other similar tasks, and the issue was for bugs that had arisen.

According to our described procedure, the general workflow was that for each idea for new tasks - a card was made and placed in the backlog list. Here the cards could be fleshed out and ironed out as the ideas for features or other tasks matured. When a card felt complete and contained enough information to allow for the development, it would be owned by one team member (member joins the card) which would move it to the in-progress list to imply that the card owner has started the development process for that task.

When the development of a task had reached a state where it was ready to enter production, the card was moved to the review list so that a peer could handle it. If the peer agreed upon the task completion and that it correctly fulfilled the requirements, it was moved to the complete list. However, if the peer did not find the requirement to be fulfilled, an issue tag was added to the card and it was put back into the backlog list.

As each card represented a task that should be performed in the project, they had to be correlated somehow to a branch in git. Therefore, each card was named in the form of a section/task and the branch related to that task was created with the same name. A link would also be added to the card which pointed to that branch in bitbucket for easy access.

One problem that arose was that sometimes, a feature would not be fully completed before it was moved to In progress. This resulted in a card having to be updated while in progress, which was not as intended. This issue was minimized for coming tasks by spending more time thinking about the design and ensuring a task had matured fully before starting to work on it. 

### Git workflow
We followed the specified feature branch workflow as follows, where all merges to the master branch were done via pull requests on Bitbucket.



As the figure implies, each git branch had a close relation to a task in Trello. Therefore, each branch was named after that corresponding task so that it could be easily found and switched to. This also helped to ensure that the work was properly organized and tracked throughout the development process.

As part of this workflow, each commit made by the developer included a header to give a quick summary of the changes made and a body to describe the changes in more detail. This provided a clear and concise summary of the changes being made while also improving the readability and maintainability of the codebase.

### Feature branch and pull requests
One problem that arose was trying to merge a feature branch after the master branch had moved forward from other merged feature branches - resulting in merge conflicts in the master branch. To resolve these conflicts, the forwarded master commit had to be pulled into the feature branch and the conflict resolved - before a new pull request would be submitted. This was a new way of resolving merge conflicts. To make this issue less frequent - more afterthought was put into how to divide the work and try to work on tasks that wouldn't be as likely to result in conflicts. 

### Collaboration
Before starting to work, a basic design was made to ensure that all team members would pull in the same direction and have a general idea of what the result should look like, and have a basic understanding of the required functionality, components, and how these would interplay. 

We then divided the work between the members as we went along, and selected tasks freely from the backlog. Continuous communication was kept at all times before starting to work on a task, about creating new features or making other changes to the project to make sure all members knew what was going on and could raise concerns if needed. We also made sure that another member was also able to do peer review and merge/decline pull requests on somewhat short notice to keep the project rolling without major stops because of bottlenecks in the review process. We sometimes agreed to work on-site for determined hours, and sometimes worked asynchronously from home/at school because of personal reasons and other commitments. 

The resulting share of work was in Tobias writing the majority of the backend logic, Samuel the majority of the GUI and MVC architecture and designing the workflows, and writing up the Trello board. Each member has been involved and worked with all different aspects though, and the workload has been even.

## Discussion
The concrete goals of the assignment have been fulfilled:

* The project has been developed as a pair
* Program was built using Python
* Unit tested using the Python unittest module
* The solution compiles and runs
* Kanban board has been created with all demanded sections
  * Manifest
    * General information
    * Git workflow
    * Coding workflow
    * Task guidelines
    * Peer review guidelines
    * Code conventions
    * Documentation guidelines
  * Backlog
  * In Progress
  * Review
  * Complete
* The Information stated in the different manifest cards has been followed during the development process
* The Git feature branch workflow, with pull requests and peer reviews has been followed
* The Kanban board has mirrored the state of the project throughout the development
* Test-driven development has been used 
* There is full test coverage
* Commit messages to have body and header
* The production code is separated from tests

During the development process, we initially encountered frequent merge conflicts due to working in the same file for multiple features. This issue arose when the work in one branch could not be immediately merged with the master branch on which the next feature branch was based. The process of merging became slow and frustrating as the peer conducting the review had to merge the first branch and apply an issue for the second branch due to the raised merge conflict. To mitigate this issue, one approach could be to base the second branch upon the first branch, including the code, to avoid the merge conflict. However, this could lead to potential problems where the first branch contained faulty code that would move on to the second branch, making error detection and review more difficult and time-consuming. Another way to approach it could be to break down the work tasks into smaller, more manageable pieces. Although, that could increase the development time as it could get out of hand, adding more overhead to the workflow. Therefore, it's important to strike a balance between the size of the work tasks and the frequency of merges to ensure smooth collaboration and effective development.

Since all members were keen on making progress and had a mutual understanding of how the project should be done in broad terms, there was no major friction or conflicts during the process. There is always a personal opinion on how something should be done, but being able to let go of personal preferences to ensure the project progresses instead of being bogged down in details is good practice.  

There were no big issues in the collaboration process, and discussions regarding how/what should be done were resolved through mutual understanding or that one member had a strong conviction and idea of how something should be done - with the other member letting the idea proceed because of trust in each others ability and judgment. It is also important to not be overly attached to one's code and be willing to change/remove it as needed for the good of the project. 

There is always some time overhead and possible friction when one member has an idea and the other has to try and understand and may come up with doubtful comments or have a different conviction. But it seems as long as each member can confidently and freely describe their ideas, not be afraid of being “wrong”, and also be aware that others may have better solutions, there are often not so many problems. It is also important to be patient in trying to understand each other's perspectives and be respectful and constructive. It is also better to let somebody go ahead and let it rip at something they do good, instead of forcefully trying to make everybody contribute to everything “just because”. 

We do not like the idea of necessarily pair-programming everything, just to make everybody be involved in every line of code - and instead let team members work undisturbed, but with checks and balances being implemented by peer reviewing and also openly discussing things that are unclear or questionable.
