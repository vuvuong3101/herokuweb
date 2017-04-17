import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds161400.mlab.com:61400/link_data
host = "ds161400.mlab.com"
port = 61400
db_name = "link_data"
username = "hoangspm"
password = "passion1610"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())