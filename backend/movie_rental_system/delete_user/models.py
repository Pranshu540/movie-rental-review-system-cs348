from MySQLdb import Error


def delete_user(userid, mydb):
    query = f"DELETE FROM user WHERE uid={userid}"
    try:
        cursor = mydb.connection.cursor()
        cursor.execute(query)
        mydb.commit()
        print("Account Deletion Successful")
        return True
    except Error as err:
        print("Something went wrong: {}".format(err))
        return False
