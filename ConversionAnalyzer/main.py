import httplib
from ProjectDownload import ProjectDownload
import DatabaseHandler

def main():
    projectDownloader = ProjectDownload()
    id = projectDownloader.findProjectBySearch("cat",0)
    error = projectDownloader.convert(id)
    print str(id)
    print error
    conn = DatabaseHandler.connect()
    DatabaseHandler.writeErrors(conn, error)
    conn.close()
    pass

if __name__ == '__main__':
    main()