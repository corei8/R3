# R3

A new Language Management System. Canvas, Blackboard, Moodle, they all fall short in some way or another. This web application strives to solve all the issues found in all of these systems.

## Features

Bear in mind our user base: teachers who have to optimize very moment of their time, who are of varying technical prowness. The enire application has to be manageable without a user manual: intuitiveness is essential. Everything has to be very fast, and everything has to be equally fast: this app has to be the vim of LMSs. Also, nobody wants to use an ugly tool, and minimalism has become a popular trend in software, owing to the ease of use that this design encourages. Customization of style will be permitted to some degree, but a strict styling standard will be enforced.

### 100ms rule

Each action has to be instantaneous. Every page load and data manipulation has to be super fast, less than 100ms. If an action does not meet that requirement, then it is either not ready for production, or the process has to be rethought.

**Example**: loading a page of grades. For large classes this might become an issue, especially deep in the year, and if the teacher wants to see, let's say, two and a half quarters of a class of 100 students, 
