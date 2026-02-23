from googletrans import Translator

def translate_to_kannada(text):
    # Initialize the Translator
    translator = Translator()
    
    # Translate text from English to Kannada
    translated = translator.translate(text, src='en', dest='kn')
    
    # Return the translated text
    return translated.text

# Example usage
english_text = "good Afternoon, had your lunch?"
kannada_translation = translate_to_kannada(english_text)

print(f"English: {english_text}")
print(f"Kannada: {kannada_translation}")