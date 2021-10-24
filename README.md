<a name="totop"/>

## <p><img src="#"></p>
---
<p> <img src="#"></p>

- Link to live website 

##### Table of Contents  
- [UX](#ux)  
- [The Site owner Goals](#usergoals)  
- [Existing Features](#existing)
- [Features Left to Implement](#leftfeatures)
- [Database Design](#dbdesign)
- [Project Requirements](#prequrements)
- [Wireframes](#wireframe)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#ack)

## UX
<a name="ux"/>

### User Stories

- User 1 : As a user I want to
- User 2 : As a user I want to 
- User 3 : As a user I want to 
- User 4 : As a user I want to be able to 
- User 5 : As a user I want to 
- User 6 : As a user I want to be able to register as a regular user.
- User 7 : As a user I want to be able to 

### The Site owner Goals
<a name="usergoals"/>



## Existing features
<a name="existing"/>



## Admin


## Color scheme



 <p><img src="static/docs/color-scheme-ms3.PNG" style="min-width:100%" height="200" alt="Color scheme"></p>


- Typography
    

## Features Left to Implement
<a name="leftfeatures"/>



## Database Design
<a name="dbdesign"/>

### Database Schema



## Project Requirements
<a name="prequrements"/>



### Main Technologies:





## Frameworks and libraries:
<a name="flibs"/>



- [**jQuery**](https://jquery.com/) used as a JavaScript library and for Materialize components  initialization.

## Other Technologies used:

- [**Heroku**](https://www.heroku.com/)  used for hosting deployed website.
- [**Google Dev Tools**](https://developer.chrome.com/docs/devtools/) used for developing and testing webpage.
- [**Firefox Dev Tools**](https://developer.mozilla.org/en-US/docs/Tools) used for developing and testing webpage.
- [**Get Waves**](https://getwaves.io/) used to generate SVG banner.
- [**Balsamiq**](https://balsamiq.com) used for creating a wireframe.
- [**Resize Pixel**](https://www.resizepixel.com/) Free online image editor used to resize images format.
- [**Google Fonts**](https://fonts.google.com) used for project fonts.
- [**Google Icons**](https://fonts.google.com/icons) used for project icons.
- [**Gitpod**](https://gitpod.io) used as a development environment.
- [**Gitpod Chrome Extension**](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) used to open Github repo in Gitpod.
- [**GitHub**](https://github.com/) used for storing repository. 
- [**Canva**](https://www.canva.com) used for logo creation.
- [**Autoprefixer**](https://autoprefixer.github.io/) used to add CSS prefixes and ensure cross-browser compatibility.
- [**Youtube**](https://www.youtube.com/) used as a general source of information.
- [**W3School**](https://www.w3schools.com/) used as a general source of information.
- [**Pexel**](https://www.pexels.com/) used to download the website's images.
- [**Pixabay**](https://pixabay.com/) used to download the website's images.
- [**Stackoverflow**](https://stackoverflow.com/) used as a general source of information.
- [**W3C Markup Validator**](https://validator.w3.org/) Used to test HTML code validation.
- [**W3C CSS Validator - Jigsaw**](https://jigsaw.w3.org/css-validator/) Used to test CSS code validation.
- [**PEP8 online**](http://pep8online.com/) used during post deployment testing stage to ensure PEP8 requirement.
- [**Am I Responsive**](http://ami.responsivedesign.is/) used during post deployment testing stage.
- [**Pixlr**](https://pixlr.com) used to remove background and editing photographs.
- [**Ezgif**](https://ezgif.com/video-to-gif) used to covert videos to gif format.

<a name="wireframe"/>

To see Project Wireframes please click the link: 
<a href="#">Wireframes</a>

## Testing :
<a name="testing"/>



## Deployment
<a name="deployment"/>

### Version control 

- The project's website code was written using Gitpod IDE. In order for code to be pushed to GitHub,it had to be added to stage for commit using `git add `command in GitPod's CLI .Once changes have been successfully added, it is required to commit these entering `git commit -m` into CLI. After committing it then can be pushed to GitHub by entering `git push` command in CLI.

### GitHub

- How to fork a repository: Forking a repository allows you to make changes to the code without affecting the project. To fork a repository follow the next steps:
1. If you do not have one,create a [GitHub](https://github.com/) account and remain logged in.
2. Navigate to [kuzGo/MS3-Project-CI](https://github.com/kuzGo/MS3-Project-CI);
3. In the top right corner find the "Fork" icon.
4. Click the Fork icon to fork the repository.

- How to clone repository: Cloning repository allows you to pull down a full copy of the repository and work on it locally on your machine. To clone a repository follow these steps:
1. If you do not have one,create a [GitHub](https://github.com/) account and remain logged in.
2. Navigate to [kuzGo/MS3-Project-CI](https://github.com/kuzGo/MS3-Project-CI);
3. On the repository main page navigate to the "Code" drop down menu button and click on it.
4. Ensure to select HTTPS and click on the clipboard icon to copy the URL.
5. In the IDE you chose to work, open the new terminal.
6. Change the current working directory location where you want the cloned directory.
7. Enter command git clone and paste the URL you copied.
8. Click Enter.



### Heroku

- The website is deployed to [Heroku](https://www.heroku.com/) due to GitHub's ability to only host static pages. To successfully  deploy the website to Heroku please follow these steps.

### Prerequisite
In order to successfully  run the app on Heroku,there are a few applications and dependencies required.
1. In the IDE terminal enter command `pip3 freeze--local > requirements.txt`.
2. Create Procfile using CLI command `echo web: python app.py > Procfile`. Delete a blank line to avoid any possible issues with the app.
- Heroku Deployment

1. If you do not have one,create a free [Heroku](https://www.heroku.com/) account and remain logged in.
2. For this particular project Python needs to be selected as a Primary Development Language.
3. Navigate to "Create New App" button.
4. Create a unique app name using hyphens instead of spaces.
5. Choose a region closest to you. I selected my region Europe.
6. Click Create App button.
7. In the Deploy section, as Deployment method select GitHub,this option will automatically deploy from GutHub repository.
8. In the Connect to GitHub section ensure that your GitHub profile is displayed.
9. Enter repository name and click Search button.
10. Once repository is found click Connect button.
11. Navigate to settings and click Reveal Config Vars.
<p><img src="static/docs/configvars.PNG" style="min-width:30%" height="100" alt="Heroku App snip"></p>

12. Enter variables from `env.py` file : IP , MONGODB_NAME, MONGO_URI, PORT and SECRET_KEY. This is required step since Heroku will not be able to find these secured in `gitignore` folder.
<p><img src="static/docs/vars.PNG" style="min-width:30%" height="100" alt="Heroku App snip"></p>

13. Prior to enabling automatic deployment, make sure that requirements.txt and Procfile are pushed (`git push`)to GitHub.
14. Click Deploy Branch button.


## Credits :
<a name="credits"/>

### Code snippets :





### Photographers :



## Acknowledgements
<a name="ack"/>



### Site is for educational purposes

[:arrow_up:](#totop)

