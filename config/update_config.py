#!/usr/bin/python

"""
update_config.py:

    This module converts the user-editable set_config text file
    into a python module file. This allows the user to edit
    the configuration with easily understandable values such
    as "ON" or "OFF", but yet SET operates with a module from
    which variables can be imported and boolean values operated
    upon.
"""
import os
from src.core.setcore import print_status, print_info, print_error, return_continue
import datetime
from time import sleep

definepath = os.getcwd()

# TODO
# * integers should not have quotes
# * paths should be double-quoted
# * Booleans should not be quoted

def value_type(value):
    
    """ Determines whether the setting parameter should be quoted. """
    
    return {
            'METASPLOIT_PATH':True,
            'METASPLOIT_DATABASE':True,
            'ENCOUNT':False,
            'AUTO_MIGRATE':False,
            'CUSTOM_EXE':True,
            'BACKDOOR_EXECUTION':False,
            'METERPRETER_MULTI_SCRIPT':False,
            'LINUX_METERPRETER_MULTI_SCRIPT':False,
            'METERPRETER_MULTI_COMMANDS':True,
            'LINUX_METERPRETER_MULTI_COMMANDS':True,
            'METASPLOIT_IFRAME_PORT':False,
            'ETTERCAP':False,
            'ETTERCAP_PATH':True,
            'ETTERCAP_DSNIFF_INTERFACE':True,
            'DSNIFF':False,
            'AUTO_DETECT':False,
            'SENDMAIL':False,
            'EMAIL_PROVIDER':True,
            'WEBATTACK_EMAIL':False,
            'MLITM_PORT':False,
            'APACHE_SERVER':False,
            'APACHE_DIRECTORY':True,
            'WEB_PORT':False,
            'SELF_SIGNED_APPLET':False,
            'JAVA_ID_PARAM':True,
            'JAVA_REPEATER':False,
            'JAVA_TIME':True,
            'WEBATTACK_SSL':False,
            'SELF_SIGNED_CERT':False,
            'PEM_CLIENT':True,
            'PEM_SERVER':True,
            'WEBJACKING_TIME':False,
            'COMMAND_CENTER_INTERFACE':True,
            'COMMAND_CENTER_PORT':False,
            'SET_INTERACTIVE_SHELL':False,
            'TERMINAL':True,
            'DIGITAL_SIGNATURE_STEAL':False,
            'UPX_ENCODE':False,
            'UPX_PATH':True,
            'AUTO_REDIRECT':False,
            'HARVESTER_REDIRECT':False,
            'HARVESTER_URL':True,
            'UNC_EMBED':False,
            'ACCESS_POINT_SSID':True,
            'AIRBASE_NG_PATH':True,
            'DNSSPOOF_PATH':True,
            'AP_CHANNEL':False,
            'POWERSHELL_INJECTION':False,
            'POWERSHELL_VERBOSE':False,
            'WEB_PROFILER':False,
            'OSX_REVERSE_PORT':False,
            'LINUX_REVERSE_PORT':False,
            'USER_AGENT_STRING':True,
            'SET_SHELL_STAGER':False,
            'AUTOMATIC_LISTENER':False,
            'METASPLOIT_MODE':False
           }.get(value,"ERROR")

def update_config():
    
    init_file = file("%s/config/set_config" % (definepath), "r")
    new_config = file("%s/config/set_config.py" % (definepath), "w")
    timestamp = str(datetime.datetime.now())
    
    new_config.write("""#!/usr/bin/python\n
#######################################################################
##                    DO NOT MODIFY THIS FILE                        ##
#######################################################################
#  This file is generated by a routine inside SET, for use by SET.    #
#                                                                     # 
#  Settings should be modified in the set_config file, and then       #
#  SET updated using the 'Update SET Configuration' menu item in      #
#  the main menu. This file will be updated with the new settings.    #
#                                                                     #
#  set_config.py generated: """ + timestamp + """                #
#                                                                     #
#######################################################################
CONFIG_DATE='"""+timestamp+"""'\n""")
    for line in init_file:
        if not line.startswith("#"):
            line = line.rstrip()
            line = line.split("=")
            setting = line[0]
            value = line[1]
            if value == "ON":
                value = "True"
            elif value == "OFF":
                value = "False"
            else:
                pass
            
            quoted = value_type(setting)
            
            if quoted:
                new_config.write(setting + '="' + value + '"\n')
            else:
                new_config.write(setting + '=' + value + '\n')

    init_file.close()
    new_config.close()
    sleep(1)
    from set_config import CONFIG_DATE as verify
    print_info("New set_config.py file generated on: %s" % timestamp)
    print_info("Verifying configuration update...")
    if verify == timestamp:
        print_status("Update verified, config timestamp is: %s" % timestamp)
    else:
        print_error("Update failed? Timestamp on config file is: %s" % verify)
    print_status("SET is using the new config, no need to restart")
    return_continue()

if __name__ == "__main__":
    update_config()

