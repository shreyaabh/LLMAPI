from flask import Flask, request, jsonify
from article_func import article_generator # Ensure this is correctly imported

app = Flask(__name__)

@app.route('/generate_article', methods=['POST'])
def generate_article():
    if request.method == 'POST':
        
        # Extracting topic, key_word, and language from the request data
        topic = request.form.get('topic')
        key_word = request.form.get('key_word')
        language = request.form.get('language')
        
        article = article_generator(topic, key_word, language)
        return jsonify({'article': article})

if __name__ == '__main__':
    app.run(debug=True)
