
### `screener.py`
```python
import re
from collections import Counter

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def match_resume(resume_file, job_file):
    with open(resume_file) as f:
        resume = f.read()
    with open(job_file) as f:
        job_desc = f.read()

    resume_keywords = extract_keywords(resume)
    job_keywords = extract_keywords(job_desc)

    matched = sum((job_keywords & resume_keywords).values())
    total = sum(job_keywords.values())
    score = (matched / total) * 100 if total > 0 else 0
    print(f"Resume Match Score: {score:.2f}%")

if __name__ == "__main__":
    match_resume("sample_resume.txt", "job_description.txt")
