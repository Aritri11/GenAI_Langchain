from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

model= ChatOpenAI(model='gpt-3.5')

#schema
class Review(BaseModel):
    key_themes: list[str]=Field(description='Write down all the key themes discussed in the review in a list')
    summary: str= Field(description='A brief summary of the review')
    sentiment: Literal["pos", "neg"]= Field(description='Return sentiment of the review either negative, positive or neutral') #literal when used makes only decisions based on the ones given inside the literal
    pros: Optional[list[str]]=Field(default=None,description='write down all the pros inside a list') #optional is for the llm to understand that if not explicitly mentioned do not give that
    cons: Optional[list[str]]=Field(default=None, description='write down all the cons inside a list')

structured_model= model.with_structured_output(Review)

result= structured_model.invoke("""I recently purchased the Dell Inspiron XPS-Prime 15 after months of research and careful comparison with competitors, and here’s my honest experience with it. I’ll break it down into different sections so you can understand the good, the bad, and everything in between.
Included in the box were: The laptop itself ,90W USB-C charger, Quick start guide, Warranty card. The 15.6-inch QHD+ (2560x1600) IPS panel is one of the highlights of this machine.I opted for the configuration with: Intel Core i7–13650H, 16GB DDR5 RAM, 512GB NVMe SSD.
Pros:
Excellent display quality and brightness
Solid everyday and productivity performance
Responsive keyboard and trackpad
Good battery life for general use
Clean design with ample port selection
Fast SSD and reliable wireless
Cons:
Fans get loud under heavy load
No dedicated GPU for intense creative/gaming tasks
Keyboard flex and slightly awkward key sizes
Webcam quality could be better""")
print(result)
print(result["summary"])
print(result["sentiment"])

