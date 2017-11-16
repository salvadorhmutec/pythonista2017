import config
import app


class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_product, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_DELETE(id_product)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self, id_product, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_DELETE(id_product)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_DELETE(id_product, message=None):
        id_product = config.check_secure_val(str(id_product))
        result = config.model.get_products(int(id_product))
        result.id_product = config.make_secure_val(str(result.id_product))
        return config.render.delete(result, message)

    @staticmethod
    def POST_DELETE(id_product, message=None):
        form = config.web.input()
        form['id_product'] = config.check_secure_val(str(form['id_product']))
        res = config.model.delete_products(form['id_product'])
        if res is None:
            message = "El registro no se puede borrar"
            id_product = config.check_secure_val(str(id_product))
            result = config.model.get_products(int(id_product))
            result.id_product = config.make_secure_val(str(result.id_product))
            return config.render.delete(result, message)
        else:
            raise config.web.seeother('/products')

