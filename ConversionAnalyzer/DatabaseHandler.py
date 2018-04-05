import java.sql
from config import configParams
import java
from java.sql import Statement

def connect(params):
    assert(isinstance(params, configParams))
    driver = params.database.driver
    java.lang.Class.forName(driver).newInstance(  )
    server= params.database.host
    db =  params.database.database
    usr = params.database.user
    passwd = params.database.password
    url = "jdbc:mysql://%s/%s?user=%s&password=%s" % (
        server, db, usr, passwd)
    conn = java.sql.DriverManager.getConnection(url)
    return conn

def writeErrors(conn, errors):
    def writeError(conn, error):
        query = "SELECT * FROM errors WHERE errortext=?"
        stmt = conn.prepareStatement(query)
        stmt.setString(1, error)
        has_entry = False
        errorID = -1
        if stmt.execute():
            rs = stmt.getResultSet(  )
            while rs and rs.next(  ):
                has_entry = True
                errorID = rs.getInt("ID")
        stmt.close()
        if not has_entry:
            stmt_insert = conn.prepareStatement("INSERT INTO errors (`errortext`) VALUES (?)", Statement.RETURN_GENERATED_KEYS)
            stmt_insert.setString(1, error)
            stmt_insert.executeUpdate()
            keys = stmt_insert.getGeneratedKeys()
            while keys.next():
                errorID = keys.getInt(1)
            stmt_insert.close()
        return errorID

    list_of_errors = []
    for sprite in errors:
        errorID = writeError(conn, "".join(errors[sprite]))
        list_of_errors.append(errorID)
    return list_of_errors


def insertProject(conn, pid):
    query = "INSERT INTO conversions (PID) VALUES (?);"
    stmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
    stmt.setInt(1, pid)
    stmt.executeUpdate()
    keys = stmt.getGeneratedKeys()
    id = -1
    while keys.next():
        id = keys.getInt(1)
    stmt.close()
    return id


def insertErrorOccurances(conn, pid, errors):
    for error in errors:
        query = "INSERT IGNORE INTO error_occurences (CID, EID) VALUES (?, ?);"
        stmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        stmt.setInt(1, pid)
        stmt.setInt(2, error)
        stmt.executeUpdate()

    return