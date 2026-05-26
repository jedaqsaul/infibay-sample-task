# Broken Flask Registration API

A Flask registration endpoint is currently behaving incorrectly.

Endpoint:

POST /register

Expected behavior:

- Accept JSON body
- Require:
  - email
  - password

Validation:

- email must be valid
- password minimum length is 6

Responses:

Success:
201

{
"message":"User created successfully"
}

Failure:
400

Current known issues:

- invalid emails are accepted
- weak passwords pass
- missing fields are not handled correctly
- success responses use incorrect status codes

Task:

Fix the implementation so all tests pass.

Do not modify test files.
