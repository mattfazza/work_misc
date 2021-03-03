import json
import sys

def ingestJSON(filePath):
    try:
        with open(filePath) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        sys.exit("Could not find file")
    except json.decoder.JSONDecodeError:
        sys.exit("Please provide a valid JSON file")
    except Exception:
        sys.exit("An error has occurred.")

def stitcher():
    global stitched_template
    stitched_template = {}
    baseTemplate = ingestJSON("/Users/mfazza/Code/work_misc/templates/modular_base.json") # remove this hardcoded mess

    put_together(stitched_template, baseTemplate)
    print(stitched_template)



def put_together(current_state, current_base):

    if current_state == {}:
        current_state["Project"] = "Project_Name" # remove this hardcoded one, please?

    if "Folders" not in current_base:
        return
    
    level = map(lambda x: {"name": x}, current_base["Folders"])
    
    current_state["Folders"] = list(level)

    for folder_index in range(len(current_state["Folders"])):
        try:
          put_together(current_state["Folders"][folder_index], current_base["Model"])
        except KeyError:
            return

stitcher()

