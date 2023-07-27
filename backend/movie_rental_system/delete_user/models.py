from ..util.util import find_user_id


def delete_user(username, mydb):
    userid = find_user_id(username, mydb)
    query = f"DELETE FROM user WHERE uid={userid}"
    try:
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.commit()
        print("Account Deletion Successful")
        return True
    except Exception as err:
        print("Something went wrong: {}".format(err))
        return False
