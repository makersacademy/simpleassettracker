# Contributing

When contributing to this repository, please first discuss the change you wish to make by talking it over with a team, either on slack or discord.

### Pull Request Process

1. Ensure any dependencies you add are mentioned either in requirements.txt if its Django related or reactfrontend/package.json if its React related.
2. Update the README.md with details of changes if you think that they were significant enough to do so.
3. You have to ask another developer to review and approve your pull request before you can merge.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the team
* Showing empathy towards other team members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

### Working Hours

Our working schedule is Monday to Friday from 9 30 am to 1 pm, we are very flexible and understand if someone can't make it on a particular day.

### Testing 

Ensure that all the code you write is test-driven or tested, we have high test coverage and are doing our best to maintain it.

### Deployment

We use automatic deployment on Heroku, which means every time we make changes to the master branch Heroku will recognize them and automatically deploy those changes to the live server. We also use Codeship as another layer of security. What Codeship does is it ensures that the app is working and all the tests are passing. If Codeship is failing that means either your code has a bug that prevents the app to be successfully deployed or at least one test is not passing.
