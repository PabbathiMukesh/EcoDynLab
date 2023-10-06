# database_router.py

class CopyDataRouter:
    def db_for_read(self, model, **hints):
        # Use the 'default' database for reading (source database).
        return 'default'

    def db_for_write(self, model, **hints):
        # Use the 'new' database for writing (destination database).
        return 'new'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the 'new' database.
        if obj1._state.db == 'new' and obj2._state.db == 'new':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow all models to be migrated to the 'new' database.
        if db == 'new':
            return True
        return None
