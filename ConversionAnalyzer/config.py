from scratchtocatrobat.tools import helpers

class configParams(object):
    keyword = None
    start_offset = 0
    end_offset = 1

    def readConfig(self):
        config = helpers._setup_configuration("config/default.ini")
        self.keyword = config.config_parser.get("ConversionAnalyzer", "keyword")
        self.start_offset = config.config_parser.getint("ConversionAnalyzer", "start_offset")
        self.end_offset = config.config_parser.getint("ConversionAnalyzer", "end_offset")

        self.database.database = config.config_parser.get("Database", "database")
        self.database.user = config.config_parser.get("Database", "user")
        self.database.password = config.config_parser.get("Database", "password")
        self.database.driver = config.config_parser.get("Database", "driver")
        self.database.host = config.config_parser.get("Database", "host")
        return self

    class database:
        user = ""
        password = ""
        database = ""
        driver = ""
        host = ""