from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from llm_service import LLMService

load_dotenv()

app = Flask(__name__)
CORS(app)

llm_service = LLMService()

@app.route('/health', methods=['GET'])
def health_check():
    """Check the health of the Flask API and LLM connection"""
    try:
        # Test LLM connection
        llm_status = llm_service.check_connection()
        
        return jsonify({
            'status': 'healthy',
            'service': 'flask-api',
            'llm_connection': llm_status
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'service': 'flask-api',
            'error': str(e)
        }), 500

@app.route('/process/clean-text', methods=['POST'])
def clean_text():
    """Clean and normalize input text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        input_text = data['text']
        
        if not input_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = llm_service.clean_text(input_text)
        
        return jsonify({
            'success': True,
            'result': result,
            'step': 'clean-text'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/process/summarize', methods=['POST'])
def summarize():
    """Summarize the input text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        input_text = data['text']
        
        if not input_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = llm_service.summarize(input_text)
        
        return jsonify({
            'success': True,
            'result': result,
            'step': 'summarize'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/process/extract-key-points', methods=['POST'])
def extract_key_points():
    """Extract key points from the input text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        input_text = data['text']
        
        if not input_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = llm_service.extract_key_points(input_text)
        
        return jsonify({
            'success': True,
            'result': result,
            'step': 'extract-key-points'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/process/tag-category', methods=['POST'])
def tag_category():
    """Tag/categorize the input text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        input_text = data['text']
        
        if not input_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        result = llm_service.tag_category(input_text)
        
        return jsonify({
            'success': True,
            'result': result,
            'step': 'tag-category'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/process/workflow', methods=['POST'])
def process_workflow():
    """Process a complete workflow with multiple steps"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data or 'steps' not in data:
            return jsonify({'error': 'Missing text or steps'}), 400
        
        input_text = data['text']
        steps = data['steps']
        
        if not input_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        if not steps or len(steps) < 2:
            return jsonify({'error': 'Workflow must have at least 2 steps'}), 400
        
        results = []
        current_text = input_text
        
        for step in steps:
            step_type = step.get('type')
            
            if step_type == 'clean-text':
                output = llm_service.clean_text(current_text)
            elif step_type == 'summarize':
                output = llm_service.summarize(current_text)
            elif step_type == 'extract-key-points':
                output = llm_service.extract_key_points(current_text)
            elif step_type == 'tag-category':
                output = llm_service.tag_category(current_text)
            else:
                return jsonify({'error': f'Unknown step type: {step_type}'}), 400
            
            results.append({
                'step': step_type,
                'input': current_text,
                'output': output
            })
            
            current_text = output
        
        return jsonify({
            'success': True,
            'results': results
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

