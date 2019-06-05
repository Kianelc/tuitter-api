from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializa o banco e o marshmallow
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

USER = {
    "name": "Kiane L. Casagreande",
    "username": "@kianelc",
    "address": "Florianópolis/SC",
    "profession": "Desenvolvedora Front-End",
    "url": "http://localhost/"
}

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140))

    def __init__(self, description):
        self.description = description


class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description')


comment_schema = CommentSchema(strict=True)
comments_schema = CommentSchema(many=True, strict=True)


@app.route('/comment', methods=['POST'])
def add_comment():
    description = request.json['description']

    new_comment = Comment(description)

    db.session.add(new_comment)
    db.session.commit()

    return comment_schema.jsonify(new_comment)


@app.route('/comments', methods=['GET'])
def get_comments():
    all_comments = Comment.query.all()
    result = comments_schema.dump(all_comments)
    return jsonify(result.data)

@app.route('/comment/<id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return comment_schema.jsonify(comment)

if __name__ == "__main__":
    manager.run()