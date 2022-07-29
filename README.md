[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org) 
# API for Yatube 

## About API for Yatube
A Python Application Program Interface based on Django Rest Framework to create, update, or delete posts, comments and followings in Yatube social network.

## Installation

Python 3.8 or later is required.
Clone repository and go to it on the command line:

`git clone git@github.com:epsilonm/api_final_yatube.git`

`cd api_final_yatube`

To make your life easier, you are encouraged to install into a virtualenv.

`python3 -m venv venv`

`source venv/Scripts/activate`

Update pip and install requerements from **requirements.txt**

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

Apply migrations

`cd yatube_api`

`python3 manage.py migrate`

Run API

`python3 manage.py runserver`

## Usage examples

### Get list of posts
Get list of all posts. If *limit* and *offset* are specified, response will be paginated. 
#### Request

`GET /api/v1/posts/`

`http://127.0.0.1:8000/api/v1/posts/`

With pagination:

`http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2/`

#### Response

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

With pagination:

```
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "previous": null,
    "results": [
        {
            "id": 2,
            "text": "1",
            "author": "dell",
            "image": null,
            "group": null,
            "pub_date": "2022-07-29T17:16:40.270155Z"
        },
        {
            "id": 3,
            "text": "2",
            "author": "dell",
            "image": null,
            "group": null,
            "pub_date": "2022-07-29T17:16:50.733601Z"
        }
    ]
}
```

### Create post
Anonymous requests are forbidden.
#### Request

`POST /api/v1/posts/`

`http://127.0.0.1:8000/api/v1/posts/`

##### Payload
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Retrieve post

#### Request

`GET /api/v1/posts/{id}/`

`http://127.0.0.1:8000/api/v1/posts/{id}/`

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Overwrite post 
Only author can overwrite post. Anonymous requests are forbidden.
#### Request

`PUT /api/vi/posts/{id}/`

`http://127.0.0.1:8000/api/v1/posts/{id}/`

##### Payload
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### Partial update post
Only author can update post. Anonymous requests are forbidden.
#### Request

`PATCH /api/v1/posts/{id}/`

`http://127.0.0.1:8000/api/v1/posts/{id}/`

##### Payload

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Delete post
Only author can delete post. Anonymous requests are forbidden.
#### Request

`DELETE /api/v1/posts/{id}/`

`http://127.0.0.1:8000/api/v1/posts/{id}/`

### Get list of comments to the post you have chosen

#### Request

`GET /api/v1/posts/{post_id}/comments/`

`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`

#### Response

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### Add comment to post
Anonymous requests are forbidden.
#### Request

`POST /api/v1/posts/{post_id}/comments/`

`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`

##### Payload

```
{
  "text": "string"
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Get comment

#### Request
`GET /api/v1/posts/{post_id}/comments/{id}/`

`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/`

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Overwrite comment
Only author can overwrite comment. Anonymous requests are forbidden.
#### Request
`PUT /api/v1/posts/{post_id}/comments/{id}/`
`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/`

##### Payload
```
{
  "text": "string"
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Partial update comment
Only author can update comment. Anonymous requests are forbidden.
#### Request

`PATCH /api/v1/posts/{post_id}/comments/{id}/`
`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/`

##### Payload
```
{
  "text": "string"
}
```

#### Response

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Delete comment
Only author can delete comment. Anonymous requests are forbidden.
#### Request

`DELETE /api/v1/posts/{post_id}/comments/{id}/`
`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/`

### Get list of groups

#### Request

`GET /api/v1/groups/`
`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/`

#### Response

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

### Get information about group

#### Request

`GET /api/v1/groups/{id}/`
`http://127.0.0.1:8000/api/v1/groups/{id}/`

#### Response

```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

### Get all user's subscriptions
Anonymous requests are forbidden.
#### Request

`GET /api/v1/follow/`
`http://127.0.0.1:8000/api/v1/follow/`

#### Response

```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

### Subscribe from requesting user on user in request body
Anonymous requests are forbidden.
#### Request

`POST /api/v1/follow/`
`http://127.0.0.1:8000/api/v1/follow/`

##### Payload
```
{
  "following": "string"
}
```

#### Response

```
{
  "user": "string",
  "following": "string"
}
```

### Recieve JWT-token

#### Request
`POST /api/v1/jwt/create/`
`http://127.0.0.1:8000/api/v1/jwt/create/`

##### Payload

```
{
  "username": "string",
  "password": "string"
}
```

#### Response

```
{
  "refresh": "string",
  "access": "string"
}
```

### Refresh JWT-token

#### Request

`POST /api/v1/jwt/refresh/`
`http://127.0.0.1:8000/api/v1/jwt/refresh/`

##### Payload
```
{
  "refresh": "string"
}
```

#### Response

```
{
  "access": "string"
}
```

### Check JWT-token

#### Request

`POST /api/v1/jwt/verify/`
`http://127.0.0.1:8000/api/v1/jwt/verify/`

##### Payload

```
{
  "token": "string"
}
```

#### Response

```
{
  "token": [
    "Обязательное поле."
  ]
}
```
