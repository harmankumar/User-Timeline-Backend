class MySQLPlabroRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read testing models go to default.
        """
        if model.name == 'testing':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write testing models go to default.
        """
        if model._meta.app_label == 'testing':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the testing app is involved.
        """
        if obj1._meta.app_label == 'testing' or \
           obj2._meta.app_label == 'testing':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the testing app only appears in the 'default'
        database.
        """
        if app_label == 'testing':
            return db == 'default'
        return None