###  Provider
provider "vsphere" {
  user                 = "${var.vsphere_username}"
  password             = "${var.vsphere_password}"
  vsphere_server       = "${var.vsphere_server}"
  allow_unverified_ssl = true
}

###  Data Sources
data "vsphere_datastore" "datastore" {
  name          = "datastore"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "network" {
  name          = "VM Network"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "vm_network_1" {
  name          = "vm_network_1"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_2" {
  name          = "vm_network_2"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_3" {
  name          = "vm_network_3"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_4" {
  name          = "vm_network_4"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_5" {
  name          = "vm_network_5"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_6" {
  name          = "vm_network_6"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_7" {
  name          = "vm_network_7"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_network" "vm_network_0" {
  name          = "vm_network_0"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"

  depends_on = [
    vsphere_host_port_group.pg
  ]
}

data "vsphere_datacenter" "dc" { }

data "vsphere_resource_pool" "pool" { }
