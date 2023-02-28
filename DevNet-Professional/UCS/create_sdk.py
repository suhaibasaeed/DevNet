from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.ucshandle import UcsHandle

# Login to UCSM
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
handle.login()

# Create a new service profile
sp = LsServer(parent_mo_or_dn="org-root", name="test-server", src_templ_name="sastemplate")

handle.add_mo(sp)
# Commit the changes
handle.commit()