"""
Password Strength Checker

This module provides a comprehensive password strength checker that evaluates
passwords based on multiple security criteria and provides detailed feedback.

Features:
- Length validation
- Character type requirements (uppercase, lowercase, numbers, special chars)
- Common password detection
- Strength scoring system
- Detailed feedback for improvement

Author: Contributing to Hacktoberfest 2025
Date: October 2025
"""

import re
from typing import Dict, List, Tuple


class PasswordStrengthChecker:
    """A comprehensive password strength checker with scoring system."""
    
    # Common passwords to avoid (subset for demonstration)
    COMMON_PASSWORDS = {
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
        'baseball', 'iloveyou', 'master', 'sunshine', 'ashley',
        'bailey', 'passw0rd', 'shadow', '123123', '654321'
    }
    
    def __init__(self):
        """Initialize the password checker."""
        self.min_length = 8
        self.recommended_length = 12
        
    def check_password(self, password: str) -> Dict:
        """
        Check password strength and return detailed analysis.
        
        Args:
            password (str): The password to check
            
        Returns:
            Dict: Dictionary containing:
                - score: Overall score (0-100)
                - strength: Text description (Weak/Fair/Good/Strong/Very Strong)
                - checks: Dictionary of individual check results
                - suggestions: List of improvement suggestions
        """
        if not password:
            return {
                'score': 0,
                'strength': 'Invalid',
                'checks': {},
                'suggestions': ['Please enter a password']
            }
        
        # Perform individual checks
        checks = {
            'length': self._check_length(password),
            'uppercase': self._has_uppercase(password),
            'lowercase': self._has_lowercase(password),
            'numbers': self._has_numbers(password),
            'special_chars': self._has_special_chars(password),
            'no_common': not self._is_common_password(password),
            'no_sequential': not self._has_sequential_chars(password),
            'no_repeating': not self._has_repeating_chars(password)
        }
        
        # Calculate score
        score = self._calculate_score(password, checks)
        
        # Determine strength level
        strength = self._get_strength_level(score)
        
        # Generate suggestions
        suggestions = self._generate_suggestions(password, checks)
        
        return {
            'score': score,
            'strength': strength,
            'checks': checks,
            'suggestions': suggestions
        }
    
    def _check_length(self, password: str) -> bool:
        """Check if password meets minimum length requirement."""
        return len(password) >= self.min_length
    
    def _has_uppercase(self, password: str) -> bool:
        """Check if password contains uppercase letters."""
        return bool(re.search(r'[A-Z]', password))
    
    def _has_lowercase(self, password: str) -> bool:
        """Check if password contains lowercase letters."""
        return bool(re.search(r'[a-z]', password))
    
    def _has_numbers(self, password: str) -> bool:
        """Check if password contains numbers."""
        return bool(re.search(r'\d', password))
    
    def _has_special_chars(self, password: str) -> bool:
        """Check if password contains special characters."""
        return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    def _is_common_password(self, password: str) -> bool:
        """Check if password is in common passwords list."""
        return password.lower() in self.COMMON_PASSWORDS
    
    def _has_sequential_chars(self, password: str) -> bool:
        """Check for sequential characters (e.g., '123', 'abc')."""
        password_lower = password.lower()
        for i in range(len(password_lower) - 2):
            if (ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and
                ord(password_lower[i+2]) == ord(password_lower[i]) + 2):
                return True
        return False
    
    def _has_repeating_chars(self, password: str) -> bool:
        """Check for 3 or more repeating characters."""
        return bool(re.search(r'(.)\1{2,}', password))
    
    def _calculate_score(self, password: str, checks: Dict) -> int:
        """Calculate overall password score (0-100)."""
        score = 0
        
        # Length scoring (0-30 points)
        length = len(password)
        if length >= self.recommended_length:
            score += 30
        elif length >= self.min_length:
            score += 20
        else:
            score += length * 2
        
        # Character type scoring (40 points total)
        if checks['uppercase']:
            score += 10
        if checks['lowercase']:
            score += 10
        if checks['numbers']:
            score += 10
        if checks['special_chars']:
            score += 10
        
        # Bonus points (30 points total)
        if checks['no_common']:
            score += 10
        if checks['no_sequential']:
            score += 10
        if checks['no_repeating']:
            score += 10
        
        return min(score, 100)
    
    def _get_strength_level(self, score: int) -> str:
        """Convert score to strength level."""
        if score >= 80:
            return 'Very Strong'
        elif score >= 60:
            return 'Strong'
        elif score >= 40:
            return 'Good'
        elif score >= 20:
            return 'Fair'
        else:
            return 'Weak'
    
    def _generate_suggestions(self, password: str, checks: Dict) -> List[str]:
        """Generate improvement suggestions based on check results."""
        suggestions = []
        
        if not checks['length']:
            suggestions.append(f'Increase length to at least {self.min_length} characters')
        elif len(password) < self.recommended_length:
            suggestions.append(f'Consider using {self.recommended_length}+ characters for better security')
        
        if not checks['uppercase']:
            suggestions.append('Add uppercase letters (A-Z)')
        
        if not checks['lowercase']:
            suggestions.append('Add lowercase letters (a-z)')
        
        if not checks['numbers']:
            suggestions.append('Add numbers (0-9)')
        
        if not checks['special_chars']:
            suggestions.append('Add special characters (!@#$%^&*)')
        
        if not checks['no_common']:
            suggestions.append('Avoid common passwords')
        
        if not checks['no_sequential']:
            suggestions.append('Avoid sequential characters (e.g., abc, 123)')
        
        if not checks['no_repeating']:
            suggestions.append('Avoid repeating characters (e.g., aaa, 111)')
        
        if not suggestions:
            suggestions.append('Great! Your password is strong.')
        
        return suggestions


def print_password_analysis(analysis: Dict):
    """Pretty print password analysis results."""
    print("\n" + "="*50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("="*50)
    print(f"\n📊 Score: {analysis['score']}/100")
    print(f"💪 Strength: {analysis['strength']}")
    
    print("\n✅ Checks:")
    for check, passed in analysis['checks'].items():
        status = "✓" if passed else "✗"
        check_name = check.replace('_', ' ').title()
        print(f"  {status} {check_name}")
    
    print("\n💡 Suggestions:")
    for i, suggestion in enumerate(analysis['suggestions'], 1):
        print(f"  {i}. {suggestion}")
    
    print("\n" + "="*50 + "\n")


def main():
    """Main function to demonstrate password checker."""
    checker = PasswordStrengthChecker()
    
    print("🔐 Password Strength Checker")
    print("="*50)
    
    # Test examples
    test_passwords = [
        "weak",
        "Password1",
        "MyP@ssw0rd",
        "Str0ng!P@ssw0rd123",
        "V3ry$tr0ng&S3cur3P@ss!"
    ]
    
    for password in test_passwords:
        print(f"\nTesting: {'*' * len(password)}")
        analysis = checker.check_password(password)
        print(f"Score: {analysis['score']}/100 - {analysis['strength']}")
    
    print("\n" + "="*50)
    print("Interactive Mode")
    print("="*50)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\n👋 Thank you for using Password Strength Checker!")
            break
        
        analysis = checker.check_password(password)
        print_password_analysis(analysis)


if __name__ == "__main__":
    main()
