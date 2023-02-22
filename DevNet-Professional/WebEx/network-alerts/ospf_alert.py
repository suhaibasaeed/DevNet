from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv
import os
from rich import print

# Load environment variables
load_dotenv()

# Create a Webex Teams API access object
api = WebexTeamsAPI(access_token=os.environ["WEBEX_TEAMS_ACCESS_TOKEN"])

nr = InitNornir(config_file="config.yaml")


def ospf_neighbors_test(task):
    device_name = task.host.name

    # Run show ip ospf neighbor on device
    result = task.run(
        task=netmiko_send_command,
        command_string="show ip ospf neighbor",
        use_textfsm=True,
    )

    neigbours_num = len(result.result)

    # Loop through the neigbours and check they're FULL
    if neigbours_num == 2:
        for neighbour in result.result:
            if "FULL" in neighbour["state"]:
                print(
                    f"{device_name} has {neighbour['neighbor_ipaddr']} OSPF neighbour up - [green]PASSED[/green]"
                )
            else:
                print(
                    f"{device_name} has OSPF neighbour {neighbour['neighbor_ipaddr']} down - [red]FAILED[/red]"
                )
                webex_send_failure_message(
                    f"ALERT - {device_name} has OSPF neighbour {neighbour['neighbor_ipaddr']} down"
                )
    else:
        print(f"{device_name} has OSPF neighbours down - [red]FAILED[/red]")
        webex_send_failure_message(
            f"ALERT - {device_name.upper()} has OSPF neighbours failed"
        )


def webex_send_failure_message(message):
    alert_room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vODFjZjIyMDAtYWZjZi0xMWVkLWFjZmUtNTk2NjRkMjcwYzhi"

    api.messages.create(alert_room_id, text=message)


results = nr.run(task=ospf_neighbors_test)
