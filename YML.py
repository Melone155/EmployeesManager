import os
import yaml

def CreateConfigs(Status, Host, Username, Password, Database):

    # Path to the YAML files
    MySQL = 'Config/MySQL.yaml'
    Employees = 'Config/Employees.yaml'
    User = 'Config/User.yaml'

    MySQLdata = {
        "MySQL": [
            {'Status' : Status, 'Host': Host, 'User': Username, 'Password': Password, "Database": Database}
        ]
    }

    Employeesdata = {
        "Employees": [
            #{'Name': 'Max Mustermann', 'Alter': 30, 'Position': 'Manager'}
        ]
    }

    Userdata = {
        "User": [
            {'Admin': 'admin'}
        ]
    }

    with open(MySQL, 'w') as MySQLfile:
        yaml.dump(MySQLdata, MySQLfile)

    with open(Employees, 'w') as Employeesfile:
        yaml.dump(Employeesdata, Employeesfile)

    with open(User, 'w') as Userfile:
        yaml.dump(Userdata, Userfile)

