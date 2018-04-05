from ProjectDownload import ProjectDownload
import DatabaseHandler
from time import sleep
from config import configParams

params = None
def main():
    global params
    params = configParams().readConfig()
    projectDownloader = ProjectDownload()
    for offset in range (params.start_offset, params.end_offset):
        convert_single_project_and_insert_errors(projectDownloader, params.keyword, offset)
        print "------------------------------------------------------------------"

def convert_single_project_and_insert_errors(projectDownloader, keyword, offset):
    global params
    id = projectDownloader.findProjectBySearch(keyword,offset)
    error = projectDownloader.convert(id, params)
    conn = DatabaseHandler.connect(params)
    database_error_ids = DatabaseHandler.writeErrors(conn, error)
    database_pid = DatabaseHandler.insertProject(conn, id)
    DatabaseHandler.insertErrorOccurances(conn, database_pid, database_error_ids)
    conn.close()
    sleep(5)
    pass

if __name__ == '__main__':
    main()