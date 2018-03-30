import java.sql

import java, javax
from java.sql import Statement

def connect():
    driver = "com.mysql.jdbc.Driver"
    java.lang.Class.forName(driver).newInstance(  )
    server, db = "localhost", "conversion_analysis"
    usr, passwd = "root", "1"
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
                print(rs.getInt("ID"))
        stmt.close()
        if not has_entry:
            stmt_insert = conn.prepareStatement("INSERT INTO errors (`errortext`) VALUES (?)")
            stmt_insert.setString(1, error)
            errorID = stmt_insert.executeUpdate(Statement.RETURN_GENERATED_KEYS)
            stmt_insert.close()
        return errorID

    list_of_errors = []
    for sprite in errors:
        print errors[sprite]
        print "______________________________________________________"
        errorID = writeError(conn, "".join(errors[sprite]))
        list_of_errors.append(errorID)
    return list_of_errors


def insertProject(conn, pid):
    query = "INSERT INTO conversions (PID) VALUES (?);"
    stmt = conn.prepareStatement(query)
    stmt.setInt(1, pid)
    id = stmt.executeUpdate(query, Statement.RETURN_GENERATED_KEYS)

    stmt.close()
    return id
