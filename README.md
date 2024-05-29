AdMob Request Verification using Python

===========================================================

This Python script is designed to verify the authenticity of AdMob requests by checking the signature against the provided data and public key.
Get Public Key

The get_public_key() function retrieves the public key from the AdMob server for verifying the authenticity of AdMob requests.
Verify AdMob Request

The verify_admob_request() function verifies the authenticity of an AdMob request by checking the signature against the provided data and public key.
Usage

To use this script, you need to provide the following parameters:

    data_to_verify: The data to be verified.
    key_id: The ID of the public key used for verification.
    signature: The base64-encoded signature to be verified.

Here is an example usage:

data_to_verify = "ad_network=5450213213286189855&ad_unit=1234567890&reward_amount=1&reward_item=Token&timestamp=1716976735073&transaction_id=123456789&user_id=123321"
signature = "MEUCICz4mA1ozoCCbCORMk8XAXqx8PXA3vqiujxuHKGYFVueAiEA1WG74G2tHXau1Wsdk14SeNvF0M4LpqWYvesWmLUurIY"
key_id = "3335741209"

print(verify_admob_request(data_to_verify, key_id, signature))

This will verify the signature and print True if the signature is valid, or False otherwise.
Note

This script uses the ECDSA algorithm for verification. If the signature is invalid, it will raise a BadSignatureError.
License

This script is licensed under the MIT License.
