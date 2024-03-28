# The List - Unit 4 Mini Project

- **App Name: The List Roulette**
- **Description: A full CRUD application for keeping track of all those things you told people you would eventually watch and for generating a random option by genre so you might actually watch some of those things.**

- ![GitHub Url](https://github.com/mackwick/thelistBE)
- Deployed Backend:
- Trello Board:

## List of Dependencies

- TBD

## Route Map

### Show routes (shows == both shows and movies)

|     Route      |    Endpoint    | Method |                     Description                      |
| :------------: | :------------: | :----: | :--------------------------------------------------: |
|     Index      |     /show      |  Get   |                  Returns all shows                   |
|  Index comedy  |  /show/comedy  |  Get   |       Return all shows with a genre of comedy        |
|  Index drama   |  /show/drama   |  Get   |        Return all shows with a genre of drama        |
| Index thriller | /show/thriller |  Get   |   Return all shows with a genre of thriller/horror   |
| Index reality  | /show/reality  |  Get   | Return all shows with a genre of reality/documentary |
|  Index weird   |  /show/weird   |  Get   |     Return all shows with a genre of just weird      |
|  Index other   |  /show/other   |  Get   |    Return all shows with a genre of other/unsure     |
|    Destroy     |   /show/:id    | Delete |                 Delete a show by id                  |
|     Update     |   /show/:id    |  Put   |                 Update a show by id                  |
|     Create     |     /show      |  Post  |                Add a show to the list                |
|      Show      |   /show/:id    |  Get   |              Return show details by id               |

## ERD (Entity Relationship Diagram)

**FYI: User model/auth is a stretch goal**

![ERD](https://i.imgur.com/7H4jIcy.png)
