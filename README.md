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

|  Route  | Endpoint  | Method |                          Description                           |
| :-----: | :-------: | :----: | :------------------------------------------------------------: |
|  Index  |   /show   |  Get   |                       Returns all shows                        |
| Destroy | /show/:id | Delete | Delete a show by id and remove it from the associated genre(s) |
| Update  | /show/:id |  Put   |     Update a show by id and update the assocated genre(s)      |
| Create  |   /show   |  Post  |                     Add a show to the list                     |
|  Show   | /show/:id |  Get   |                   Return show details by id                    |

### Genre routes

| Route | Endpoint  | Method |        Description        |
| :---: | :-------: | :----: | :-----------------------: |
| Index |   /list   |  Get   |    Returns all genres     |
| Show  | /list/:id |  Get   | Return show details by id |

## ERD (Entity Relationship Diagram)

**FYI: User model/auth is a stretch goal**

![ERD](https://i.imgur.com/7H4jIcy.png)
