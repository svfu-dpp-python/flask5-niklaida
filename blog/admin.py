from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import db, Post, Comment

# session = models.db.session

admin = Admin()
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
