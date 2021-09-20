import os
import xml.dom.minidom as xml

_mac_vendor_dict: dict = {}


def __init__():
    curr_dir = os.path.dirname(os.path.realpath(__file__))  # get's the path of the script
    os.chdir(curr_dir)  # changes the current path to the path of the script


def get_mv():
    return _mac_vendor_dict


def load_vendor_xml(xml_file_path: str):
    root = xml.parse(xml_file_path)
    for vendorMapping in root.getElementsByTagName("VendorMapping"):
        m = vendorMapping.getAttribute("mac_prefix")
        v = vendorMapping.getAttribute("vendor_name")
        _mac_vendor_dict[m] = v
    return _mac_vendor_dict
