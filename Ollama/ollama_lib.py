import ollama
import base64
#
# #direct response

response=ollama.generate(model="llama3.2:1b", prompt='what is a cell?')
print(response.response)


#Stream response (produces only the response, no metadata)
result=ollama.generate(model="llama3.2:1b", prompt='what is a cell?', stream=True)
for i in result:
    print(i['response'], end='')

# #Giving multimodal input to the model (passing image to the model)

image_path=""

with open(image_path, "rb") as f:
    image_bytes=f.read() #reading the image
img_64=base64.b64encode(image_bytes).decode("utf-8") #encoding the image in base 64 bits
result=ollama.generate(model="gemma3:4b", images={img_64},prompt='Give caption for the image')
print(result.response)

# #Passing multiple images to the model

image_paths= ['','']

images_base64=[]
for i in image_paths:
    with open(i, "rb") as f:
        image_bytes = f.read()  # reading the image
        images_base64.append(base64.b64encode(image_bytes).decode("utf-8")) # encoding the image in base 64 bits

result=ollama.generate(model="gemma3:4b", images=images_base64,prompt='Generate a story based on these images, make sure you take context of each image')
print(result.response)

# #System instructions to the model

result=ollama.generate(model="llama3.2:1b", prompt='what is a cell?', system='You are a Scientist, explain things in that way')
print(result.response)

#Options parameter change of the model

result=ollama.generate(model="llama3.2:1b", prompt='what is a cell?',
                       options={
                           'temperature':0.5,
                           'top_p':0.5, #Selects smallest set of tokens whose cumulative probability ≥ 50%.
                           'top_k':45  #Limits selection to the top 45 most probable tokens at each step.
                       })
print(result.response)


#ollama list
local_models=ollama.list()
print(local_models)

for i in local_models['models']:
    print(i['model'])
    print(i['size'])


#ollama pull

model_name='gemma3:4b'
progress= ollama.pull(model_name,stream=True)

for i in progress:
    print(i)


# # #Ollama show
#
model_details=ollama.show('gemma3:4b')
print(model_details.dict())

