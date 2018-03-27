import httplib
from ProjectDownload import ProjectDownload

def main():
    projectDownloader = ProjectDownload()
    id = projectDownloader.findProjectBySearch("cat",0)
    project = projectDownloader.convert(id)
    print str(id)
    print project

    pass

if __name__ == '__main__':
    main()