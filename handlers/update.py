from handlers import procs
from utils import Header

def run():
    print(Header("UPDATE INSTANCE"))
    procs.index_instances_by_update()
    
    class Params:
        
        def __init__(self):
            self.instance_id = procs.enter_instance_id()
            self.instance = procs.get_instance_name(self.instance_id)
            self.url = (f"{self.instance}.p3l.app")
            self.database = (f"{self.instance}_p3l_app")
            self.server_ip = procs
            self.server_ip = procs.get_server_ip_by_instance(self.instance_id)
            self.server_name = procs.get_server_name_by_instance(self.instance_id)
            self.git_branch = procs.get_git_branch_by_instance_id(self.instance_id)
    
    params = Params()
    procs.updatemenu(params)


