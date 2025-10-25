import os, requests, random, datetime

# ✅ Setup
topics = ["AI", "Technology", "Science", "Startups", "Future Trends", "Robotics", "Space Exploration"]
today = datetime.datetime.now().strftime("%Y-%m-%d")

def generate_post():
    topic = random.choice(topics)
    title = f"Latest {topic} Update - {today}"
    content = f"This report covers the newest developments in {topic.lower()} as of {today}. Stay tuned for future insights."
    return title, content

def save_post(title, content):
    os.makedirs("content", exist_ok=True)
    filename = f"content/{title.replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content}\n")

if __name__ == "__main__":
    title, content = generate_post()
    save_post(title, content)
    print(f"✅ Generated post: {title}")
