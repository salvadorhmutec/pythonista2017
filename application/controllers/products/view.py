import config
import app


class View:
    def __init__(self):
        pass

    def GET(self, id_product):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_VIEW(id_product)
            elif privilege == 1:
                return self.GET_VIEW(id_product)
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(id_product):
        id_product = config.check_secure_val(str(id_product))
        result = config.model.get_products(id_product)
        return config.render.view(result)
    