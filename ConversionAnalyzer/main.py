import httplib
from ProjectDownload import ProjectDownload
import DatabaseHandler
from time import sleep

def main():
    projectDownloader = ProjectDownload()
    for offset in range (100, 200):
        convert_single_project_and_insert_errors(projectDownloader, "cat", offset)
        print "------------------------------------------------------------------"

def convert_single_project_and_insert_errors(projectDownloader, keyword, offset):
    id = projectDownloader.findProjectBySearch(keyword,offset)
    error = projectDownloader.convert(id)
    conn = DatabaseHandler.connect()
    database_error_ids = DatabaseHandler.writeErrors(conn, error)
    database_pid = DatabaseHandler.insertProject(conn, id)
    DatabaseHandler.insertErrorOccurances(conn, database_pid, database_error_ids)
    conn.close()
    sleep(5)
    pass

if __name__ == '__main__':
    main()