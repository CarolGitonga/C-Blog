# C-Blog

## Author

[carol-profile](https://github.com/carol-profile)

# Description
<p>This is a web app that allows users to sign in or subscribe, view blogs and comment on different blogs. A writer can create blogs, update blogs and delete their blogs or comments on their blogs. The web app has also a section that displays random quotes and subscribers get emails when new blogs are posted.</p>

## Live Link
* This is the live [link to the app ](https://carolpitchhub.herokuapp.com/)

## Screenshot


## User Story

* As a user, I would like to view the blog posts on the site
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
 git@github.com:carol-profile/C-Blog.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd C-Blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3 manage.py server
  ```
5. Testing the application
  ```bash
  python3 manage.py test
  ```


## Technology used

* [Python3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

Slack Profile - [Carol Gitonga](https://app.slack.com/client/T0101L740P4/D036H8B6WF2/user_profile/U0330AYGJAY)



## License
* *MIT License:*
* Copyright (c) 2022 **Carol Gitonga**

[Go Back to the top](#C-Blog)
