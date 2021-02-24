#------MODEL--------------------------
import requests
from enauto_rest_functions_ebo import *

#------USER INTERFACE (VIEW)----------
import tkinter as tk
from enauto_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64
from enauto_functions_interface_ebo import *

#-------------IOS NETCONF OPTIONS-----------
def IOSXE_NETCONF_GET_YANG_INTERFACES(ans1,text_box):
    netconf_reply=GET_SCHEMA_IOS_NETCONF(ans1,identifier="ietf-interfaces")
    #BORRO LO QUE ESTÁ EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
#    text_box.config(state="disabled")               #solo lectura
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,netconf_reply['rpc-reply']['data']['#text']+"\n")
    text_box.config(state="disabled")               #solo lectura

    
def IOSXE_NETCONF_GET_INTERFACES(ans1,text_box):
    source="running"
    netconf_filter="""
<filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface></interface>
   </interfaces>
 </filter>"""
    netconf_reply=GET_IOS_NETCONF(ans1,source,netconf_filter)
    #BORRO LO QUE ESTÁ EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
#    text_box.config(state="disabled")               #solo lectura
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE(netconf_reply['rpc-reply']['data']['interfaces'],text_box)

def IOSXE_NETCONF_ADD_INTERFACES(ans1,text_box):
    target="running"

    name="Loopback99"
    if_type="ianaift:softwareLoopback"

    status="true"
    ip_address="192.168.10.2"
    mask="255.255.255.0"

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<enabled>{status}</enabled>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
        			<netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type = if_type,
        status = status,
        ip_address = ip_address,
        mask = mask
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_MERGE_DESCRIPTION(ans1,text_box):
    target="running"

    name="Loopback99"
    if_type="ianaift:softwareLoopback"

    desc="Testin NETCONF EBO"

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="merge">
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<description>{desc}</description>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type=if_type,
        desc=desc
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_EDIT_INTERFACES(ans1,text_box):
    target="running"

    name="Loopback99"

    desc="Testin NETCONF EBO (change IP ADDRESS)"
    if_type="ianaift:softwareLoopback"
    ip_address="192.168.10.99"
    mask="255.255.255.0"

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="replace">
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<description>{desc}</description>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type=if_type,
        desc=desc,
        ip_address = ip_address,
        mask = mask
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_DEL_INTERFACES(ans1,text_box):
    target="running"

    name="Loopback99"

    netconf_interface_template = """
 <config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface operation="delete">
             <name>{name}</name>
         </interface>
     </interfaces>
 </config>"""        
    netconf_data = netconf_interface_template.format(
        name = name)
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

#-------------IOS RESTCONF OPTIONS-----------
def IOSXE_RESTCONF_GET_HEADERS(ans1,text_box):
    headers=SANDBOX_AUTHENTICATION(ans1,text_box)
    return headers

def IOSXE_RESTCONF_GET_YANG_INTERFACES(ans1,headers,text_box):
    services="netconf-state/capabilities"
    response=GET_FUNCTION_EBO(ans1,services,headers,text_box)
    PRINT_RESPONSE_JSON(response,text_box)

def IOSXE_RESTCONF_GET_INTERFACES(ans1,headers,text_box):
    services="ietf-interfaces:interfaces"
    response=GET_FUNCTION_EBO(ans1,services,headers,text_box)
    PRINT_RESPONSE_JSON(response,text_box)

def IOSXE_RESTCONF_ADD_INTERFACES(ans1,headers,text_box):
    services="ietf-interfaces:interfaces"
    data = {
        "ietf-interfaces:interface": {
            "name": "Loopback99",
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": "192.168.10.2",
                    "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }
    response=POST_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_MERGE_DESCRIPTION(ans1,headers,text_box):
    services="ietf-interfaces:interfaces/interface=Loopback99"
    data = {
        "ietf-interfaces:interface": {
            "name": "Loopback99",
            "description": "Testing RESTCONF EBO",
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
        }
    }
    response=PATCH_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_EDIT_INTERFACES(ans1,headers,text_box):
    services="ietf-interfaces:interfaces/interface=Loopback99"
    data = {
        "ietf-interfaces:interface": {
            "name": "Loopback99",
            "description": "Testing RESTCONF EBO changing IP ADDRESS",
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": "192.168.10.99",
                    "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }
    response=PUT_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_DEL_INTERFACES(ans1,headers,text_box):
    services="ietf-interfaces:interfaces/interface=Loopback99"
    response=DELETE_FUNCTION_EBO(ans1,services,headers,text_box)
    
    PRINT_STATUS_CODE(response,text_box)