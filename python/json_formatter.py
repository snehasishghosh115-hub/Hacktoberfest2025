"""
JSON Formatter and Validator

A comprehensive utility for formatting, validating, and manipulating JSON data.
Useful for developers working with APIs, configuration files, and data processing.

Features:
- Pretty print JSON with customizable indentation
- Validate JSON syntax
- Minify JSON (remove whitespace)
- Convert between JSON and Python dictionaries
- Sort JSON keys alphabetically
- Find and extract values by key path
- Compare two JSON objects

Author: Contributing to Hacktoberfest 2025
Date: October 2025
"""

import json
import sys
from typing import Any, Dict, List, Union, Optional
from pathlib import Path


class JSONFormatter:
    """A utility class for JSON formatting and manipulation."""
    
    def __init__(self, indent: int = 2):
        """
        Initialize the JSONFormatter.
        
        Args:
            indent: Number of spaces for indentation (default: 2)
        """
        self.indent = indent
    
    def pretty_print(self, json_data: Union[str, Dict, List], 
                    sort_keys: bool = False) -> str:
        """
        Format JSON with proper indentation for readability.
        
        Args:
            json_data: JSON string or Python object
            sort_keys: Sort keys alphabetically if True
            
        Returns:
            Formatted JSON string
            
        Raises:
            ValueError: If JSON is invalid
        """
        try:
            # Parse if string, otherwise use as-is
            if isinstance(json_data, str):
                data = json.loads(json_data)
            else:
                data = json_data
            
            # Format with indentation
            formatted = json.dumps(
                data,
                indent=self.indent,
                sort_keys=sort_keys,
                ensure_ascii=False
            )
            
            return formatted
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
    
    def minify(self, json_data: Union[str, Dict, List]) -> str:
        """
        Remove all unnecessary whitespace from JSON.
        
        Args:
            json_data: JSON string or Python object
            
        Returns:
            Minified JSON string
        """
        try:
            if isinstance(json_data, str):
                data = json.loads(json_data)
            else:
                data = json_data
            
            return json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
    
    def validate(self, json_string: str) -> tuple[bool, Optional[str]]:
        """
        Validate JSON syntax.
        
        Args:
            json_string: JSON string to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            json.loads(json_string)
            return True, None
        except json.JSONDecodeError as e:
            return False, str(e)
    
    def get_value_by_path(self, json_data: Union[str, Dict, List], 
                         path: str) -> Any:
        """
        Extract value from JSON using dot notation path.
        
        Args:
            json_data: JSON string or Python object
            path: Dot-separated path (e.g., "user.address.city")
            
        Returns:
            Value at the specified path
            
        Raises:
            KeyError: If path doesn't exist
        """
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        
        keys = path.split('.')
        current = data
        
        for key in keys:
            # Handle array indices
            if '[' in key and ']' in key:
                key_name = key[:key.index('[')]
                index = int(key[key.index('[')+1:key.index(']')])
                current = current[key_name][index]
            else:
                current = current[key]
        
        return current
    
    def compare(self, json1: Union[str, Dict, List], 
                json2: Union[str, Dict, List]) -> Dict[str, Any]:
        """
        Compare two JSON objects and find differences.
        
        Args:
            json1: First JSON object
            json2: Second JSON object
            
        Returns:
            Dictionary with comparison results
        """
        if isinstance(json1, str):
            data1 = json.loads(json1)
        else:
            data1 = json1
            
        if isinstance(json2, str):
            data2 = json.loads(json2)
        else:
            data2 = json2
        
        return {
            'are_equal': data1 == data2,
            'keys_in_first_only': self._get_keys_difference(data1, data2),
            'keys_in_second_only': self._get_keys_difference(data2, data1),
            'different_values': self._find_different_values(data1, data2)
        }
    
    def _get_keys_difference(self, dict1: Dict, dict2: Dict, 
                            prefix: str = '') -> List[str]:
        """Helper method to find keys that exist in dict1 but not in dict2."""
        diff_keys = []
        
        if not isinstance(dict1, dict):
            return diff_keys
        
        for key in dict1:
            current_path = f"{prefix}.{key}" if prefix else key
            
            if key not in dict2:
                diff_keys.append(current_path)
            elif isinstance(dict1[key], dict) and isinstance(dict2.get(key), dict):
                diff_keys.extend(
                    self._get_keys_difference(dict1[key], dict2[key], current_path)
                )
        
        return diff_keys
    
    def _find_different_values(self, dict1: Dict, dict2: Dict, 
                               prefix: str = '') -> List[Dict]:
        """Helper method to find values that differ between dictionaries."""
        differences = []
        
        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            return differences
        
        common_keys = set(dict1.keys()) & set(dict2.keys())
        
        for key in common_keys:
            current_path = f"{prefix}.{key}" if prefix else key
            val1, val2 = dict1[key], dict2[key]
            
            if isinstance(val1, dict) and isinstance(val2, dict):
                differences.extend(
                    self._find_different_values(val1, val2, current_path)
                )
            elif val1 != val2:
                differences.append({
                    'path': current_path,
                    'value1': val1,
                    'value2': val2
                })
        
        return differences
    
    def read_from_file(self, filepath: str) -> Dict:
        """
        Read and parse JSON from a file.
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            Parsed JSON data
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def write_to_file(self, data: Union[Dict, List], filepath: str, 
                     pretty: bool = True):
        """
        Write JSON data to a file.
        
        Args:
            data: Data to write
            filepath: Output file path
            pretty: Use pretty formatting if True, minify if False
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(data, f, indent=self.indent, ensure_ascii=False)
            else:
                json.dump(data, f, separators=(',', ':'), ensure_ascii=False)


def print_section(title: str):
    """Helper function to print formatted section headers."""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)


def main():
    """Demonstrate JSONFormatter capabilities."""
    formatter = JSONFormatter(indent=2)
    
    print("🔧 JSON Formatter and Validator")
    print("="*60)
    
    # Sample JSON data
    sample_json = '''
    {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com",
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zipcode": "10001"
        },
        "hobbies": ["reading", "coding", "gaming"],
        "is_active": true
    }
    '''
    
    # 1. Pretty Print
    print_section("1. Pretty Print JSON")
    formatted = formatter.pretty_print(sample_json)
    print(formatted)
    
    # 2. Pretty Print with Sorted Keys
    print_section("2. Pretty Print with Sorted Keys")
    formatted_sorted = formatter.pretty_print(sample_json, sort_keys=True)
    print(formatted_sorted)
    
    # 3. Minify JSON
    print_section("3. Minified JSON")
    minified = formatter.minify(sample_json)
    print(minified)
    print(f"\nOriginal size: {len(sample_json)} chars")
    print(f"Minified size: {len(minified)} chars")
    print(f"Reduction: {((len(sample_json) - len(minified)) / len(sample_json) * 100):.1f}%")
    
    # 4. Validate JSON
    print_section("4. JSON Validation")
    
    valid_json = '{"key": "value"}'
    invalid_json = '{"key": "value"'
    
    is_valid, error = formatter.validate(valid_json)
    print(f"Valid JSON: {is_valid}")
    
    is_valid, error = formatter.validate(invalid_json)
    print(f"Invalid JSON: {is_valid}")
    if error:
        print(f"Error: {error}")
    
    # 5. Extract Value by Path
    print_section("5. Extract Value by Path")
    data = json.loads(sample_json)
    
    paths = [
        "name",
        "address.city",
        "hobbies[0]"
    ]
    
    for path in paths:
        try:
            value = formatter.get_value_by_path(data, path)
            print(f"{path} = {value}")
        except (KeyError, IndexError) as e:
            print(f"{path} = Not found")
    
    # 6. Compare JSON Objects
    print_section("6. Compare JSON Objects")
    
    json1 = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    json2 = {
        "name": "John",
        "age": 31,
        "country": "USA"
    }
    
    comparison = formatter.compare(json1, json2)
    print(f"Are equal: {comparison['are_equal']}")
    print(f"Keys only in first: {comparison['keys_in_first_only']}")
    print(f"Keys only in second: {comparison['keys_in_second_only']}")
    print(f"Different values: {comparison['different_values']}")
    
    # 7. Interactive Mode
    print_section("7. Interactive Mode")
    print("\nEnter JSON to format (or 'quit' to exit):")
    print("Example: {\"key\": \"value\"}\n")
    
    while True:
        try:
            user_input = input("\nJSON > ")
            
            if user_input.lower() == 'quit':
                break
            
            if not user_input.strip():
                continue
            
            # Try to format
            formatted = formatter.pretty_print(user_input)
            print("\n✅ Valid JSON - Formatted:")
            print(formatted)
            
            # Show minified version
            minified = formatter.minify(user_input)
            print(f"\n📦 Minified ({len(minified)} chars):")
            print(minified)
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except KeyboardInterrupt:
            break
    
    print("\n\n👋 Thank you for using JSON Formatter!")
    print("="*60)


if __name__ == "__main__":
    main()
