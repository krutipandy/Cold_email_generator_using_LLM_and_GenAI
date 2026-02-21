from flask import Flask, render_template, request, jsonify
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

app = Flask(__name__)

# Initialize chain and portfolio
chain = Chain()
portfolio = Portfolio()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_email():
    try:
        data = request.get_json()
        url_input = data.get('url', '')
        
        if not url_input:
            return jsonify({'error': 'URL is required'}), 400
        
        # Load and process the webpage
        loader = WebBaseLoader([url_input])
        page_data = clean_text(loader.load().pop().page_content)
        
        # Load portfolio
        portfolio.load_portfolio()
        
        # Extract jobs and generate emails
        jobs = chain.extract_jobs(page_data)
        emails = []
        
        for job in jobs:
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            email = chain.write_mail(job, links)
            emails.append({
                'job': job,
                'email': email
            })
        
        return jsonify({'success': True, 'emails': emails})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)