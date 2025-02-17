# Login/Signup here to generate agno keys
https://app.agno.com/login?callbackUrl=%2F

# Login/Signup here to generate OpenAI keys
https://openai.com/


# Create Virtual Environment
python -m venv venv

# Activate Virtual Environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set Keys in local environment
set OPENAI_API_KEY="Your OpenAI Key"
set AGNO_API_KEY="Your Agno Key"

# Run application
python team.py

# Deactivate Virtual Environment
deactivate
