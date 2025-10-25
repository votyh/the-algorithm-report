import openai
import datetime
import os
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

# Directory setup
output_dir = Path("posts")
output_dir.mkdir(exist_ok=True)

today = datetime.date.today().isoformat()

topics = [
    "AI & Machine Learning",
    "Technology & Innovation",
    "Business & Finance",
    "World Economy & Global Affairs"
]

def generate_report(topic):
    prompt = f"Write a short, factual and professional 2025 news summary (120–160 words) about the latest developments in {topic}. Use a formal and journalistic tone, suitable for a technology publication called The Algorithm Report."
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]

content = f"# The Algorithm Report — {today}\n\n"
content += "This edition covers key developments across AI, technology, business, and global affairs.\n\n"

for topic in topics:
    try:
        article = generate_report(topic)
        content += f"## {topic}\n\n{article}\n\n"
    except Exception as e:
        content += f"## {topic}\n\nError generating content: {e}\n\n"

# Save the report
file_path = output_dir / f"report_{today}.md"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Generated report saved to {file_path}")

