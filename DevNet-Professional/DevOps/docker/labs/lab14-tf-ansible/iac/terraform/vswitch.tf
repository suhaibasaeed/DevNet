data "vsphere_host" "esxi_host" {
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

resource "vsphere_host_virtual_switch" "devnet_lab_vswitch" {
  count          = 6
  name           = "devnet_lab_vswitch_${count.index}"
  host_system_id = "${data.vsphere_host.esxi_host.id}"

  network_adapters = []

  active_nics  = []
  standby_nics = []
}

resource "vsphere_host_port_group" "pg" {
  count               = 6
  name                = "vm_network_${count.index}"
  host_system_id      = "${data.vsphere_host.esxi_host.id}"
  virtual_switch_name = "${vsphere_host_virtual_switch.devnet_lab_vswitch[count.index].name}"
}
