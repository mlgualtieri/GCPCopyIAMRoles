# GCPCopyIAMRoles.py

Copy GCP IAM Roles from one user/group to another
Requires gcloud CLI to be configured for an account with permissions to edit IAM roles.

Author: Mike Gualtieri - https://www.mike-gualtieri.com                                                                                                                                                                          
```
Usage: 
  For display mode eliminate the --to argument:
    python3 GCPCopyIAMRoles.py --from username1@domain.com

  Copy mode:
    python3 GCPCopyIAMRoles.py --from user1@domain.com --to user2@domain.com
```
