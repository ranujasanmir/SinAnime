from flask import Flask, render_template
import newslist

app = Flask(__name__)

@app.route('/')
def index():
    post_home = newslist.my_list
    post_list = []
    post_list.extend(post_home)
    return render_template('index.html', news_list=post_list)

@app.route('/posts')
def posts():
    posts = newslist.my_list
    post_liist = []
    post_liist.extend(posts)
    return render_template('posts.html', post=post_liist)

@app.route("/about-us")
def about():
    return render_template('aboutus.html')



if __name__ == '__main__':
    app.run(debug=True)
