import httplib
import json
import os

class ProjectDownload(object):
    def __init__(self):
        pass
    def findProjectBySearch(self, querystring, offset):
        con = httplib.HTTPSConnection("api.scratch.mit.edu")
        con.request("GET","/search/projects?q="+querystring+"&offset="+str(offset)+"&limit=1")
        response = con.getresponse()
        if response.status != 200:
            raise Exception("Bad Response")
        jsonResponse = json.loads(response.read())
        return jsonResponse[0]["id"]

    def convert(self, projectID):
        code_xml_content = ""
        dir = os.path.dirname(os.getcwd())
        jythonpath = "/usr/jython/bin/jython" #TODO: get it differently
        os.system(jythonpath+" "+dir+"/run_dbg "+ "https://scratch.mit.edu/projects/"+str(projectID) + " --extracted" + " 2> out.txt")
        log_file = open("out.txt", "r")
        filtered_log = ""
        last_converted_sprite = ""
        is_new_sprite = True
        in_traceback = False
        traceback = ""
        filtered_log_dict = dict()
        for line in log_file.readlines():
            if "Converting Sprite:" in line:
                last_converted_sprite = line
                is_new_sprite = True
            interestingLine = "WARNING" in line
            interestingLine |= "ERROR" in line
            if in_traceback:
                in_traceback = not line.strip()[0].isdigit()
                if not in_traceback:
                    filtered_log_dict[last_converted_sprite].append(traceback)
                    traceback = ""
            in_traceback |= "Traceback" in line


            if not interestingLine and not in_traceback:
                continue
            filtered_log += str(interestingLine) +" , "+ str(in_traceback) + "\n"
            if is_new_sprite: #write sprite line only once and only if we need it
                filtered_log_dict[last_converted_sprite] = []
                filtered_log += last_converted_sprite
                is_new_sprite = False
            if interestingLine:
                filtered_log_dict[last_converted_sprite].append(line)
            elif in_traceback:
                traceback += line

        log_file.close()
        print filtered_log
        print filtered_log_dict


        return code_xml_content