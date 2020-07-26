# Installation before running the program
1. Python 3.7
2. [Flask](https://palletsprojects.com/p/flask/)
3. [Tensorflow for GPT-2](https://github.com/minimaxir/gpt-2-simple)
You have to run it on a local environment.

# GPT-2
We used a pretrained model developed by Max Woolf in a [google colab](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=H7LoMj4GA4n_). 
We trained this model with 50+ recipes taken from Epicurious and other recipe sites. 

# Adjust the temperature
The value of the temperature determines how "crazy" the sentences are. The higher the temperature, the crazier the recipes get. Usually temperature is between 0.7 and 1.0 (we used
0.7 for our project). We experimented with a very high temperature, 10 to be exact, and the results are fun to read. 

# Useful resources
1. [GPT-2 Text Generating model](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=H7LoMj4GA4n_)
2. [Woolf's personal blog to explain how to use GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
3. [Flask Web App](https://www.kdnuggets.com/2018/05/complete-guide-convnet-tensorflow-flask-restful-python-api.html/2)
4. [Transformers](http://www.peterbloem.nl/blog/transformers)
