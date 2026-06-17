import json
import os

class Parser:
    def __init__(self, filename: str):
        self.filename = filename
        self.file_handle = open(self.filename, "r")

    def readlines(self):
        return [line.strip(" ") for line in self.file_handle.readlines()]
    
    def parse(self):
        file_content = [] # Liste ämit allen JSON-Objekte
        actual_json_object = {} # Aktueller veränderter Python-Dict, das dann in JSON serialized wird


        for line in self.readlines():
            
            if line.startswith("%%E"):
                actual_json_object = {}

            elif line.startswith("%%B"):
                file_content.append(actual_json_object)

            elif line.startswith("::"):
                
                key = line.split("::")[1].replace("::", "").strip(" ")

                print("key = ", key)
                value = line[2:].split("::")[-1].strip(" ").replace("\n", "")
                print("value = ", value)
                probable_list_tokens = value.split(",")


                if value == "True":
                    actual_json_object[key] = True
                elif value == "False":
                    actual_json_object[key] = False
                elif value.isdecimal():
                    actual_json_object[key] = float(value)
                elif value.isdigit():
                    actual_json_object[key] = int(value)
                elif len(probable_list_tokens) == 1:
                    actual_json_object[key] = probable_list_tokens[0]
                elif len(probable_list_tokens) > 1:
                    actual_json_object[key] = probable_list_tokens

            elif not line.isprintable() or not line[:-1].isprintable():
                continue

            else:
                raise SyntaxError(f"Unknown line: {line}")

        json_repr = json.dumps(file_content)
        return json_repr

def write_to_json(output_file: str, content: str):
    file_handle = open(output_file, "a")
    file_handle.write(content)
    file_handle.close()

if __name__ == "__main__":
    files = os.listdir(os.getcwd() + "/hersteller_daten")

    for file in files:
        if file.endswith(".txt"):
            file_handle = open("hersteller_daten/" + file.split(".")[0] + ".json", "a")
            file_handle.write(Parser("hersteller_daten/" + file).parse())
            file_handle.close()
    
