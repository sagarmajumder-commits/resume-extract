# resume-extract

Extract structured data from PDF resumes.

## Features

- Extract contact information (email, phone, LinkedIn)
- Parse work experience
- Identify skills and technologies
- Education history
- Output as JSON

## Usage

```bash
pip install -r requirements.txt
python -m extract.parser resume.pdf
```

## Output Format

```json
{
  "contact": {
    "email": "john@example.com",
    "phone": "+1-555-0123",
    "linkedin": "linkedin.com/in/johndoe"
  },
  "skills": ["Python", "Docker", "AWS"],
  "experience": [
    {
      "title": "Senior Engineer",
      "company": "Tech Corp",
      "duration": "2020-2023"
    }
  ]
}
```

## Requirements

- Python 3.8+
- PyPDF2

## License

MIT
