# PickMyBrain 🧠

A fun and lightweight email analyzer tool that automatically identifies unsolicited "pick your brain" or "quick call" type emails and sends a humorous auto-reply, directing senders to a playful landing page.

## Features

- 🤖 **Smart Email Analysis**: NLP-based detection of "pick your brain" type emails
- 😄 **Humorous Auto-Reply**: Sends playful responses with fake payment links
- 🎨 **Playful Landing Page**: Humorous page that reveals the joke
- ⚙️ **Customizable**: Modify triggers, responses, and landing page content

## Project Structure

```
PickMyBrain/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── email_analyzer.py # Email processing logic
│   │   ├── nlp_processor.py # NLP analysis
│   │   └── config.py       # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   └── .env.example       # Environment variables template
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/         # Page components
│   │   └── styles/        # CSS styles
│   ├── package.json       # Node.js dependencies
│   └── public/            # Static assets
└── README.md              # This file
```

## Quick Start

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your email credentials
   ```

5. Run the backend:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm start
   ```

## Configuration

### Email Setup

1. **Gmail API** (Recommended):
   - Enable Gmail API in Google Cloud Console
   - Create credentials and download JSON file
   - Set `GMAIL_CREDENTIALS_FILE` in `.env`

2. **IMAP** (Alternative):
   - Set `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USER`, `EMAIL_PASSWORD` in `.env`

### Customization

- **Trigger Phrases**: Edit `backend/app/nlp_processor.py` to modify detection keywords
- **Auto-Reply**: Customize response templates in `backend/app/email_analyzer.py`
- **Landing Page**: Modify content in `frontend/src/pages/LandingPage.js`

## Usage

1. Start both backend and frontend servers
2. The backend will monitor your email inbox
3. When a "pick your brain" email is detected, it sends a humorous auto-reply
4. Recipients click the payment link and land on the playful page

## Development

- **Backend**: FastAPI with async email processing
- **Frontend**: React with modern CSS and animations
- **NLP**: Basic regex patterns with room for ML enhancement
- **Deployment**: Ready for Vercel (frontend) and Heroku/Railway (backend)

## License

Personal use only - not intended for commercial distribution.

---

Built with ❤️ and a sense of humor