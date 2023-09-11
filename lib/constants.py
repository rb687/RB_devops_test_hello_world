CREATE_TABLE_USER_DOB = """
CREATE TABLE user_dob (
    username varchar(255),
    date_of_birth varchar (15)
);
"""

PRIMARY_KEY_ALTER = """
ALTER TABLE user_dob
ADD PRIMARY KEY (username);
"""

TEST_QUERY = """
SELECT 1;
"""

UPDATE_DOB = """
INSERT INTO user_dob 
(username, date_of_birth)
VALUES 
("{username}", "{dob_insert}")
ON DUPLICATE KEY 
UPDATE 
    date_of_birth = "{dob_update}"
"""


GET_DOB = """
SELECT date_of_birth FROM user_dob
WHERE 
    username = "{username}";
"""

USER_EXISTS = """
SELECT username FROM user_dob
WHERE 
    username = "{username}";
"""

ERROR_RESPONSE_MESSAGE = "Bad Request"

