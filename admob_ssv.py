import requests
import json
import base64
import hashlib

def get_public_key():
    """
    Retrieves the public key from the AdMob server for verifying the authenticity of AdMob requests.

    Returns:
        dict: A dictionary containing the public keys, where the key is the key ID and the value is the corresponding PEM-encoded public key.

    Raises:
        requests.exceptions.HTTPError: If the request to the AdMob server fails.
    """
    url = "https://www.gstatic.com/admob/reward/verifier-keys.json"
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()
    return {str(key["keyId"]): key["pem"] for key in json_data["keys"]}

def verify_admob_request(data_to_verify, key_id, signature):
    """
    Verifies the authenticity of an AdMob request by checking the signature against the provided data and public key.

    Args:
        data_to_verify (str): The data to be verified.
        key_id (str): The ID of the public key used for verification.
        signature (str): The base64-encoded signature to be verified.

    Returns:
        bool: True if the signature is valid, False otherwise.

    Raises:
        BadSignatureError: If the signature is invalid.

    Note:
        This function uses the ECDSA algorithm for verification.

    """
    public_key = get_public_key().get(key_id, None)
    print(public_key)

    content = data_to_verify.encode('utf-8')

    signature = base64.b64decode(signature+"===")

    from ecdsa import BadSignatureError, VerifyingKey
    from ecdsa.util import sigdecode_der

    verifying_key = VerifyingKey.from_pem(public_key)

    try:
        return verifying_key.verify(
            signature,
            content,
            hashfunc=hashlib.sha256,
            sigdecode=sigdecode_der,
        )
    except BadSignatureError:
        return False
