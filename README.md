# FSND Capstone Project

### Project description:
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.


### Models:
**Movies** with attributes:
- title:*string*
- release_date:*string*
  
**Actors** with attributes:
- name:*string*
- age:*integer*
- gender:*string*




### Permissions:
There are three type of users (roles) in the system:
- Casting Assistant
- Casting Director
- Executive Director

The permissions based on the role and shown in the following list:
- **Casting Assistant**
  - Can view actors and movies
- **Casting Director**
  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies
- **Executive Producer**
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database


And there are multiple scopes to manipulate resources:
- `get:casting-assistant`
- `delete:executive-producer`
- `delete:casting-director`
- `post:executive-producer`
- `patch:casting-director`
- `post:casting-director`

### Authentication & Deployment URL:

#### Heroku URL:
`https://ghawanni-fsnd-capstone.herokuapp.com/`

#### Authentication Token per role (and no role for testing):
```json
{
  "roles": {
      "Casting Assistant": {
          "description": "Can view actors and movies",
          "jwt_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAzVTlKRmVYc2lNbXRpVHVxVFVIZSJ9.eyJpc3MiOiJodHRwczovL2doYXdhbm5pLWZzbmQtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6Im52bnJ1MUd0dkx3c3QxMzlPTEhmOUJtRXdBMXpBbGZEQGNsaWVudHMiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTU5ODk3MDAyOCwiZXhwIjoxNTk5MDU2NDI4LCJhenAiOiJudm5ydTFHdHZMd3N0MTM5T0xIZjlCbUV3QTF6QWxmRCIsInNjb3BlIjoiZ2V0OmNhc3RpbmctYXNzaXN0YW50IiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmNhc3RpbmctYXNzaXN0YW50Il19.ZXJWJS0D0iPm-0WnNPinl40CgPQZHht8lFXroqTDlzGQvdMjVNoYW6bBPnQRPKk1-BYivtILtd785rB-pJOIquupu9UsuDqnjXH1VWMobjkVk2j-sHxerJ8w7zM4JjTVGxI7kOOqA-wJ-J3A6o-q3PXSerVE1yGDTbdR9u-OnXA2eydCtdLCypiI0ori6TYewPLIaBCXFocEPNOM9T0F8ZjrqtRieXbalE8GGZjsRmq4hfk45wXFOMC_ef7SudvRgfdOfeoajdB7e0qF3gy1X0LbVvzJ7KndD6FUan6NlXTtO5_67r5Iv4KJzSnHi4X35aEaGAE4SVM3UNqjxK7NEA",
          "permissions": ["get:casting-assistant"]
      },
      "Casting Director": {
          "description": "All permissions a Casting Assistant has and add or delete an actor from the database and modify actors or movies",
          "jwt_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAzVTlKRmVYc2lNbXRpVHVxVFVIZSJ9.eyJpc3MiOiJodHRwczovL2doYXdhbm5pLWZzbmQtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6Im52bnJ1MUd0dkx3c3QxMzlPTEhmOUJtRXdBMXpBbGZEQGNsaWVudHMiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTU5ODk2OTkyMiwiZXhwIjoxNTk5MDU2MzIyLCJhenAiOiJudm5ydTFHdHZMd3N0MTM5T0xIZjlCbUV3QTF6QWxmRCIsInNjb3BlIjoiZ2V0OmNhc3RpbmctYXNzaXN0YW50IGRlbGV0ZTpleGVjdXRpdmUtcHJvZHVjZXIgZGVsZXRlOmNhc3RpbmctZGlyZWN0b3IgcG9zdDpleGVjdXRpdmUtcHJvZHVjZXIgcGF0Y2g6Y2FzdGluZy1kaXJlY3RvciBwb3N0OmNhc3RpbmctZGlyZWN0b3IiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2FzdGluZy1hc3Npc3RhbnQiLCJkZWxldGU6ZXhlY3V0aXZlLXByb2R1Y2VyIiwiZGVsZXRlOmNhc3RpbmctZGlyZWN0b3IiLCJwb3N0OmV4ZWN1dGl2ZS1wcm9kdWNlciIsInBhdGNoOmNhc3RpbmctZGlyZWN0b3IiLCJwb3N0OmNhc3RpbmctZGlyZWN0b3IiXX0.WwYaqn8UMAkMM80emTDEx0rJi7YPswHQrS25F-hYORtFSDLlpSpbwPrqDlVI46tVgdx6_UuyK_JK-jP0s2VngEv2ZEnhbEp89GaI6-jF1KPA8HfPq4RRTJ2nkUASeEpSD_1Dmm_qu0H-nii5u9KelrVK-e6xQNNd3TcuDAknx4gwZ-GjeBwnt6jXUWIgVfzu_VgwBOsLtCQXS3XjCDS7bax67-dp71SCTJSJ4B65yvwgGD1de5P6XaVZl5cQM6VGL9_2CSzFdTnADODDac69JGjTlSvOmVjfnsjjaKVx_8OkQMAT9Pnx_toCMkkM75WmH4wJiNoOxqjvFSyIbiJocA",
          "permissions": ["get:casting-assistant", "post:casting-director", "delete:casting-director", "patch:casting-director"]
      },
      "Executive Producer": {
          "description": "All permissions a Casting Director has and add or delete a movie from the database",
          "jwt_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAzVTlKRmVYc2lNbXRpVHVxVFVIZSJ9.eyJpc3MiOiJodHRwczovL2doYXdhbm5pLWZzbmQtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6Im52bnJ1MUd0dkx3c3QxMzlPTEhmOUJtRXdBMXpBbGZEQGNsaWVudHMiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTU5ODk2OTkyMiwiZXhwIjoxNTk5MDU2MzIyLCJhenAiOiJudm5ydTFHdHZMd3N0MTM5T0xIZjlCbUV3QTF6QWxmRCIsInNjb3BlIjoiZ2V0OmNhc3RpbmctYXNzaXN0YW50IGRlbGV0ZTpleGVjdXRpdmUtcHJvZHVjZXIgZGVsZXRlOmNhc3RpbmctZGlyZWN0b3IgcG9zdDpleGVjdXRpdmUtcHJvZHVjZXIgcGF0Y2g6Y2FzdGluZy1kaXJlY3RvciBwb3N0OmNhc3RpbmctZGlyZWN0b3IiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2FzdGluZy1hc3Npc3RhbnQiLCJkZWxldGU6ZXhlY3V0aXZlLXByb2R1Y2VyIiwiZGVsZXRlOmNhc3RpbmctZGlyZWN0b3IiLCJwb3N0OmV4ZWN1dGl2ZS1wcm9kdWNlciIsInBhdGNoOmNhc3RpbmctZGlyZWN0b3IiLCJwb3N0OmNhc3RpbmctZGlyZWN0b3IiXX0.WwYaqn8UMAkMM80emTDEx0rJi7YPswHQrS25F-hYORtFSDLlpSpbwPrqDlVI46tVgdx6_UuyK_JK-jP0s2VngEv2ZEnhbEp89GaI6-jF1KPA8HfPq4RRTJ2nkUASeEpSD_1Dmm_qu0H-nii5u9KelrVK-e6xQNNd3TcuDAknx4gwZ-GjeBwnt6jXUWIgVfzu_VgwBOsLtCQXS3XjCDS7bax67-dp71SCTJSJ4B65yvwgGD1de5P6XaVZl5cQM6VGL9_2CSzFdTnADODDac69JGjTlSvOmVjfnsjjaKVx_8OkQMAT9Pnx_toCMkkM75WmH4wJiNoOxqjvFSyIbiJocA",
          "permissions": ["get:casting-assistant", "post:casting-director", "delete:casting-director", "patch:casting-director","post:executive-producer", "delete:executive-producer"]
      },
      "No Role": {
        "description": "No permissions",
        "jwt_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAzVTlKRmVYc2lNbXRpVHVxVFVIZSJ9.eyJpc3MiOiJodHRwczovL2doYXdhbm5pLWZzbmQtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6Im52bnJ1MUd0dkx3c3QxMzlPTEhmOUJtRXdBMXpBbGZEQGNsaWVudHMiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTU5ODk3MTIwNiwiZXhwIjoxNTk5MDU3NjA2LCJhenAiOiJudm5ydTFHdHZMd3N0MTM5T0xIZjlCbUV3QTF6QWxmRCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.rFQ98LUEkEPSWCNkCZSABiQwvk3LtGU-JhsvbOaUp4InQQXKBnLj-6ghTqy6invLx-ZymWPqpbsoblHguKIQv71sOE9Jk6tCLumYDZwYJ1G2MEy-oei05-jqQvQz_UbrCsX5FFzqD7tNRLu_ljFP0ChdmbuLadK3soLLEqOe3owke_UOHdxu6B3a70kZrGcaqlI5GDR1vRisCnjLe0W9A7GdgYInqTyzfIOShPEmRWxyZbMdkGQndmERidH40VXjH7yRO6mHsvkkLzQACbPTTfXqn6YXMQ137QsRNH2P2bMCPyu-ACvGXu0PWcU-7J502yF65prQR1m_VfDFKDMjxQ",
        "permissions": []
      }
  }
}
```

### Postman Collection
Included in the project repository a Postman collection `(file: Udacity Capstone.postman_collection.json)` with preset variable and token to make testing easy.

Please feel free to import it and use it :)
### Endpoints:
#### GET /movies
Get all movies

Require `get:casting-assistant`

Expected Result:
```json
{
  "movies": [
    {
      "id": 1,
      "release_date": "2017",
      "title": "The Martian"
    }
  ],
  "success": true,
  "total_movies": 1
}
```

#### GET /actors
Get all actors

Require `get:casting-assistant`

Expected Result:
```json
{
  "actors": [
    {
      "age": 50, 
      "gender": "M", 
      "id": 1, 
      "name": "Christian Bale"
    }, 
    {
      "age": 50, 
      "gender": "M", 
      "id": 2, 
      "name": "Christian Bale"
    }
  ], 
  "success": true, 
  "total_actors": 2
}


```
#### GET /movies/id
Get a movie by id

Require `get:casting-assistant`

Request:
```bash
curl --location --request GET 'https://ghawanni-fsnd-capstone.herokuapp.com//movies/1' \
--header 'Authorization: Bearer TOKEN'
```
Expected Result:
```json
{
  "release_date": "2017",
  "success": true,
  "title": "The Martian"
}
```

#### GET /actors/id
Get an actor by id

Require `get:casting-assistant`

Request:
```bash
curl --location --request GET 'https://ghawanni-fsnd-capstone.herokuapp.com//actors/1' \
--header 'Authorization: Bearer TOKEN'
```
Expected Result:
```json
{
  "age": 50,
  "gender": "M",
  "name": "Christian Bale",
  "success": true
}
```


#### DELETE /actors/id
Delete an actor by id

Require `delete:casting-director`

Request:
```bash
curl --location --request DELETE 'https://ghawanni-fsnd-capstone.herokuapp.com//actors/2' \
--header 'Authorization: Bearer TOKEN'
```
Expected Result:
```json
{
  "delete": 2,
  "success": true
}
```


#### DELETE /movies/id
Delete a movie by id

Require `delete:execultive-director`

Request:
```bash
curl --location --request DELETE 'https://ghawanni-fsnd-capstone.herokuapp.com//movies/2' \
--header 'Authorization: Bearer TOKEN'
```
Expected Result:
```json
{
  "delete": 2,
  "success": true
}
```



#### POST /movies/id
Delete a movie by id

Require `post:execultive-director`

Request:
```bash
curl --location --request POST 'https://ghawanni-fsnd-capstone.herokuapp.com//movies' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "One Flew Over the Cuckoo'\''s Nest",
    "release_date": "1975"
}'
```
Expected Result:
```json
{
  "movie": [
    {
      "id": 2,
      "release_date": "1975",
      "title": "One Flew Over the Cuckoo's Nest"
    }
  ],
  "success": true
}
```


#### POST /actors/id
Delete an actor by id

Require `post:casting-director`

Request:
```bash
curl --location --request POST 'https://ghawanni-fsnd-capstone.herokuapp.com//actors' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Christian Bale",
    "age": 50,
    "gender": "M"
}'
```
Expected Result:
```json
{
  "actor": [
    {
      "age": 50, 
      "gender": "M", 
      "id": 2, 
      "name": "Christian Bale"
    }
  ], 
  "success": true
}
```


#### PATCH /actors/id
edit an actor by id

Require `patch:casting-director`

Request:
```bash
curl --location --request PATCH 'https://ghawanni-fsnd-capstone.herokuapp.com//actors/1' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "hello actor",
    "age": "55"
}'
```
Expected Result:
```json
{
  "actor": [
    {
      "age": 55,
      "gender": "M",
      "id": 1,
      "name": "hello actor"
    }
  ],
  "success": true
}
```


#### PATCH /movies/id
edit a movie by id

Require `patch:casting-director`

Request:
```bash
curl --location --request PATCH 'localhost:5000/movies/1' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "One Flew Over the Cuckoo'\''s nest",
    "release_date": "1975"
}'
```
Expected Result:
```json
{
  "movie": [
    {
      "id": 1,
      "release_date": "1975",
      "title": "One Flew Over the Cuckoo's nest"
    }
  ],
  "success": true
}
```


### Error Handling:
Errors returned from this project are all using in the following format:

```json
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```
There are 3 possible error responses the API could return, here's each possible response and it's meaning:

400: Bad Request

404: Not Found

422: Cannot Proccess Request