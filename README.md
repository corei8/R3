# R3

A new Language Management System. Canvas, Blackboard, Moodle, they all fall short in some way or another. This web application strives to solve all the issues found in all of these systems.

## Features

Bear in mind our user base: teachers who have to optimize very moment of their time, who are of varying technical prowness. The enire application has to be manageable without a user manual: intuitiveness is essential. Everything has to be very fast, and everything has to be equally fast: this app has to be the vim of LMSs. Also, nobody wants to use an ugly tool, and minimalism has become a popular trend in software, owing to the ease of use that this design encourages. Customization of style will be permitted to some degree, but a strict styling standard will be enforced.

### 100ms rule

Each action has to be instantaneous. Every page load and data manipulation has to be super fast, less than 100ms. If an action does not meet that requirement, then it is either not ready for production, or the process has to be rethought.

**Example**: loading a page of grades. For large classes this might become an issue, especially deep in the year, and if the teacher wants to see, let's say, two and a half quarters of a class of 100 students. In this case lazy loading will have to be absolutely necessary, and an ordering priority will have to be observed: interface, close data, far data, etc.

### Keyboard-centric

The user should be able to control the entire application without touching either the mouse or the arrow keys.

To keep things accessible, we must make sure that the application is accessible with the mouse (and the arrow keys), but the main focus should be on the keyboard and the home row. Having the ability to change the keybindings might be beneficial, and having the ability to import and export the bindings would also be beneficial.

### Command Palette

Having all of the commands available from a search that can be accessed from anywhere in the application.

### Simple Menu

The navigation for most LMS tends to be either too crowded and overwhelming, or too simplistic and unintuituve.

## Development

**Dec. 20, '22** 📖 We have no releases yet, and are just starting this project.
