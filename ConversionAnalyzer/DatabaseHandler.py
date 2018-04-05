import mysql.connector
from config import configParams
from mysql.connector.cursor import MySQLCursor
def connect(params):
    assert(isinstance(params, configParams))
    server= params.database.host
    db =  params.database.database
    usr = params.database.user
    passwd = params.database.password
    cnx = mysql.connector.connect(user=usr, password=passwd,
                                  host=server,
                                  database=db)
    return cnx

def writeErrors(conn, errors):
    def writeError(conn, error):
        query = "SELECT * FROM errors WHERE errortext=%(errortext)s"
        data = {
            'errortext': error,
        }
        assert (isinstance(conn, mysql.connector.MySQLConnection))
        cursor = conn.cursor(dictionary=True)
        assert isinstance(cursor, MySQLCursor)
        cursor.execute(query, data)
        has_entry = False
        errorID = -1
        for entry in cursor:
            has_entry = True
            errorID = entry["ID"]
        if not has_entry:
            query = "INSERT INTO errors (`errortext`) VALUES (%(errortext)s)"
            cursor.execute(query, data)
            errorID = cursor.getlastrowid()
        cursor.close()
        return errorID

    list_of_errors = []
    for sprite in errors:
        errorID = writeError(conn, "".join(errors[sprite]))
        list_of_errors.append(errorID)
    return list_of_errors


def insertProject(conn, pid):
    query = "INSERT INTO conversions (PID) VALUES (%(pid)s);"
    data = {
        'pid': pid,
    }
    assert (isinstance(conn, mysql.connector.MySQLConnection))
    cursor = conn.cursor()
    assert isinstance(cursor, MySQLCursor)
    cursor.execute(query, data)
    id = cursor.getlastrowid()
    cursor.close()
    return id


def insertErrorOccurances(conn, pid, errorIDs):
    assert (isinstance(conn, mysql.connector.MySQLConnection))
    cursor = conn.cursor()
    assert isinstance(cursor, MySQLCursor)
    for errorID in errorIDs:
        data = {
            'pid': pid,
            'errorID': errorID
        }
        query = "INSERT IGNORE INTO error_occurences (CID, EID) VALUES (%(pid)s, %(errorID)s);"
        cursor.execute(query, data)
    cursor.close()
    return