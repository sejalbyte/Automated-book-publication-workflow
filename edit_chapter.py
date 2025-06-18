import openai
import os

# Set up API key
openai.api_key = os.getenv("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")

INPUT_FILE = "data/spun_chapter1_v1_reviewed.txt"
OUTPUT_FILE = "data/spun_chapter1_v2.txt"

def load_input():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def save_output(text):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

def edit_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert book editor. Make the text more polished and consistent in tone."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message['content']

def main():
    raw_text = load_input()
    edited_text = edit_text(raw_text)
    save_output(edited_text)
    print("✅ Editing complete. Saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
