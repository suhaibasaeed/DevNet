from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_string
from nornir.core.filter import F
import logging
from sys import argv

def config_intfs_ospf(task):
    """
    > The function config_intfs_ospf() takes a task object as an argument, and then uses the
    template_string task to generate a configuration string, which is then used by the napalm_configure
    task to configure the device
    
    :param task: the task object that is passed to the function
    """
    
    TEMPLATE_STR = """
    interface GigabitEthernet2
    ip address {{ gi2ip }} 255.255.255.0
    no shutdown
    ip ospf 1 area 0"""

    result = task.run(task=template_string, template=TEMPLATE_STR, gi2ip=task.host["gi2ip"], severity_level=logging.DEBUG)

    task.host["config"] = result.result

    ospf_result = task.run(task=napalm_configure, configuration=task.host["config"])


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")

    nr = nr.filter(F(groups__contains=f"{argv[1]}"))

    results = nr.run(task=config_intfs_ospf)

    print_result(results)

