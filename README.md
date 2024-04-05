# The List - Unit 4 Mini Project

- **App Name: The List Roulette**
- **Description: A full CRUD application for keeping track of all those things you told people you would eventually watch and for generating a random option so you might actually watch some of those things.**

- GitHub Url: https://github.com/mackwick/thelistBE
- Deployed Backend: https://thelistbe.onrender.com/shows/
- Trello Board: https://trello.com/b/mfma0H5j/unit-4-project-the-list-routlette

## Dependencies

- dj-database-url
- Django
- django-cors-headers
- django-environ
- djangorestframework
- gunicorn
- psycopg2-binary
- sqlparse

## Route Map

|     Route      |    Endpoint     | Method |                     Description                      |
| :------------: | :-------------: | :----: | :--------------------------------------------------: |
|     Index      |     /shows      |  Get   |                  Returns all shows                   |
|  Index comedy  |  /shows/comedy  |  Get   |       Return all shows with a genre of comedy        |
|  Index drama   |  /shows/drama   |  Get   |        Return all shows with a genre of drama        |
| Index thriller | /shows/thriller |  Get   |   Return all shows with a genre of thriller/horror   |
| Index reality  | /shows/reality  |  Get   | Return all shows with a genre of reality/documentary |
|  Index weird   |  /shows/weird   |  Get   |     Return all shows with a genre of just weird      |
|  Index scifi   |  /shows/other   |  Get   |    Return all shows with a genre of other/unsure     |
|    Destroy     |   /shows/:id    | Delete |                 Delete a show by id                  |
|     Update     |   /shows/:id    |  Put   |                 Update a show by id                  |
|     Create     |     /shows      |  Post  |                Add a show to the list                |
|      Show      |   /shows/:id    |  Get   |              Return show details by id               |

## ERD (Entity Relationship Diagram)

**FYI: User model/auth was a stretch goal and will be implemented post-graduation**

![ERD](https://i.imgur.com/7H4jIcy.png)
