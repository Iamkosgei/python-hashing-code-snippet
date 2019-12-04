import bcrypt


def hash_token(token):
    return bcrypt.hashpw(token.encode(), bcrypt.gensalt())


def check_token(plain_token, hashed_token):
    return bcrypt.checkpw(plain_token.encode(), hashed_token)
