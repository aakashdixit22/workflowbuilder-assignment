import os
from google import genai

class LLMService:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-2.5-flash'
    
    def check_connection(self):
        """Check if the LLM API is accessible"""
        try:
            # Make a minimal API call to check connection
            response = self.client.models.generate_content(
                model=self.model_name,
                contents="test"
            )
            return 'connected'
        except Exception as e:
            return f'disconnected: {str(e)}'
    
    def clean_text(self, text):
        """Clean and normalize text"""
        try:
            prompt = f"""You are a text cleaning assistant. Remove unnecessary whitespace, fix formatting issues, correct obvious typos, and normalize the text. Return only the cleaned text without any explanation.

Text to clean:
{text}"""
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error cleaning text: {str(e)}")
    
    def summarize(self, text):
        """Summarize the text"""
        try:
            prompt = f"""You are a summarization assistant. Create a concise summary of the input text, capturing the main points. Keep it brief (2-3 sentences). Return only the summary without any preamble.

Text to summarize:
{text}"""
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error summarizing text: {str(e)}")
    
    def extract_key_points(self, text):
        """Extract key points from text"""
        try:
            prompt = f"""You are an analysis assistant. Extract the key points from the input text as a bulleted list. Focus on the most important information. Return only the key points in bullet format.

Text to analyze:
{text}"""
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error extracting key points: {str(e)}")
    
    def tag_category(self, text):
        """Categorize and tag the text"""
        try:
            prompt = f"""You are a categorization assistant. Analyze the input text and assign relevant categories/tags. Common categories include: Business, Technology, Health, Education, Entertainment, Science, Politics, Sports, Finance, Lifestyle. Return 2-4 most relevant categories as a comma-separated list.

Text to categorize:
{text}"""
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error tagging category: {str(e)}")
