import os
import yaml

def CreateConfigs():

    # Path to the YAML files
    MySQL = 'Config/MySQL.yaml'
    Employees = 'Config/Employees.yaml'
    User = 'Config/User.yaml'

    MySQLdata = {
        "MySQL": [

        ]
    }

    Employeesdata = {
        "Employees": [

        ]
    }

    Userdata = {
        "User": [

        ]
    }

    with open(MySQL, 'w') as MySQLfile:
        yaml.dump(MySQLdata, MySQLfile)

    with open(Employees, 'w') as Employeesfile:
        yaml.dump(Employeesdata, Employeesfile)

    with open(User, 'w') as Userfile:
        yaml.dump(Userdata, Userfile)

