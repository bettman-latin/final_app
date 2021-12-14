from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from app.auth import login_required # the decorator to ensure login
from app.db import get_db

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
    query = """SELECT post.id, title, body, created, author_id, username, first, last
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
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            # title and body come from form, author_id comes from user which was done on request already in auth
            # could also get session.get(user_id) but that's not guaranteed to exist
            query = "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)"
            db.execute(query, (title, body, g.user["id"]))
            db.commit()
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

@bp.route("/<int:id>")
def view(id):
    post = get_my_post(id)
    return render_template("blog/view.html", post=post);
    # return id

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



