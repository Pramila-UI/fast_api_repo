Create the mysql database in the docker file and perform the crud operation using the fast api

Run the Project
Install the docker in the system
In the terminal enter into the root project directory execute the following command .
1. docker-compose build
2 .docker-compose up -d

## Followings are the url for the crud operation 

Base Url :- 
Method - get 
http://127.0.0.1:8000  


Get all user list :- 
Method - get 
http://127.0.0.1:8000/get_all_user


Get particular use details : - 1 is the id of the user 
Method - get 
http://127.0.0.1:8000/get_user_details/1


Delete the user  :- 7 is the id of the user 
Method - delete 
http://127.0.0.1:8000/delete_user/7



Update the user details : 1 is the id of the user 
Method - put 
http://127.0.0.1:8000/update_user/1

Request : - 
{
  "fullname" :"pramila"
}


Add the new user :- 
Method : post 
http://127.0.0.1:8000/add_new_user

Request: -
{
  "fullname" : "Pramila B",
  "email_id" : "Pramila@mailinator.com",
  "gender" : "Female" ,
  "dob": "1998-07-21”
}
