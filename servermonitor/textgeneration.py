
from transformers import Pipeline

generator = Pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
prompt = "Rolls-Royce is a household name, but only a few have experienced its pristine luxury."
res = generator(prompt, max_length=50, do_sample=True, temperature=0.9)
print(res[0]['generated_text'])
with open('gpttext.txt', 'w') as f:
    f.writelines(res[0]['generated_text'])
    f.close()