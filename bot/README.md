# GenAI Chatbot

A Streamlit-based chatbot application powered by Groq's AI API.

## Features

- Interactive chat interface using Streamlit
- Powered by Groq's Llama 3.3 70B model
- Maintains chat history during the session
- Clean and user-friendly UI

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Manjunathnithin/GenAi-chat-bot-.git
cd GenAi-chat-bot-
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install groq streamlit python-dotenv
```

4. Create a `.env` file and add your Groq API key:
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

## Usage

Run the Streamlit app:
```bash
streamlit run agent.py
```

The app will open in your default browser at `http://localhost:8501`.

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key (get it from [console.groq.com](https://console.groq.com))

## License

MIT
