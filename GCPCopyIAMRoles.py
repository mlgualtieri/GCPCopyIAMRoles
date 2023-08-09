#!/usr/bin/env python3
#
# Copy GCP IAM Roles from one user/group to another
# Requires gcloud CLI to be configured for an account with permissions
# to edit IAM roles
#
# Author: Mike Gualtieri - https://www.mike-gualtieri.com
#
# Usage: 
#   For display mode eliminate the --to argument:
#     python3 GCPCopyIAMRoles.py --from username1@domain.com
#
#   Copy mode:
#     python3 GCPCopyIAMRoles.py --from user1@domain.com --to user2@domain.com
#

import sys, os, json, subprocess


GCP_PROJECT = ""


if (len(sys.argv) < 2) or (sys.argv[1] != "--from"):
    print("Usage:", sys.argv[0], "--from username1@domain.com --to username2@domain.com")
    exit()


from_username = sys.argv[2]
to_username   = ""


if (len(sys.argv) < 4) or (sys.argv[3] != "--to"):
    print("Warning: --to argument found, display mode only")
else:
    if (len(sys.argv) > 4):
        to_username = sys.argv[4]
    else:
        print("Warning: --to argument found, display mode only")


print("Roles attached to:", from_username)


cmd='gcloud projects get-iam-policy '+ GCP_PROJECT +' --format=json'
#cmd     = 'cat /tmp/test.json'
cmdout  = subprocess.check_output(cmd, shell=True)
jsonout = json.loads(cmdout)


# Display roles
is_group = False
roles = []
for result in jsonout['bindings']:
    if ("user:" + from_username in result['members']) or ("deleted:user:" + from_username in result['members']):
        print(" ",result['role'])
        roles.append(result['role'])
    if ("group:" + from_username in result['members']) or ("deleted:group:" + from_username in result['members']):
        is_group = True
        print(" ",result['role'])
        roles.append(result['role'])




# Copying roles
if to_username != "":
    print("Copying roles to:", to_username)
else:
    exit()

if (is_group == True):
    to_username = "group:"+ to_username
else:
    to_username = "user:"+ to_username


for role in roles:
    print("  Attaching: ",role)
    cmd="gcloud projects add-iam-policy-binding "+ GCP_PROJECT +" --condition=None --member='"+ to_username +"' --role='"+ role +"'"
    print(cmd)
    cmdout  = subprocess.check_output(cmd, shell=True)
    #print(cmdout)


exit()

