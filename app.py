from flask import Flask, request, jsonify, render_template, session
import sqlite3
import os
from pyngrok import ngrok
from translations import get_translation

app = Flask(__name__)
app.secret_key = 'eldercare_survey_secret_key_2024'

# Initialize database and table
def init_db():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age_group TEXT,
            uses_digital_assistant TEXT,
            difficulty_using_tech TEXT,
            interest_in_ai TEXT,
            helpful_features TEXT,
            comfort_with_ai_voice TEXT,
            concerns TEXT,
            willingness_to_pay TEXT,
            interest_level TEXT,
            additional_comments TEXT,
            contact_name TEXT,
            contact_email TEXT,
            contact_phone TEXT,
            contact_preference TEXT,
            social_contact TEXT,
            lonely_feel TEXT,
            lonely_frequency TEXT
        )
    ''')
    
    # Create waiting list table
    c.execute('''
        CREATE TABLE IF NOT EXISTS waiting_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age_group TEXT,
            wants_help_with TEXT,
            interest_level TEXT,
            contact_email TEXT,
            contact_phone TEXT,
            contact_preference TEXT,
            added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Get language from session or default to English
    lang = session.get('lang', 'en')
    return render_template('survey_multilingual.html', lang=lang, t=lambda key: get_translation(lang, key))

@app.route('/set-language/<lang>')
def set_language(lang):
    """Set the language for the session"""
    if lang in ['en', 'fr', 'ar']:
        session['lang'] = lang
    return jsonify({"status": "success", "language": lang})

@app.route('/waiting-list')
def waiting_list():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    
    # Get all survey responses for statistics
    c.execute('SELECT age_group, interest_level FROM responses')
    all_responses = c.fetchall()
    
    # Get waiting list entries
    c.execute('SELECT * FROM waiting_list ORDER BY added_date DESC')
    people = c.fetchall()
    
    conn.close()
    
    # Calculate statistics
    total_people = len(all_responses)
    
    # Age group counts - handle both string and integer values
    age_60_70 = len([r for r in all_responses if str(r[0]) == '60_70'])
    age_70_80 = len([r for r in all_responses if str(r[0]) == '70_80'])
    age_over_80 = len([r for r in all_responses if str(r[0]) == 'over_80'])
    age_under_60 = len([r for r in all_responses if str(r[0]) == 'under_60'])
    
    # Interest level counts - handle both string and integer values
    interested = len([r for r in all_responses if str(r[1]) in ['3', '4', '5']])  # 3, 4, or 5 are considered "interested"
    not_interested = len([r for r in all_responses if str(r[1]) in ['1', '2']])  # 1 or 2 are "not interested"
    
    stats = {
        'total_people': total_people,
        'age_60_70': age_60_70,
        'age_70_80': age_70_80,
        'age_over_80': age_over_80,
        'age_under_60': age_under_60,
        'interested': interested,
        'not_interested': not_interested
    }
    
    return render_template('waiting_list.html', people=people, stats=stats)

@app.route('/submit', methods=['POST'])
def submit():
    # Form will send data as POST fields
    data = request.form

    age_group = data.get('age_group', '')
    uses_digital_assistant = data.get('digital_assistant_yes', '') or data.get('digital_assistant_no', '')
    difficulty_using_tech = data.get('difficulty_using_tech', '')
    interest_in_ai = data.get('interest_in_ai', '')
    helpful_features = data.get('helpful_features', '')
    comfort_with_ai_voice = data.get('comfort_with_ai_voice', '')
    concerns = data.get('concerns', '')
    willingness_to_pay = data.get('willingness_to_pay', '')
    interest_level = data.get('interest_level', '')
    additional_comments = data.get('additional_comments', '')
    contact_name = data.get('contact_name', '')
    contact_email = data.get('contact_email', '')
    contact_phone = data.get('contact_phone', '')
    contact_preference = data.get('contact_preference', '')
    social_contact = data.get('social_contact', '')
    lonely_feel = data.get('lonely_feel', '')
    lonely_frequency = data.get('lonely_frequency', '')

    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO responses (
            age_group, uses_digital_assistant, difficulty_using_tech,
            interest_in_ai, helpful_features, comfort_with_ai_voice,
            concerns, willingness_to_pay, interest_level,
            additional_comments, contact_name, contact_email, contact_phone, contact_preference,
            social_contact, lonely_feel, lonely_frequency
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        age_group, uses_digital_assistant, difficulty_using_tech,
        interest_in_ai, helpful_features, comfort_with_ai_voice,
        concerns, willingness_to_pay, interest_level,
        additional_comments, contact_name, contact_email, contact_phone, contact_preference,
        social_contact, lonely_feel, lonely_frequency
    ))
    conn.commit()
    conn.close()

    # Add to waiting list if they're interested (interest level 3, 4, or 5) and provided contact info
    if interest_level in ['3', '4', '5'] and (contact_name or contact_email or contact_phone):
        conn = sqlite3.connect('survey.db')
        c = conn.cursor()
        
        # Get the helpful features they selected
        helpful_features_list = data.getlist('helpful_features')
        wants_help_with = ', '.join(helpful_features_list) if helpful_features_list else 'Not specified'
        
        c.execute('''
            INSERT INTO waiting_list (name, age_group, wants_help_with, interest_level, contact_email, contact_phone, contact_preference)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (contact_name, age_group, wants_help_with, interest_level, contact_email, contact_phone, contact_preference))
        conn.commit()
        conn.close()

    return jsonify({"status": "success", "message": "Survey submitted. Thank you!"})

if __name__ == '__main__':
    init_db()
    
    # Get port from environment variable (for cloud platforms)
    port = int(os.environ.get('PORT', 5001))
    
    print('=' * 50)
    print('🚀 ElderCare Survey is starting...')
    print('=' * 50)
    print(f'📱 Local URL: http://localhost:{port}')
    print(f'🌐 Network URL: http://0.0.0.0:{port}')
    print('=' * 50)
    print('✅ Survey is ready!')
    print('📊 View results at: /waiting-list')
    print('=' * 50)
    
    # Use debug=False for production
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode, threaded=True) 