#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould
@description: start, revert and shutdown vbox networks. a file with a list of
vm's for the network being used is needed in conjuction with this script

@run instructions: ./vbox_network.py [ args ]
    -t, --type     --> start|stop|revert  --> default = start
    -f, --file     --> name of file           --> default = CCDC
    -s, --snapshot --> snapshot               --> default = BaseSnap

@EXAMPLES for basic network commands

./vbox_network.py            -->    starts CCDC network with defaults
./vbox_network.py -t stop    -->    stops CCDC network
./vbox_network.py -t revert  -->    reverts CCDC network to defaults snap

@NOTES
revert will not work with the vms running
'''

import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type',
                        help="start stop revert",
                        default='start')

    parser.add_argument('-f', '--file',
                        help="file name",
                        default='CCDC')

    parser.add_argument('-s', '--snapshot',
                        help="name of snapshot",
                        default='BaseSnap')

    args = parser.parse_args()

    if(args.type == 'start'):

        start_vm(args.file)

    elif(args.type == 'stop'):

        stop_vm(args.file)

    elif(args.type == 'revert'):

        revert_vm(args.file, args.snapshot)

    else:

        print('Something wemt wrong check your args')


def start_vm(filename):

    print("\n\tStarting the vbox network - " + filename + '\n')

    try:

        with open(filename, 'r') as f:

            for vm in f:

                vm = vm.strip()

                vm_to_start = ["VBoxManage", "startvm", vm]

                try:

                    vm_start_test = subprocess.run(vm_to_start,
                                                   timeout=120,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)

                    if vm_start_test.returncode:
                        print('\tSomething went wrong\n')
                        print('VM ' + vm + ' did not start\n')

                    else:
                        print('VM ' + vm + ' is running\n')

                except Exception as e:
                    print(e)

    except Exception as e:
        print("\t******* Something went wrong with the vbox network - " +
              filename + ' start up \n')
        print(e)


def stop_vm(filename):

    print("\n\tStopping the vbox network - " + filename + '\n')

    try:

        with open(filename, 'r') as f:

            for vm in f:

                vm = vm.strip()

                vm_to_stop = ["VBoxManage", "controlvm", vm, "poweroff"]

                try:

                    vm_stop_test = subprocess.run(vm_to_stop,
                                                  timeout=120,
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)

                    if vm_stop_test.returncode:
                        print('\tSomething went wrong')
                        print('VM ' + vm + ' was not shutdown or not running\n')

                    else:
                        print('VM ' + vm + ' has been Shutdown\n')

                except Exception as e:
                    print(e)

    except Exception as e:
        print("\t******* Something went wrong with the vbox network - " +
              filename + ' shutdown \n')
        print(e)


def revert_vm(filename, snapshot):

    print("\n\tReverting the vbox network - " + filename +
          ' to Snapshot' + snapshot + '\n')

    try:

        with open(filename, 'r') as f:

            for vm in f:

                vm = vm.strip()

                vm_to_revert = ["VBoxManage", "snapshot", vm,
                                'restore', snapshot]

                try:

                    vm_revert_test = subprocess.run(vm_to_revert,
                                                    timeout=120,
                                                    stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE)

                    if vm_revert_test.returncode:
                        print('\tSomething went wrong\n')
                        print('VM ' + vm + ' did not revert to ' +
                              snapshot + '\n')

                    else:
                        print('VM ' + vm + ' has been reverted to ' +
                              snapshot + '\n')

                except Exception as e:
                    print(e)

    except Exception as e:
        print("\t******* Something went wrong with the vbox network - " +
              filename + ' did not revert to ' + snapshot + ' \n')
        print(e)


if __name__ == "__main__":
    main()
