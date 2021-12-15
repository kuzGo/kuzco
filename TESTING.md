# Testing :
<a name="totop"/>


At various stages of the project development I have been using extensive testing of the website.Main tools used to test the website are Google Dev Tools,Firefox Dev Tools . To validate the code  I have been using W3C Markup Validator, W3C CSS Validator - PEP8 Online to ensure proper indentation and full PEP8 compliance. During development The [Built-In Django's Debugger](https://docs.djangoproject.com/en/4.0/ref/settings/) was set to `True` so the code has been refactored on multiple occasions should any errors occurred.


<details>

<br>
text here
</details>



### Image of rendered page:

<details>
<br>
 <p><img src="static/docs/scrshot 2.PNG" style="min-width:80%" height="400" alt="HTML Temlpate"></p>
</details>

### Image of HTML Template:

<details>
<br>
  <p><img src="static/docs/html.scrshot.PNG" style="min-width:60%" height="600" alt="HTML Temlpate"></p>
</details>


<details>
<br>
 <p><img src="" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

<details>
<br>
 <p><img src="" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

## Code Validation

- Results of CSS code validation:
      - Code shows no errors.Note: Warnings are due to prefixes added using Autoprefixer to ensure cross-browser compatibility.

   <a href="Docs/W3C CSS Validator Kuzco.pdf" target="_blank" >Link to CSS Validation PDF Document</a>

   <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
   </p>
       
  <p>
   <a href="http://jigsaw.w3.org/css-validator/check/referer">
     <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
       </a>
   </p>

- Results of HTML code validation:
      - Document checking completed. No errors to show, warnings are only for `type` unnesesary for javascript.

  <a href="Docs/Nu Html Checker Kuzco.pdf" target="_blank" >Link to HTML Validation PDF Document</a>


- Results of Python PEP8 code validation:
<details>
<br>
 <p><img src="static/docs/pep8.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

### Lighthouse reports of deployed website:

Lighthouse mobile report:

<details>
<br>
 <p><img src="Docs/lighthse-mobile.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

Lighthouse desktop report:

<details>
<br>
 <p><img src="static/docs/lighthse-desktop.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

### User stories testing :

- User 1 : As a user I want to 
<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 2 : As a user I want to 


<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 3 : As a user I want to be able to
<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="Docs/.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 4 : As a user I want to be able to 
 <details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="" style="min-width:60%" height="200" alt="Activities"></p>
</details>

- User 5 : As a user I want to have convenient access 
<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 6 : As a user I want to be able to register as a regular user.
      - I was able to easily navigate to convenient registration page and to register as a user.

<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details> 

- User 7 : As a user I want to be able to login to my account as a registered user.
    - I was able to create a strong password and to login into Groapps securely every time after registration.

<details>
<br>
<p><img src="static/docs/login.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>   


### Functionality testing :

As part of functionality testing the developer tested every part of the website to ensure that everything is working properly on different types of devices and screen sizes. Browsers that the website has been tested on are as follows:Google Chrome, Firefox, Microsoft Edge.Testing of the website was conducted on numerous devices that I and my close relatives and friends own,these are as follows : Samsung S21, Samsung S20,Samsung A52.Desktop screen sizes all report no issues.

#### Navigation bar:
1. When the company logo is clicked it will bring the user to the home/landing page regardless of what page the user visits.
2. The Home button will change the text color to red when hovered over. When clicked it will bring the user to the homepage. 
3. The Login button is styled slightly differently than the other two buttons to emphasise it's functionality.When hovered over it'll change the text and background color, when clicked it'll bring the user to the Login page.
4. The Register button is styled slightly differently than the other two buttons to emphasise it's functionality and bring the user's attention and click register. When hovered over it will change the background and text color and when clicked it will bring the user to the register page.

#### Homepage:
1. Image sliders, is a full width of the screen with indicator showing which item is displayed.Each photo consists of text content describing the purpose of the website.
- Three card panels with the image and informative text content , inviting users to register.
When the plus button is clicked there are two possible outcomes:




<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>   


<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  

#### Register page:



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  

- If the user already has a registered account, they can click the link below, which will lead to the login page.

#### Activities page:


1. Search bar
    - Search button

    <details>
    <br>
    <p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
    </details> 

   

    <details>
    <br>
    <p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
    </details> 

    

    <details>
    <br>
    <p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
    </details> 


    
    <details>
    <br>
    <p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
    </details> 
   



    <details>
    <br>
    <p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
    </details> 


#### Admin page:



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  



<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>  


<details>
<br>
<p><img src="" style="min-width:60%" height="400" alt="Activities"></p>
</details>




#### Known Issues:

[:arrow_up:](#totop)