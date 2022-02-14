from __future__ import annotations

import yaml
from lastversion import has_update

def main():
    with open('requirements.yml', 'r') as file:
        ans_req = yaml.safe_load(file)

    retval = {}

    for role in ans_req['roles']:
        if 'name' in role:
            role_name = role['name']
            repo_url = role['src'].replace('.git', '')
            role_version = role['version']
            latest_version = has_update(repo=repo_url, current_version=role_version)
            if latest_version:
                retval[role_name] = {
                    'current_version': role_version,
                    'latest_version' : latest_version
                }

    return retval

if __name__ == '__main__':
    result = main()
    if result:
        print(result)
    else:
        print("All roles are using the latest version.")
