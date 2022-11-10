![image](https://user-images.githubusercontent.com/93741957/194701273-220700eb-bc22-4f88-95ab-5b88478a3a21.png)

Avenger Stuff lives inside the MCU - it's purpose: "When the battlefield has cleared and the dust has settled in the aftermath of an Avenger bout, we collect Avenger's stuff so you can own an item that once belonged to the beloved Avengers!". 

This site is intended to be fun, and placed inside a make believe world of Marvel. It is to enable people to purchase items/weapons/clothing that once belonged to an Avenger. 

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

# (Temporarily keeping the below during development) 

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
