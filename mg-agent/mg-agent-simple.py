import yaml
import sys
import requests
from datetime import datetime

def main(argv):
    # read YAML file
    with open("mg-agent.yaml","r") as stream:
        try:
            config = yaml.load(stream)
            SendData(config)
        except yaml.YAMLError as exc:
            print(exc)

def SendData(config):
    path = config["path"]+"/notice.log"
    open_temp = open(path,"rb")
    post = requests.post(config["pooler"], files={"notice":open_temp})

    # update last line to mg-agent.yaml and its timestamp
    with open("mg-agent.yaml","w") as stream:
        config["lastrun"] = datetime.now()
        yaml.dump(config,stream,default_flow_style=False)

    print post.text

if __name__ == "__main__":
    main(sys.argv[1:])
