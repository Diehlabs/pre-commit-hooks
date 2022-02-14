import yaml
from lastversion import has_update

with open('../requirements.yml', 'r') as file:
    ans_req = yaml.safe_load(file)

for role in ans_req['roles']:
    if 'name' in role:
        role_name = role['name']
        repo_url = role['src'].replace('.git', '')
        role_version = role['version']
        latest_version = has_update(repo=repo_url, current_version=role_version)
        if latest_version:
            print('Role {0} at {1} is version {2}'.format(role_name, repo_url, role_version))
            print('Has new version: {0}'.format(latest_version))
