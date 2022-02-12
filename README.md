<div align="center">

![Food plants to Grow](media/readme_files/responsive-mockup.png)

---

Food plants to Grow is a website dedicated to providing users with the opportunity to purchase the plants they need to grow their own food. Users can also suggest plants to add to the website, using a rating system. This site is connected with the "Recipe to Grow" website, which contains plant based recipes. 

**-- [See live site on Heroku](https://ejh-food-plants-to-grow.herokuapp.com/) --**

</div>

---

## Table of contents

**<details><summary>User Experience</summary>**
  - [User stories](#user-stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
</details>

**<details><summary>Features</summary>**
  - [Existing features](#existing-features)
  - [Future features](#future-features)
</details>

**<details><summary>Technologies Used</summary>**
  - [Languages](#languages)
  - [Libraries, Frameworks and programs](#Libraries,-Frameworks-and-programs)
</details>

**<details><summary>Testing</summary>**
  - [Test documentation](https://github.com/ElkeJohannes/food-plants-to-grow/blob/main/TESTING.md)
</details>

**<details><summary>Deployment</summary>**
  - [Deployment to GitHub pages](#deployment-to-github-pages)
  - [Forking this repository](#forking-this-repository)
  - [Local deployment](#local-deployment)
</details>

**<details><summary>Credits</summary>**
  - [Text](#text)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
</details>

---

## &rarr; **User Experience**

### **<ins>User stories</ins>**
![User stories](media/readme_files/user_stories.png)


### **<ins>Strategy</ins>**
The main purpose of the website is to allow the shop owner to sell his plants online, and for users to purchase them. The site is slightly community driven in that it receives input on which plants to sell from the users. 

### **<ins>Scope</ins>**
The site will have a plants page where you can search for a plant and add it to your shoppingcart. Additionally it will have a suggestions page to submit plant suggestions. 

### **<ins>Structure</ins>**
The main page has links that bring you to the most important parts of the site right away. The menu will collapse into a hamburger menu on tablet or smaller sizes. Each action takes the user to the next logical place to go. For instance after clicking on 'Add to cart' the user is brought to their shoppingcart. 

### **<ins>Skeleton</ins>**
The following wireframes were made using Balsamiq to give a rough idea of the project.
- [Home page](media/readme_files/wireframe_home.png)
- [Plant overview page](media/readme_files/wireframe_plants.png)
- [Suggestions page](media/readme_files/wireframe_suggestions.png)
- [Login page](media/readme_files/wireframe_login.png)
- [Contact page](media/readme_files/wireframe_contact.png)


### **<ins>Surface</ins>**
A bright green image featuring leaves from the Beech tree is visible through a transparant background. Overall the site will feature mostly green buttons, but will otherwise be low in colour usage. 

---

## &rarr; **Features**

#### **<ins>Existing features</ins>**
|#|Name|Description|
|-|-|-|


#### **<ins>Future features</ins>**
|#|Name|Description|
|-|-|-|


---

## &rarr; **Technologies Used**
### **<ins>Languages</ins>**

| <div align="center">HTML5</div> | <div align="center">CSS3</div> | <div align="center">Javascript</div> | <div align="center">Python</div> |
|-|-|-|-|
| ![html5](media/readme_files/html5.png) | ![css3](media/readme_files/css3.png) | ![javascript](media/readme_files/javascript.png) | ![python](media/readme_files/python.png) |


### **<ins>Libraries, Frameworks and programs</ins>**
- [JQuery 3.5.1](https://jquery.com/)
  * Used for easier DOM access.
- [Django 4.0](https://www.djangoproject.com/)
  * Used as the framework for the site to speed up development.  
- [Bootstrap 5.1.0](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
  * Used widely troughout the site to speed up layout design.
- [Multi device mockup generator](http://techsini.com/multi-mockup/index.php)
  * Used to create the header image of this readme file.
- [Favicon generator](https://favicon.io/favicon-generator/)
  * Used to create a custom favicon.
- Various python modules, entire list visible in [Requirements file](https://github.com/ElkeJohannes/food-plants-to-grow/blob/main/requirements.txt)


---

## &rarr; **Deployment** 
### **<ins>Deployment to Heroku</ins>**
1. Created the project on Github. Git and Github were also used for the version control.
2. Created a new, empty app on Heroku
3. Linked the Github repository to the app
4. Created the Config Vars on the settings page of the app. In order to make the application work for yourself, ensure you create the following keys here:
   - SECRET_KEY (needed for Flash messages)
5. From the deploy page, ran a manual deploy, after which, automatic deployment was enabled for the 'main' branch

### **<ins>Forking this repository</ins>**
1. Login to [GitHub](https://github.com)
2. Browse to the [repository](https://github.com/ElkeJohannes/food-plants-to-grow)
3. On the top right of the page, there should be a button that says 'Fork'. Click on this button to fork a copy of the site to your own repositories.

---

## &rarr; **Credits**

### **<ins>Text</ins>**
- All plant common and botanical names as well as the descriptions were taken from: [foodforestnursery.com](https://foodforestnursery.com/product/swamp-white-oak/)

### **<ins>Media</ins>**
- All plant images were also taken from: [foodforestnursery.com](https://foodforestnursery.com/product/swamp-white-oak/)

### **<ins>Acknowledgements</ins>** 
- Shop template taken from [Startbootstrap.com](https://startbootstrap.com/template/shop-homepage)
- Color sheme from [Colorhunt.co](https://colorhunt.co/palette/125c133e7c17f4a442e8e1d9)
- Tutorial for adding extra fields to users [cpadiernos](https://cpadiernos.github.io/how-to-add-fields-to-the-user-model-in-django.html)
- Converting string to list [Geeks for Geeks](https://www.geeksforgeeks.org/python-program-convert-string-list/)
- The following stackoverflow questions:
  - [Filtering by category](https://stackoverflow.com/questions/4062955/django-foreign-key-queries)
  - [Resetting django db](https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory)