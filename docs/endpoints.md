# User API

## Endpoints

### List Users

### User
- **GET**: get my user(ME)
  - *url*: `api/v1/users/me`
  - *Handler*: `Me.get()`
- **PATCH**: update my user info
  - *url*: `api/v1/users/me`
  - *Handler*: `Me.patch()`
- **POST**: create a new user
  - *url*: `api/v1/users`
  - *Handler*: `Users.post()`
- **GET**: get user info
  - *url*: `api/v1/users/username`
  - *Handler*: `PublicUser.get()`
- **POST**: sign-in
  - *url*: api/v1/users/sign-in
  - *Handler*: `SignIn.post()`

# mingl
- **POST**: Create a new user
  - **URL**: `/api/v1/users`
  - **Handler**: `Users.post()`

### User Details
- **GET**: Retrieve a user by ID
  - **URL**: `/api/v1/users/<int:pk>`
  - **Handler**: `UserDetail.get()`

- **PUT**: Update a user by ID
  - **URL**: `/api/v1/users/<int:pk>`
  - **Handler**: `UserDetail.put()`

- **DELETE**: Delete a user by ID
  - **URL**: `/api/v1/users/<int:pk>`
  - **Handler**: `UserDetail.delete()`
