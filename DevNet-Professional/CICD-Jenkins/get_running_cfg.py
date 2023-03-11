from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file

nr = InitNornir(config_file="config.yaml")

def get_running(task):
    
    r = task.run(task=napalm_get, getters=["config"], retrieve="running")
    
    task.host["running_config"] = r.result['config']['running']
    
    task.run(task=write_file, content=task.host["running_config"], filename=f"configs/{task.host}.cfg")


results = nr.run(task=get_running)
print_result(results)

