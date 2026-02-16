# Flask API for Workflow Builder

This Flask API provides LLM-powered text processing capabilities for the Workflow Builder application.

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your Gemini API key.

3. **Run the server:**
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- **GET** `/health`
- Returns the health status of the API and LLM connection

### Process Individual Steps
- **POST** `/process/clean-text` - Clean and normalize text
- **POST** `/process/summarize` - Summarize text
- **POST** `/process/extract-key-points` - Extract key points
- **POST** `/process/tag-category` - Categorize text

Request body:
```json
{
  "text": "Your input text here"
}
```

### Process Complete Workflow
- **POST** `/process/workflow`
- Execute multiple steps in sequence

Request body:
```json
{
  "text": "Your input text here",
  "steps": [
    {"type": "clean-text"},
    {"type": "summarize"}
  ]
}
```

## Environment Variables

- `GEMINI_API_KEY` - Your Google Gemini API key (required)
- `PORT` - Server port (default: 5000)

## What's Done
✅ Flask API with CORS support
✅ LLM service integration with Google Gemini
✅ Four text processing operations
✅ Health check endpoint
✅ Complete workflow processing
✅ Error handling and validation

## What's Not Done
❌ Rate limiting
❌ Authentication/Authorization
❌ Caching for repeated requests
❌ Support for other LLM providers
❌ Advanced error recovery
