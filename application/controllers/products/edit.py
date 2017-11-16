import config
import app


class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_product, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_EDIT(id_product)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self, id_product, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_EDIT(id_product)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_EDIT(id_product, message=None):
        id_product = config.check_secure_val(str(id_product))
        result = config.model.get_products(int(id_product))
        result.id_product = config.make_secure_val(str(result.id_product))
        return config.render.edit(result, message)

    @staticmethod
    def POST_EDIT(id_product, message=None):
        form = config.web.input()
        form['id_product'] = config.check_secure_val(str(form['id_product']))
        res = config.model.edit_products(
            form['id_product'],
            form['product'],
            form['stock'],
            form['description'],
            form['purchase_price'],
            form['price_sale']
        )
        if res == 0:
            id_product = config.check_secure_val(str(id_product))
            result = config.model.get_products(int(id_product))
            result.id_product = config.make_secure_val(str(result.id_product))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/products')