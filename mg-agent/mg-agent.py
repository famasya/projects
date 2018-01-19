import yaml
import sys
import requests
from datetime import datetime

def main(argv):
    # read YAML file
    with open("mg-agent.yaml","r") as stream:
        try:
            config = yaml.load(stream)
            LoadLogs(config)
            SendData(config)
        except yaml.YAMLError as exc:
            print(exc)

def LoadLogs(config):
    # define variables
    notice_path = config["path"]+"/notice.log"
    temp_path = config["temp"]
    startline = config["startline"]
    stopline = 0

    temp = open(temp_path,"w")
    '''
    Read notice.log, read if lines > startline to write into temp.log. Close resource
    '''
    with open(notice_path) as f:
        try:
            for i, l in enumerate(f):
                if(i<startline or i<8):
                    pass
                else:
                    temp.write(l)
        except IOError:
            print sys.exit("File not found")
        stopline = i
    temp.close()

    # update last line to mg-agent.yaml and its timestamp
    with open("mg-agent.yaml","w") as stream:
        config["startline"] = stopline
        config["lastrun"] = datetime.now()
        yaml.dump(config,stream,default_flow_style=False)

def SendData(config):
    open_temp = open(config["temp"],"rb")
    post = requests.post(config["pooler"], files={"notice":open_temp})
    print post.text

if __name__ == "__main__":
    main(sys.argv[1:])
