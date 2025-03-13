
![copil-color-cool](https://github.com/Jarvx200/PbInfoAPI/assets/147537737/b3aec21d-7e51-47e7-9c35-4a83cd6f63d0)


# Unofficial PbInfo (Webscraping) API

This is a project attempting to be a user friendly way to geather **public available** data about user and problems of the programming website [PbInfo](www.pbinfo.ro), so they can be later used in other people's apps. \
The project directory also includes a simple html frontent for easier testing for the `/users/` (data visualization).

## Technologies Used

The whole API is written in python with flask, although python is not known for it's speed, I tried mitigating those type of problems by introducing mechanisms that I describe in the **Features** part
For storing data, I used `.yaml` files and will use `.json` for logs so i can parse them easier further down the road in an admin panel frontend.
For the data visualization page I used good ol' HTML and a little js for data fecthing.

## How to run the API locally 
-  Clone the repo: `git clone https://github.com/Jarvx200/PbInfoAPI.git`
- `cd api`
- `pip install -r requirements.txt`
- `python3 main.py`


### Features
  - Can lookup by name/id any problem *
  - Can lookup users by username
  - Indexes problems/id while the api is used in a `.yaml`
  - Implements caches for users/problems

  * the problems can e searched by name only if they were previously indexed and searched by `id`

### Todo:
  - [ ] Convert list caching to hashmap caching for problems
  - [ ] Add logging for all endpoints
  - [ ] Add admin dashboard to track usage
  - [ ] Implement key based authentication with keys that can expire/be left with no uses
  - [x] Add requirements.txt

