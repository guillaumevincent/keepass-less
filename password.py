import hmac
import base64
import hashlib


def make_password(key, salt, length=10):
    signature = hmac.new(key.encode(), salt.encode(), hashlib.sha1).hexdigest()
    password = base64.b64encode(signature.encode()).decode()
    return password[:length]
