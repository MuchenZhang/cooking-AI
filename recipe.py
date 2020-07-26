from flask import Flask, render_template, request
from setuptools import setup, find_packages
import gpt_2_simple as gpt2


app = Flask(__name__)

@app.route("/", methods=['GET',  'POST'])
def generate_text():
    

    gpt2.download_gpt2()
  
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)

    recipe = gpt2.generate(sess)

    return render_template("index.html", recipe = recipe)
	

@app.route("/home")
def test():
    return render_template("index.html")
if __name__ == "__main__":
	app.run(debug=True)