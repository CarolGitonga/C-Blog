from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..requests import get_quote
from flask_login import login_required,current_user
from ..models import Blog,User, Comment,Subscriber
from .forms import BlogForm,BioForm, CommentForm
from .. import db,photos
from ..email import mail_message
from urllib.parse import urljoin

def get_abs_url(url):
    """ Returns absolute url by joining post url with base url """
    return urljoin(request.url_root, url)
# Views
@main.route('/')
@login_required
def index():
    quotes = get_quote()
    blogs = Blog.query.all()
    return render_template('index.html',blogs=blogs, quotes=quotes)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user.id
    blog = Blog.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user, blog=blog)

@main.route('/new_blog', methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        title = form.title.data
        new_blog=Blog(blog=blog,title=title,user_id=current_user.id)
        
        new_blog.save_blog()
        
        return redirect(url_for('main.index'))
    
    return render_template('blogs.html', form=form,legend='New Post')
        
@main.route('/comments/<int:blog_id>', methods=['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm
    blogs = Blog.query.get(blog_id)
    comment = Comment.query.filter_by(blog_id=blog_id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comments = form.comment.data
        title = form.title.data
        
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment= Comment(comments=comments,title=title,blog_id=blog_id, user_id=user_id)
        new_comment.save_comment()      
       
        return redirect(url_for('main.new_comment', blog_id=blog_id))
    
    return render_template('comments.html', form=form, comment=comment, blog_id=blog_id,blogs=blogs)

@main.route('/user/<uname>/bio',methods = ['GET','POST'])
@login_required
def update_bio(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    bioform = BioForm()

    if bioform.validate_on_submit():
        user.bio = bioform.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/bio.html',bioform=bioform)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_subscriber():
    subscribers = Subscriber.query.all()
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        blog = Blog(title=title,content=content,user_id=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("New Blog Post","email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        flash('You Posted a new Blog')
    return render_template('newblog.html', form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog.query.get(id)
    return render_template('blogs.html',blog=blog,comments=comments)

@main.route('/blogs/<int:blog_id>/delete', methods = ['POST'])
@login_required
def delete(blog_id):
    quotes = get_quote()
    blogs = Blog.query.all()
    blog = Blog.query.get(blog_id)
    if blog.blogger != current_user:
        abort(403)
    
    Blog.delete(blog)
    
    return redirect(url_for('.index',quotes=quotes,blog=blog,blogs=blogs))

@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.blogger != current_user:
        abort(403)
        
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.blog = form.blog.data
        db.session.commit()
        
        flash("You have updated your Blog!")
        
        return redirect(url_for('main.index',id = blog.id)) 
    
    if request.method == 'GET':
        form.title.data = blog.title
        form.blog.data = blog.blog
        
    return render_template('blogs.html', form = form, legend='Update Post')

@main.route('/comments/<int:comment_id>/delete', methods = ['POST'])
@login_required
def delete_comment(comment_id):
    quotes = get_quote()
    comment = Comment.query.all()
    comment = Comment.query.get(comment_id)
    if comment.feedback != current_user:
        abort(403)
    
    Comment.delete_comment(comment)
    
    return redirect(url_for('.index',quotes=quotes, comment=comment))

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
       
    return render_template('subscribe.html')
   
