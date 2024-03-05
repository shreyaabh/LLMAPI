from flask import Flask, request, jsonify
from article_func import article_generator 

app = Flask(_name_)

@app.route('/generate_article', methods=['POST', 'GET'])
def generate_article():
    if request.method == 'POST':

        topic = request.form.get('topic') or request.json.get('topic')
        key_word = request.form.get('key_word') or request.json.get('key_word')
        language = request.form.get('language') or request.json.get('language')
        article = article_generator(topic, key_word, language)
        return jsonify({'article': article})
    
    elif request.method == 'GET':
        topic = request.args.get('topic')
        key_word = request.args.get('key_word')
        language = request.args.get('language')
        article = article_generator(topic, key_word, language)
        return jsonify({'article': article})
        
    

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)
