#! /usr/bin/python
import sys
import yaml
import json


def validator():
    try:
        json_data = yaml.load(open(sys.argv[1]).read(), Loader=yaml.FullLoader)
        json_file = json.dumps(json_data, indent=4)
        print("Is a Valid Yaml")
        answer = input("Do You need to see Json Format of your yaml file?[y/n]: ")
        if answer in ("y", "yes", "Yes"):
            print(json_file)
        else:
            print("Have good Day")

    except yaml.YAMLError as ex:
        print("Not Valid File")
        print(ex)
    except IndexError:
        print("""
        File not found!
        Usage:
        python valid_yaml.py Your_Yaml_file.yaml
        """)


validator()
