<b> Quick Description </b>
This app exposes a few simple HTTP APIs endpoints.

1. Description: Saves/updates the given user’s name and date of birth in the database.
   Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
   Response: 204 No Content

2. Description: Returns hello birthday message for the given user
   Request: Get /hello/<username>
   Response: 200 OK
   Response Paylod: { “message”: “Hello, <username>! Your birthday is in N day(s)”
   }

<b>How to run this locally:</b>
1. Clone the repo
2. cd RB_devops_test_hello_world
3. pipenv install --dev (if you dont do --dev, dev packages wont be installed and you wont be able to run anything requiring those pkgs)
4. pipenv run python main.py 

<b> How to run the test?</b>
Run this command from your pipenv shell -
pytest --cov=RB_devops_test_hello_world --cov-report=html --cov-report=term --verbose
This will create a terminal output and a html report of unit test coverage

There is a known bug in pytest where it doesnt tell you exactly which lines are not coverage. For this,
You can also use coverage module like - coverage run -m pytest && coverage report

<B>High Level decisions made:</B>

1. MySQL DB is used because of wide spread availability of multiple different formats. Also, a personal use license is free of cost. In PROD environment, we should be relying on Oracle given all the DB management facilities available in it.

2. Python language was used

3. There is only table currently created for this - user_dob with columns username and date_of_birth. There were 2 choices here:
   a. Store the DOB as is ie. a string value and do the math in python before returning the message
   b. Create 3 separate colums for date, month and year so as making it easier during the calcualation.

   I choose first becuase although there are many ways of slicing and dicing and storing the data, the first choice gives the fasts and most readble format. Of course depending on other business requirements, this decision could do either way.

4. Another error handling outside of provided business rule that was added was to check if the user is valid or not before sending any birthday message.

5. Some of the error messages are on purpose generic ex: Bad username/date of birth provided so as to protect the system from any attacks. This is in line with the theory where if an attacker is making API calls and it errors out, they shouldn't be told what the right way to access is to delay any potential impact. I understand its not important for this case but I would highly recommend this for any production env.

6. There should also be an authentication method which was omitted in this particular project. 
