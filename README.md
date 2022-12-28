![image](https://user-images.githubusercontent.com/93741957/194701273-220700eb-bc22-4f88-95ab-5b88478a3a21.png)

Avenger Stuff lives inside the MCU - it's purpose: "When the battlefield has cleared and the dust has settled in the aftermath of an Avenger bout, we collect Avenger's stuff so you can own an item that once belonged to the beloved Avengers!". 

This site is intended to be fun, and placed inside a make believe world of Marvel. It is to enable people to purchase items/weapons/clothing that once belonged to an Avenger. 

Functionality and accessibilty varied dependant on regular user, authenticated user and superuser. There is a difference, to try and entice people to become a user and join in conversations and have more access in the site. While having a superuser with full access and some access others don't to try and uphold good security (though this is something I feel could be developed further for better relevance and user experience too - for example, an author being able to edit their own product without the help of the superuser/site owner).

Something I chose to do was to enable non-users to post a product to the site, I did this as I wanted the main purpose for the site for people to buy Avengers stuff, and felt giving someone the opportunity to post a product might entice them to further browse and want further functionality to then sign up. This in particular could be up for review, however.

## Colour Scheme: 

In line with the Avengers logo and Marvel, I went for a clean Red and White scheme, which is persistent throughout the site.

## Extra Information: 

To have Create, Read, Update and Delete functionality, this is allowed via either User or Superuser authentication, which is purposely done to avoid anyone visiting the site to be able to affect the database. 
To purchase something, you can also use the generic details of 4242 4242 4242 4242 42 42 in the card details section to see an example of the E-commerce aspect of the site in action. 

## User Experience Design Thinking: 

This site, as clearly stated above is to allow the user to purchase something that belonged to one of the Avengers - this is the core and main purpose. This was the reasoning behind all of the design thinking behind layout which is clear and is only a few clicks away from entering the page to landing on the checkout page. This is purposely done to allow efficient speed to the goal and objective of someone landing on the site. To help which this I included a clear message and mission statement to the landing page to ensure the user knows exactly what they can do on this site, to cover the basis of new users and users who know what they were looking for when finding this site. 

The design of the information, text and forms is also purposefully quite streamlined - though keeping all relevant information to ensure the experience is clear, quick and enjoyable for the user too. As too much information, too little information or a messy design could deter from this.

It is also made clear to the user and it is encouraging the user that you must register to be able to make purchases or have some core functionality in the site. This is important, as if you land and stay on the site, it's becuase you want to join the community, and or, purchase something - and to be able to do this you need to be a "member" as such and sign in/register. This is a key driver to doing so, and is made clear to the user in a plutonic way. 

## Stuggles: 

The main struggle was the amount of moving pieces and keeping on top of all the interconnection between apps, AWS, Stripe etc. was difficult finding the needle in a hay stack when there was a bug. 

One main issue was an issue with a csrf token in allauth templates, this took a lot of hours to debug to find out that there was a random input field generating the same recursive token number which, for Django, was causing a security risk and was spitting out an error. 

Another struggle I had was with AWS setup, there were lots of steps and I may have missed a step or two and had to redo the whole process to rectify the problem, which was the static files not loading into the bucket in AWS.

I came across a 'checkout' issue, with a internal server error 500 message appearing. This was due to stripe secret and public keys not being in config. vars in Heroku, they were in gitpod variables which I had thought would suffice, but evidently not. This was rectified and E-Commerce element is fully functional - which can be tested using 4242 4242 4242... recurring. 

## Future Expansion: 

The site has good foundations to be built upon. As it is set in a fake reality, it could build relationships with Avengers to offer services rather than just products i.e. have Captin America be a dinner speaker for an evening. There is also scope to build upon the Reviews section, to expand this into a wider community forum to allow people to connect and communicate with one and other. It could be developed further from a UI/UX perspectice to allow authors of their own products to edit or remove items without the need to contact the site admin.

## Development 

### Blueprint for site: 

![image](https://user-images.githubusercontent.com/93741957/201719199-3f63fb3b-dfe6-4363-867a-c4c4e232767a.png)

I used Balsamiq to create each template for the key pages: Home, Products Page, Mobile view...

The generic form pages I did not create templates for, as they were VERY basic and did not require the extra time it would take to create the templates for them.

### Facebook page: 

![image](https://user-images.githubusercontent.com/93741957/201722230-a590227b-ab2f-46a3-af90-e2cb440fe34e.png)

This is in development stage of creating a business page for the Avenger Stuff site. With the consistency of the intro message in there. The final step was simply just uploading the Avenger background and logo. 

Final page: 
![image](https://user-images.githubusercontent.com/93741957/201725392-fadd2e3d-e04b-4082-8987-524e2da31367.png)

## User Stories: 

![image](https://user-images.githubusercontent.com/93741957/197396518-d2b6ca4d-4e8a-4fb7-8db8-12ed64af368d.png)

Created a file for all user stories in an excel spreadsheet, which I worked through one by one to help create functionality, this helped prepare and plan out the steps of development and helped work through an agile method also. Part way through the project I added these in Git to better help and plan my work.

Then further created a file in Projects to work in an Agile way and follow proper structure when developing elements and functionality across the site: 

![image](https://user-images.githubusercontent.com/93741957/201072183-5fae37f9-fd90-46bd-9d68-2b6af0cb4f46.png)

### Understand the purpose of the site:
This is covered in the above intro, this initial message is what is displayed to the user which clearly outlines what you can do on this site. 

### Properly navigate the site:
Created a user friendly nav bar, specfically designed for all screen sizes. 

![image](https://user-images.githubusercontent.com/93741957/194764217-5b05a8cf-2815-4a6c-b116-c9db5f5f1ebc.png)

### View all items: 
As per above image, which highlights sound navigation, this page demonstrates the ability to view all items in the site in one place. 

### Be able to Log in and out as an authenticated user: 
![image](https://user-images.githubusercontent.com/93741957/194764385-4eb8dc9c-d1f8-4c88-a038-26e8f344db4c.png)

Using Allauth, created ability to allow authenticated users to log in and out. 

### Select an item for a detailed view: 

![image](https://user-images.githubusercontent.com/93741957/194937749-00a71534-df86-471d-ae67-c17f79892bfb.png)

Created a separate page, per item, to allow users to view that items detail.

### Search functionality to filter products

Created functionality to serach for keyword inside item name. Chose not to include descriptions into the function as Avenger names are used often in descriptions that do not directly relate to them and this would convelute and confuse the search functionality for the user. 

### Filter products by category or avenger: 

Added functionality to the site navigation to filter each item by either its category or it's avenger connection. 

### Sort items by price

![image](https://user-images.githubusercontent.com/93741957/196261762-f65db296-9f69-491f-a17d-2b30866fb6a9.png)

As per above (highlighted), added functionality to allow the user to filter or sort by product price, as well as Avenger name and Category. 

### add and edit items via bag 

This acculminates a few user stories of being able to add items to the bag, viewing the bag and also being able to edit those items i.e. remove. 

### Purchasing

For the ability to purchase items in the bag and to complete the Ecommerce aspect of this site, I implemented and installed Stripe. This is to allow users to input payment details, alongside their personal details and address to enable functionality to properly purchase their selected items. 

### Add/Edit/Delete items

Any superuser, or site owner can have full functionality to add, edit and delete items from the database via the front end. Though, anyone can upload an item found in the aftermath of an Avenger bout! I chose to have the full functionality limited to superusers and site owners to stop the possibilty of anyone deleting other peoples work or products. 

### Sign up to a newsletter

There is an option in the About section to sign up for a newsletter, which requires simple information from a user. This would be stored in the database ready for newsletter release by the site admin. 

### Able to contact the site owner via contact us page 

Implemented a simple section in the About section of the site, to allow users to contact the site owners, this is generic for a reason, to allow ease and simplicity for all issues or reasons a person may need to contact the site admin/owner. 

### Post a review 

Implemented an area in the About section to allow for a community feel of communication on the site directly, this is mainly for people to post their reviews on the items they have purchased, or related topics. Though it is kept relaxed and flexible to try and encourage a forum styled area for people to come and join the conversation of all things related to the Avengers and their "Stuff" - this encourages people to get involved, stay involved and ultimately spend more time on the site which will promote purchases and/or people to go and find items to post on the site. 

## Testing:

### Heroku Database

New information regarding Heroku's database policy changes came about following initial and secondary submittion. Leading to errors on many pages that rely on sound database storage and connectivity. To resolve, I migrated the local database into ElephantSQL and ensured the App used this database URL rather than the local one. I then referrenced the elephantsql URL in the Heroku/Gitpod variables to ensure the site worked with the datbase correctly. To check this worked, it was simple - via the local and deployed site, I navigated to the pages that required use of the database and when no Internal Error messages appeared, I knew things worked and the app was ready for stress testing and further manual tests to ensure links and functionality all worked correctly. 

### Python

Passed through https://extendsclass.com/python-tester.html (online validator) as PEP8 was not working online at the time of testing. This passed with no errors. 

### HTML and CSS

Passed through https://validator.w3.org/ without error as per below: 

![image](https://user-images.githubusercontent.com/93741957/201132204-00ce9e38-d66f-4e1a-8763-92346a67004b.png)

Found error in ID duplication which was due to clashes in mobile and web browser navigation bars and their ids clashing. Once I changed the IDs to something more unique per option, this error was rectified. 

### Browser

The site address avenger-stuff.herokuapp.com was trialled on Edge, Chrome and Modzilla - all work correctly.
I also asked family and friends to test out the site, encouraging them to click links, navigate, register/login, purchase, add and delete items as much as possible to help find any bugs or system issues/errors that could be rectified. 
Doing so also helped find and fine tune the UI/UX and helped with the layout of the site, specfically speaking on small screens.

### E-Commerce Testing: 

Various payments, using the example digits of 4242 4242 4242 4242 42 42, were processed to check the functionality of Stripe. As per the below report, you can see proof of many successful payments: 

![image](https://user-images.githubusercontent.com/93741957/208946339-ae13a915-61c9-49f5-bd8e-c574e61ab417.png)

### Security

To stop people being able to access sensitive pages directly via the URL I included security into the views.py files to ensure @login_required. Which removes non-authenticated users being able to access pages they shouldn't have access to. And, also further prompts people to be an authenticated user of the site. 

### Lighthouse Report

![image](https://user-images.githubusercontent.com/93741957/201134083-45eb19fc-8eb7-4b55-9072-8751cb1b065d.png)

The results of this report are quite average, but after review, found that some of the issues bringing it down seemed off, one example being li elements not being wrapped in ul and the nav elements were highlighted, but as per the code, you can see that they are...I was stumped with this and was not sure how to rectify this. I thought that the report was not bad enough to warrant lots of investigation to resolve this. 

## 404 Custom Error Page

As per the requirements of the course, I created the below error page, keeping in sync with the sites look and feel. 

![image](https://user-images.githubusercontent.com/93741957/201349258-1346abb1-0986-4b27-86f6-6d12af25cfcd.png)

## Site development: 

To confirm the site during development and in deployment, both look as they should, as per the below. 

Development: 
![image](https://user-images.githubusercontent.com/93741957/202790073-701d78c2-bc1f-44fd-9764-b67679b20c31.png)

Deployment: 
![image](https://user-images.githubusercontent.com/93741957/202790175-9e3dc0d8-6f26-4c08-9cb2-603e4113b088.png)

## Deployment:

This project was deployed via Heroku.

- Login to Heroku account on app.
- Set buildbacks to Django and AWS. 
- Link Heroku to Git repository.
- Deployed.

Essential packages installed/used for this app. Are as follows:

- Allauth
- Stripe
- AWS Wire up
- ElephantSQL 
- Pillow
- Boto3
- Gunicorn

Environment variables for AWS/Static, ElephantSQL and Stripe are stored in Heroku Config. Vars or Gitpod variables area. Not copied in README for security. 

## Using Git: 

I created a respository and opened in gitpod to create my code. To move my code from gitpod to repository ready for deployment I followed these steps (which I did often to show a journey of creating my site):

- git add .
- git commit -m "message"
- git push
- git pull --rebase
  
## Resources: 

For resources not mentioned above, I used Slack, Google, YouTube, Code Institute walkthrough videos and tutoring as well as relate tech stack documentation. All to help with developing and debugging across the site.

## SEO

I was careful throughout the whole project to include good language that was inline with what a Google Rater would perceive a good site. I was mindful to not over do it and make all the information relevant and concise. 

I included a robots.txt and sitemap.xml files to ensure compliance and demonstration of awareness around this particular topic and practice. 

## Head Tags

All meta tags and head content was typed up to best practices, checked via multiple sites, a concise one being https://www.searchenginejournal.com/important-tags-seo/156440/ 

