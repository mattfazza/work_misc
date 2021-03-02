import json

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
    stitched_template = {}
    baseTemplate = ingestJSON("/Users/mfazza/Code/work_misc/templates/modular_base.json") # remove this hardcoded mess

    put_together(stitched_template, baseTemplate)
    print(stitched_template)



def put_together(current_state, current_base):
    
    if current_state == {}:
        current_state["Project"] = "Project_Name" # remove this hardcoded one, please?
    
    if "Folders" not in current_base:
        return

    if "Folders" not in current_state:
        current_state["Folders"] = []
        
        for folder_index in range(0, len(current_base["Folders"])):
            folder_object = {"name": current_base["Folders"][folder_index]}
            current_state["Folders"].append(folder_object)

            put_together(current_state["Folders"][folder_index], current_base["Model"])

    


stitcher()

