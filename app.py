from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
"https://github.com/Pankajsingh63/Jenkins-Docker/blob/main/Devops.png"
"https://github.com/Pankajsingh63/Jenkins-Docker/blob/main/Tomcat.png",
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
