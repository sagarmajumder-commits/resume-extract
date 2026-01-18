"""Resume PDF parser."""
import re
import json
from pathlib import Path
from typing import Dict, List, Optional
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None


class ResumeParser:
    """Parse resume PDFs and extract structured data."""
    
    def __init__(self):
        if PdfReader is None:
            raise ImportError("PyPDF2 is required. Install with: pip install PyPDF2")
    
    def extract_text(self, pdf_path: str) -> str:
        """Extract raw text from PDF."""
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    def extract_email(self, text: str) -> Optional[str]:
        """Extract email address."""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(pattern, text)
        return match.group(0) if match else None
    
    def extract_phone(self, text: str) -> Optional[str]:
        """Extract phone number."""
        patterns = [
            r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        ]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return None
    
    def extract_skills(self, text: str) -> List[str]:
        """Extract technical skills."""
        common_skills = [
            'Python', 'Java', 'JavaScript', 'Go', 'Rust', 'C++',
            'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP',
            'PostgreSQL', 'MongoDB', 'Redis',
            'React', 'Node.js', 'Django', 'Flask'
        ]
        
        found_skills = []
        text_upper = text.upper()
        
        for skill in common_skills:
            if skill.upper() in text_upper:
                found_skills.append(skill)
        
        return found_skills
    
    def parse(self, pdf_path: str) -> Dict:
        """
        Parse resume and return structured data.
        
        Args:
            pdf_path: Path to PDF resume
            
        Returns:
            Dictionary with extracted information
        """
        text = self.extract_text(pdf_path)
        
        return {
            'contact': {
                'email': self.extract_email(text),
                'phone': self.extract_phone(text)
            },
            'skills': self.extract_skills(text),
            'raw_text_length': len(text)
        }


def main():
    """CLI entry point."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m extract.parser <resume.pdf>")
        sys.exit(1)
    
    parser = ResumeParser()
    result = parser.parse(sys.argv[1])
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
