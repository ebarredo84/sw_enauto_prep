#--------------------IOS XE MENUS NIVEL 1-----------------------------
IOSXE_L1_MENU="""Estás usando IOS XE SANDBOX ALWAYS ON
1) SANDBOX IOS XE 1    (host="ios-xe-mgmt.cisco.com")
¿Que opción deseas usar?"""

#--------------------IOS XE MENUS NIVEL 2-----------------------------
IOSXE_L2_MENU="""Estás usando IOS XE SANDBOX ALWAYS ON
    1)  NETCONF
    2)  RESTCONF
    ¿Que opción deseas usar?"""

#--------------------IOS XE MENUS NIVEL 3-----------------------------
IOSXE_NETCONF_MENU="""Estás usando IOS XE SANDBOX ALWAYS ON
    2)  GET YANG MODEL INTERFACE        (get_config interfaces)
    3)  GET INTERFACE LIST              (get_config interfaces)
    4)  ADD NEW INTERFACE               (edit_config operation="create" interfaces Loopback99)
    5)  MERGE DESCRIPTION               (edit_config operation="merge" interfaces Loopback99)
    6)  EDIT IP AND MASK                (edit_config operation="replace" interfaces Loopback99: edit ip address)
    7)  DELETE INTERFACE                (edit_config operation="delete" interfaces Loopback99)
    ¿Que opción deseas usar?"""

IOSXE_RESTCONF_MENU="""Estás usando IOS XE SANDBOX ALWAYS ON
    1)  GET HEADER AUTHENTICATION       (CREATE HEADER)
    2)  GET YANG MODEL INTERFACE        (GET /EN PRUEBAS!!)
    3)  GET INTERFACE LIST              (GET /ietf-interfaces:interfaces)
    4)  ADD NEW INTERFACE               (POS /ietf-interfaces:interfaces Loopback99)
    5)  MERGE DESCRIPTION               (PATCH /ietf-interfaces:interfaces/interface=Loopback99: merge description)
    6)  EDIT INTERFACE                  (PUT /ietf-interfaces:interfaces/interface=Loopback99: edit ip address)
    7)  DELETE INTERFACE                (DEL /ietf-interfaces:interfaces/interface=Loopback99)
    ¿Que opción deseas usar?"""