import config
import app


class Index:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_INDEX(privilege)
            elif privilege == 1:
                return self.GET_INDEX(privilege)
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INDEX(privilege):
        result = config.model.get_all_products().list()
        for row in result:
            row.id_product = config.make_secure_val(str(row.id_product))
        return config.render.index(result,privilege)