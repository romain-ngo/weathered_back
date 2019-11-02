# API

API endpoints documentation.

### User

- Create new user: `POST /user`  
  * body:

  ```json
  {
    "email": "string",
    "username": "string",
    "password": "string"
  }
  ```
  * response:
    * 400: missing field or duplicate email
    * 201: user created

- Edit a user (access jwt required): `PUT /user/:id`  
  * body:

  ```json
  {
    "id": "integer",
    "email": "string (optional)",
    "username": "string (optional)",
    "currentPassword": "string (optional)",
    "newPassword": "string (mandatory if currentPassword specified)"
  }
  ```
  * response:
    * 400: missing id field
    * 401: wrong password
    * 500: duplication
    * 200: success

- Add a location to a user (access jwt required): `POST /user/:userId/location/:locationId`  
  * response:
    * 201: location successfully added

- Remove a location from a user (access jwt required): `DELETE /user/:userId/location/:locationId`
  * response:
    * 200: location successfully deleted

- Log in: `POST /login`  
  * body:

  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```

  * response:
    * 400: email does not exist
    * 401: wrong password
    * 200: success (user and jwt returned)

- Refresh access token (refresh jwt required): `GET /refresh`  
  _Access token appended in authorization header_

  * response:
    * 200: success (new access token returned)

### Location

- Add new location (access jwt required): `POST /location`  
  * body:

  ```json
  {
    "id": "integer",
    "country": "string",
    "city": "string",
    "latitude": "integer",
    "longitude": "integer"
  }
  ```
  * response:
    * 201: location successfully added
    * 204: location already exist
    * 400: error in the request