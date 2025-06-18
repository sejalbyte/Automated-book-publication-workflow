import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") or "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"

# Files
INPUT_FILE = "data/spun_chapter1_v1.txt"
OUTPUT_FILE = "data/reviewed_chapter1_v2.txt"

def review_and_refine(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a literary reviewer. Improve the clarity, flow, and engagement of this modernized chapter while preserving its tone and style."},
            {"role": "user", "content": f"Please review and refine this rewritten chapter:\n\n{text}"}
        ],
        temperature=0.7,
        max_tokens=3000
    )
    return response.choices[0].message["content"]

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        spun_text = f.read()

    reviewed_text = review_and_refine(spun_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(reviewed_text)

    print(f"[✓] Reviewed version saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()


