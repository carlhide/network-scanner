from HostRange import HostRange as Range
import os
import Context as Context


def main():
    #start_ip = input("Enter first IP in range: ")
    #stop_ip = input("Enter last IP in range: ")
    #select_show_dead = input("Show dead hosts? (y/n): ")
    #show_dead = False

    start_ip = "10.5.2.1"
    stop_ip = "10.5.2.200"
    select_show_dead = "y"
    show_dead = False

    Context.load_vendor_xml("./lists/vendorMacs.xml")

    if select_show_dead == "y":
        show_dead = True
    elif select_show_dead == "n":
        show_dead = False
    else:
        print("Invalid input")

    hosts = Range(start_ip, stop_ip)
    hosts.ping_hosts()

    for i in hosts.get_hosts():
        if i.is_alive() or (not i.is_alive() and show_dead):
            print(i.to_string())

    print("Task finished")


if __name__ == '__main__':
    curr_dir = os.path.dirname(os.path.realpath(__file__))  # get's the path of the script
    os.chdir(curr_dir)  # changes the current path to the path of the script
    main()
