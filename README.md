# CS-340-Client-Server-Development


**How do you write programs that are maintainable, readable, and adaptable?**

I try to keep my programs organized and break the code into sections that each have their own job. A good example of this was the CRUD Python module from Project One. The module handled the connection to MongoDB and the create, read, update, and delete functions. When I started Project Two, I was able to use the same module to connect the dashboard to the database instead of having to write all of that code again inside the dashboard.

I think one of the biggest advantages of doing it this way was that the code was easier to follow and easier to change. If there was a problem with the database connection or one of the CRUD functions, I knew where to look instead of searching through the entire dashboard program. I could also use the same CRUD module again in another program that needs to work with the same database. It could be used with another dashboard, website, or other type of application without starting over from scratch.

**How do you approach a problem as a computer scientist?**

I usually try to break a problem down into smaller parts and get one part working before moving on to the next one. With the Grazioso Salvare project, I started with the database and made sure the CRUD functions worked first. After that, I moved on to the dashboard and worked on the filters, data table, charts, and map. I tested things as I went instead of trying to build everything at once. That made it easier to figure out what was causing a problem when something did not work.

This project was a little different from some of the work I have done in other courses because there were several parts that all had to work together. The MongoDB database, the Python CRUD module, and the dashboard all depended on each other. In the future, I would use the same basic approach for another client. I would look at what the client needs, figure out what data has to be stored, decide how the data needs to be searched or filtered, and then build and test each part one at a time.

**What do computer scientists do, and why does it matter?**

Computer scientists use programming and technology to solve problems and make tasks easier or more efficient. Depending on the project, that can mean building a database, creating a program, working with data, or making a tool that helps people find and use information.

For Grazioso Salvare, the dashboard makes it much easier to work with the animal shelter data. Instead of looking through a large amount of records by hand, the user can filter the data and see the results in a table, chart, or map. This can help the company find animals that match certain rescue requirements faster and make better use of the information they already have in the database.
