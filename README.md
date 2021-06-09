# DjangoTrainingBooking
## Welcome  
This project is the start of the internal training system that will be used by L&D to help Ideagen employees’ book onto training courses. So far, the backend design is complete, and the web app preforms all the basic functionality outlined in the project scope to an extent. Some logistic issues like email replies are not working as the website needs to be on the public domain and during development it’s on a local domain, there are a few other features that need to be added, these are:
- Automatic email reminders to the course host & participants 
- Exclusively allow employees in a certain department to access certain courses
- Change the approved field in the attendees model to have states (Pending, Approved, Rejected) rather than the current True or False  

**When will this be done?**
I hope to add these features before the next rotation  

## Documentation
The design that is used in this project is documented on confluence and this can be found [here](https://ideagen.atlassian.net/wiki/spaces/~475003006/pages/38275022851/Training+System+Backend). As for the code, all the main files have comments to indicate what everything is doing.

## Getting Started
This section is for the other apprentices, if you are curious about how this works or want to use it as a reference to learn Django then you will need to know how to navigate around the files. The main file you would want to look in is called `views.py` which can be found in `TrainingSystem/app_name/views.py`. I have used `app_name` because in this project there are **two** apps. These apps are:
### Users App
- Contains all the models, functions and templates regarding user registration & login
- Contains the Profile model mentioned in the design documentation

### Booking App
- Contains all the models, functions, templates regarding the admin side of the site (adding programs & courses, admin dashboard and updating course information)
- Contains all the models, functions, templates regarding the user booking process (viewing available courses and booking onto those courses)

I have tried to keep the codebase as simple and maintainable as possible so after learning the basics of Django it should be easy to follow but if you don’t understand a certain function or how something works, ask me I’m happy to explain the code.
