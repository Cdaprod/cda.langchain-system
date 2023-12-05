# Instead of `import openai` we will use
OpenAI = promptlayer.openai.OpenAI
openai = OpenAI()

# Make a completion to OpenAI
response = openai.completions.create(
  model="text-davinci-003", 
  prompt="My name is",
)
print(response.choices[0].text)
