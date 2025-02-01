#%%
from scrape_guardian import scrape_guardian
import re

def concatenate_texts(texts):
    return " ".join([tag.get_text(strip=True) for tag in texts])
texts = scrape_guardian()
text = concatenate_texts(texts)

# proper nouns for default url to check
proper_nouns = [
    "US",
    "Donald Trump",
    "DeepSeek",
    "OpenAI",
    "ChatGPT",
    "Google",
    "Gemini",
    "R1",
    "Nvidia",
    "AI",
    "Apple",
    "Sam Altman",
    "Asia",
    "Nikkei",
    "Advantest",
    "Tokyo Electron",
    "Disco Corporation",
    "SoftBank",
    "Business Today",
    "Marc Andreessen",
    "US-USSR",
    "X",
    "Soviet Union",
    "Artificial Analysis",
    "Meta",
    "Anthropic",
    "Liang Wenfeng",
    "High-Flyer Capital",
    "Hangzhou",
    "o1-mini",
    "o1"
]
# %%

reg_exp = r"\b[A-Z][a-z]*\b|\b[A-Z][a-z]*\b\s\b[A-Z][a-z]*\b|\b[A-Z]+\b"

matches = set(re.findall(reg_exp, text))
print(matches)

correct = 0
for t in matches:
    if t in proper_nouns:
        correct += 1

print(f"You got {correct/len(proper_nouns):.2f} correct.")
# %%
