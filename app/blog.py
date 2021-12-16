from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_file, current_app, send_from_directory)

import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

from app.auth import login_required # the decorator to ensure login
from app.db import get_db


#app = Flask(__name__)

# group together related parts of the app
bp = Blueprint("blog", __name__)

# main route to show all posts
@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    query = """SELECT post.id, title, body, created, author_id, username
            FROM post JOIN user ON post.author_id = user.id
            ORDER BY created DESC"""
    posts = db.execute(query).fetchall() # will be a list of all Rows
    return render_template("blog/index.html", posts=posts)


def get_my_post(id):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    db = get_db()
    query = """SELECT post.id, title, body, created, author_id, username, first, last, file
            FROM post JOIN user ON post.author_id = user.id
            WHERE post.id = ?"""
    post = db.execute(query, (id,)).fetchone()
    
    if post is None:
        abort(404, f"Post id {id} doesn't exist.") # Not Found

    # if post["author_id"] != g.user["id"]:
    #     abort(403) # Forbidden

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required # make sure user is logged in first, else redirect
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        file = request.files["file"]

        error = None

        if "file" not in request.files:
            print('no file')
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            print("saved file successfully")

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            # title and body come from form, author_id comes from user which was done on request already in auth
            # could also get session.get(user_id) but that's not guaranteed to exist
            if filename:
                query = "INSERT INTO post (title, body, author_id, file) VALUES (?, ?, ?, ?)"
                db.execute(query, (title, body, g.user["id"], filename))
                db.commit()
            else:
                query = "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)"
                db.execute(query, (title, body, g.user["id"]))
                db.commit()

      #send file name as parameter to downlad
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_my_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            query = "UPDATE post SET title = ?, body = ? WHERE id = ?"
            db.execute(query, (title, body, id))
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)

@bp.route("/<int:id>", methods=("GET","POST"))
def view(id):
    if request.method == "POST":
        # favorite = request.form['favorite']
        db = get_db()
        query = "INSERT INTO collection (f_posts, f_user) VALUES (?, ?) "
        db.execute(query, (id, g.user["id"]))
        db.commit()

    post = get_my_post(id)
    return render_template("blog/view.html", post=post);
    # return id


@bp.route("/uploads/<file>")
def download_file(file):

    return send_from_directory(current_app.config["UPLOAD_FOLDER"], file)


@bp.route("/profile")
def profile():
    db = get_db()
    query = """SELECT post.id, title, body, created, author_id
            FROM post JOIN user ON post.author_id = user.id
            ORDER BY created DESC"""
    posts = db.execute(query).fetchall() # will be a list of all Rows
    return render_template("blog/profile.html", posts=posts)

@bp.route("/favorites")
def favorites():

    db = get_db()
    query = """SELECT post.id, title, body, created, author_id
            FROM collection JOIN post ON collection.f_posts = post.id
            WHERE collection.f_user = ?"""
    posts = db.execute(query, (g.user["id"],)).fetchall() # will be a list of all Rows
    return render_template("blog/index.html", posts=posts)
    return render_template("blog/favorites.html")

@bp.route("/test")
def test():
    return "test"


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    post = get_my_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))



# # Upload API
# @app.route('/uploadfile', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             print('no file')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             print('no filename')
#             return redirect(request.url)
#         else:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             print("saved file successfully")
#       #send file name as parameter to downlad
#             return redirect('/downloadfile/'+ filename)
#     return render_template('upload_file.html')
# # Download API
# @app.route("/downloadfile/<filename>", methods = ['GET'])
# def download_file(filename):
#     return render_template('download.html',value=filename)
# @app.route('/return-files/<filename>')
# def return_files_tut(filename):
#     file_path = UPLOAD_FOLDER + filename
#     return send_file(file_path, as_attachment=True, attachment_filename='')
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')



