**<b> Quick Description </b>**

This app exposes a few simple HTTP APIs endpoints.

1. Description: Saves/updates the given user’s name and date of birth in the database.
   Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
   Response: 204 No Content

2. Description: Returns hello birthday message for the given user
   Request: Get /hello/<username>
   Response: 200 OK
   Response Paylod: { “message”: “Hello, <username>! Your birthday is in N day(s)”
   }
-----------------------------
**<b>How to run this locally:</b>**
1. Clone the repo
2. cd RB_devops_test_hello_world
3. pipenv install --dev (if you dont do --dev, dev packages wont be installed and you wont be able to run anything requiring those pkgs)
4. pipenv run python main.py 

-----------------------------
**<b> How to run the test?</b>**

Run this command from your pipenv shell -

pytest --cov=RB_devops_test_hello_world --cov-report=html --cov-report=term --verbose

This will create a terminal output and a html report of unit test coverage

There is a known bug in pytest where it doesnt tell you exactly which lines are not coverage. For this,
You can also use coverage module like: 

coverage run -m pytest && coverage report

-----------------------------
**<B>High Level decisions made:</B>**

1. MySQL DB is used because of wide spread availability on multiple platforms. Also, a personal use license is free of cost. 
In PROD environment, we should be relying on Oracle given all the DB management facilities available in it like golden gate replication etc.

2. Python language was used due to skill set available and how fast and easy it is to whip up a flask app

3. There is only one table currently created for this - user_dob with columns username and date_of_birth with username as PK. There were 2 choices here:
   a. Store the DOB as is ie. a string value and do the math in python before returning the message
   b. Create 3 separate colums for date, month and year so you only fetch month and day and then do the calculation.

   I choose first because although there are many ways of slicing and dicing and storing the data, the first choice gives the fast and most readable format. Of course depending on other business requirements, this decision could go either way.

4. Another error handling outside of provided business rule that was added was to check if the user exists or not before sending any birthday message.

5. Some of the error messages are on purpose generic ex: 'Bad Request' so as to protect the system from any attacks. This is in line with the theory where if an attacker is making API calls and it errors out, they shouldn't be told what the right way to access is through errors messages so as to delay any potential impact. 
   I understand its not important for this case but I would highly recommend this for any production env.

6. There should also be an authentication method which was omitted in this particular project. 

7. 'Waitress' should be used for serving a PROD app and not Flask. It could still be a flask app, but waitress is used for PROD system. 
The best advantage of using waitress is that it doesnt need much of the wsgi management. 