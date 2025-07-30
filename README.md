# ElderCare Survey

A multilingual survey application designed to gather insights from seniors about their interest in digital assistant technology.

## 🌟 Features

- **Multilingual Support**: English, French, and Arabic
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Form Persistence**: Saves progress as you type
- **Star Rating System**: Visual star ratings for interest levels
- **Database Storage**: SQLite database for responses
- **Waiting List**: Tracks interested participants
- **Statistics Dashboard**: View survey results and demographics

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eldercaresurvey.git
   cd eldercaresurvey
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the survey**
   - Survey: http://localhost:5001
   - Waiting List: http://localhost:5001/waiting-list

## 📊 Survey Questions

1. **Contact Information** - Name, email, phone, preferred contact method
2. **Age Group** - Under 60, 60-70, 70-80, Over 80
3. **Digital Assistant Usage** - Current usage of Siri, Alexa, etc.
4. **Technology Difficulty** - How easy/difficult they find technology
5. **Interest in Digital Assistants** - Interest level with "just talk" option
6. **Helpful Features** - Multiple choice: reminders, conversation, health monitoring, emergency help, entertainment
7. **AI Voice Comfort** - Comfort level with voice assistants
8. **Social Contact** - How often they talk to friends and family
9. **Loneliness When Not Talking** - Feelings when not in contact
10. **Loneliness Frequency** - General loneliness frequency
11. **Willingness to Pay** - Price sensitivity for digital assistant services
12. **Interest Level** - Star rating system (⭐ to ⭐⭐⭐⭐⭐)
13. **Additional Comments** - Open-ended feedback

## 🗄️ Database Schema

### Responses Table
- `id` - Primary key
- `age_group` - Age group selection
- `uses_digital_assistant` - Current usage
- `difficulty_using_tech` - Technology difficulty level
- `interest_in_ai` - Interest in digital assistants
- `helpful_features` - Selected helpful features
- `comfort_with_ai_voice` - Comfort with voice assistants
- `concerns` - Any concerns (currently unused)
- `willingness_to_pay` - Price sensitivity
- `interest_level` - Star rating (1-5)
- `additional_comments` - Open feedback
- `contact_name` - Participant name
- `contact_email` - Email address
- `contact_phone` - Phone number
- `contact_preference` - Preferred contact method
- `social_contact` - Social contact frequency
- `lonely_feel` - Loneliness when not talking
- `lonely_frequency` - General loneliness frequency

### Waiting List Table
- `id` - Primary key
- `name` - Participant name
- `age_group` - Age group
- `wants_help_with` - Selected helpful features
- `interest_level` - Interest level (3-5 stars)
- `contact_email` - Email address
- `contact_phone` - Phone number
- `contact_preference` - Preferred contact method
- `added_date` - Timestamp

## 🌐 Deployment Options

### Render (Recommended)
1. Fork this repository
2. Create account on [Render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `python app.py`
7. Deploy!

### Railway
1. Fork this repository
2. Create account on [Railway.app](https://railway.app)
3. Connect your GitHub repository
4. Deploy automatically

### Heroku
1. Fork this repository
2. Create account on [Heroku.com](https://heroku.com)
3. Connect your GitHub repository
4. Deploy using the Procfile

## 📈 Statistics Dashboard

The waiting list page shows:
- Total survey participants
- Age group distribution
- Interest level statistics
- List of interested participants

## 🔧 Configuration

### Environment Variables
- `PORT` - Server port (default: 5001)
- `FLASK_ENV` - Development/production mode

### Database
The application automatically creates `survey.db` on first run.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ for senior care technology research** 