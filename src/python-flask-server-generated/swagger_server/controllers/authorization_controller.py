from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_5gmeta_oauth2(token):
    return {'scopes': ['read:pets', 'write:pets'], 'uid': 'test_value'}

def validate_scope_5gmeta_oauth2(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))

def check_api_key(api_key, required_scopes):
    return {'test_key': 'test_value'}


