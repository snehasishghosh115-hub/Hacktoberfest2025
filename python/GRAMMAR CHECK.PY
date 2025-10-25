import language_tool_python

def check_grammar(text):
    # Initialize the LanguageTool object for English
    tool = language_tool_python.LanguageTool('en-US')
    
    # Check text for grammar errors
    matches = tool.check(text)
    
    # Show detailed error suggestions
    for match in matches:
        print(f"Error: {match.ruleId}")
        print(f"Issue: {match.message}")
        print(f"Incorrect text: {match.context}")
        print(f"Suggested correction: {match.replacements}
")
    
    # Return corrected text
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text
