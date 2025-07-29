# AI Companion for Seniors - Survey Application

This is a Flask web application that collects survey responses about AI companions for seniors and stores them in a SQLite database.

## Features

- Interactive web form for collecting survey responses
- SQLite database storage
- Modern, responsive UI design
- Form validation and error handling

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the survey:**
   Open your web browser and go to: `http://localhost:5000`

## Database

The application automatically creates a SQLite database file (`survey.db`) with the following table structure:

- `id` - Primary key
- `age_group` - Age group selection
- `uses_digital_assistant` - Whether they use digital assistants
- `difficulty_using_tech` - Difficulty level with technology
- `interest_in_ai` - Interest level in AI companions
- `helpful_features` - Features they find helpful
- `comfort_with_ai_voice` - Comfort level with AI voice
- `concerns` - Concerns about AI companions
- `trial_participation` - Interest in trial participation
- `willingness_to_pay` - Willingness to pay for service
- `additional_comments` - Additional comments

## File Structure

```
ElderCare/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── survey.html     # Survey form template
├── ElderCarepdf.py     # PDF form generator (existing)
└── survey.db          # SQLite database (created automatically)
```

## API Endpoints

- `GET /` - Serves the survey form
- `POST /submit` - Submits survey data to database

## Development

The application runs in debug mode by default. To run in production, set `debug=False` in `app.py`. 