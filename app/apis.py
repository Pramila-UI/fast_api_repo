from .main import app ,engine_connect
from sqlalchemy  import text 
from datetime import date

@app.get('/get_all_user')
def get_all_users():
    try:
        with engine_connect.connect() as conn:
            sql = text("SELECT * FROM users;")
            result = conn.execute(sql)
        
        list_user =[]
        for row in result:
            user_dict = {}
            user_dict['id'] = row[0]
            user_dict['fullname'] = row[1]
            user_dict['email_id'] = row[2]
            user_dict['gender'] = row[3]
            user_dict['dob'] = row[4]
            user_dict['created_date'] = row[5]
            list_user.append(user_dict)

        return   {
            "Status" : "Success" ,
            "user_details_list" : list_user
        }

    except Exception as e:
        return {
            "Status" : "Failure" ,
            "Message" : f"Exception while fetching the user list : {e}"
        }
    
@app.get('/get_user_details/{id}')
def get_particluar_user(id:int):
    try:
        where_con = f"id = {id}"
        res = checking_user_exists(where_con)
        if res['Status'] == "Success":
            if res['Result'] == 1:
                with engine_connect.connect() as conn:
                    sql = text(f"SELECT * FROM users WHERE {where_con}")
                    result = conn.execute(sql)
                    for row in result:
                        user_dict = {}
                        user_dict['id'] = row[0]
                        user_dict['fullname'] = row[1]
                        user_dict['email_id'] = row[2]
                        user_dict['gender'] = row[3]
                        user_dict['dob'] = row[4]
                        user_dict['created_date'] = row[5]
                    
                    return {
                        "Status" : "Success" ,
                        "user_details" : user_dict
                    }
            else:
                return {
                    "Status" : "Failure"  ,
                    "Message" : "There is no user for present for the provided id"
                }
        return res

    except Exception as e:
        return {
            "Status" : "Failure" ,
            "Message" : f"Exception while fetching the user details: {e}"
        }


@app.delete('/delete_user/{id}')
def get_particluar_user(id:int):
    try:
        where_con = f"id = {id}"
        res = checking_user_exists(where_con)
        if res['Status'] == "Success":
            if res['Result'] == 1:
                with engine_connect.connect() as conn:
                    sql = text(f"DELETE  FROM users WHERE {where_con}")
                    result = conn.execute(sql)
                    conn.commit()

                    return {
                        "Status" : "Success" ,
                        "Message" : "User deleted successfully"
                    }
            else:
                return {
                    "Status" : "Failure"  ,
                    "Message" : "There is no user for present for the provided id"
                }
        return res

    except Exception as e:
        return {
            "Status" : "Failure" ,
            "Message" : f"Exception while fetching the user details: {e}"
        }
    

@app.post('/add_new_user')
def insert_user_data(user_data : dict):
    try:
        fullname = user_data.get('fullname' ,'')
        email_id = user_data.get('email_id' ,'')
        gender = user_data.get('gender','')
        dob = user_data.get('dob','')
        created_date = date.today()

        if (fullname == '') or (fullname == None):
            return {
                "Status" : "Failure" ,
                "Message" : "Provide the fullname"
            }
        if (email_id == '') or (email_id == None):
            return {
                "Status" : "Failure" ,
                "Message" : "Provide the email id"
            }
        
        ### check that email-id is already exists
        where_con = f"email_id = '{email_id}'"
        res = checking_user_exists(where_con)
        if res['Status'] == "Success":
            if res['Result'] > 0:
                return {
                    "Status" : "Failure" ,
                    "Message" : f"User already present for this {email_id}"
                }
        else:
            return res
    
        with engine_connect.connect() as conn:
            sql = f"insert into users (`fullname` ,`email_id` ,`gender`,`dob` , `created_date`) values ('{fullname}' ,'{email_id}','{gender}','{dob}','{created_date}')"
            result = conn.execute(text(sql))
            conn.commit()
        
        return {
            "Status" : "Success" ,
            "Message" : "New User added Successfully"
        }
         
    except Exception as e:
        return {
            "Status" : "Failure" ,
            "Message" : f"Exception while inserting the user data : {e}"
        }


@app.put('/update_user/{id}')
def update_particluar_user(id:int , user_details :dict = {}):
    try:
        where_con = f"id = {id}"
        res = checking_user_exists(where_con)
        if res['Status'] == "Success":
            if res['Result'] == 1:
                """ update the details """
                update_con = "" 
                count = 0
                for i , j in user_details.items():
                    update_con = update_con + f"{i} = '{j}'"
                    count += 1 
                    if count != len(user_details.keys()):
                        update_con = update_con + ","

                if update_con != "":
                    with engine_connect.connect() as conn:
                        sql = text(f"UPDATE users SET {update_con} WHERE {where_con}")
                        conn.execute(sql)
                        conn.commit()

                    return {
                        "Status" : "Success" ,
                        "Message" : "User Details Updated Successfully"
                    }
                else:
                    return {
                        "Status" : "Failure" ,
                        "Message" : "No data is Provided for Update"
                    }

            else:
                return {
                    "Status" : "Failure"  ,
                    "Message" : "There is no user for present for the provided id"
                }
        return res

    except Exception as e:
        return {
            "Status" : "Failure" ,
            "Message" : f"Exception while fetching the user details: {e}"
        }


def checking_user_exists(where_condition):
    try:
        with engine_connect.connect() as conn:
            sql = text(f"SELECT COUNT(*) FROM users WHERE {where_condition}")
            result = conn.execute(sql)
            count = None
            for row in result:
                count = row[0]

        return {
            "Status":"Success" ,
            "Result" : count
        }        

    except Exception as e:
        return {
            "Status" : "Faiure",
            "Message" : f"Exception while cheecking user exists : {e}"
        }

