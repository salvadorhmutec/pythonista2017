import web
import hmac
import application.models.model_products

render = web.template.render('application/views/products/', base='master')
model = application.models.model_products

secret = "kuorra"


def hash_str(s):
    return hmac.new(secret, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val