import ollama


inventory_db= {
    "laptop": {'stock': 5, 'base_price': 1200},
    "monitor": {'stock': 6, 'base_price': 300},
    "keyboard": {'stock': 20, 'base_price': 500},
}

#Tool defining

#Tool1: Checking Database
def check_inventory(product_name):
    product_name=product_name.lower()

    if product_name in inventory_db:
        return inventory_db[product_name]

    return {'stock':0, 'base_price':None}


#Tool2: Business logic for Discounts
def calculate_loyalty_discount(base_price, yrs_as_customer):
    discount=min(yrs_as_customer * 0.05,0.30) #max 30% as discount
    final_price=base_price*(1-discount)
    return round(final_price,2)

# 1. Mapping the functions so the script can call them by name
available_function = {
    'check_inventory': check_inventory,
    'calculate_loyalty_discount': calculate_loyalty_discount
}


#Defining schema

tools= [
    {
        'type': 'function',
        'function': {
            'name': 'check_inventory',
            'description':'Get stock and price for a product',
            'parameters': {
                'type': 'object',
                'properties': {
                    'product_name': {'type': 'string'}
                },
                'required': ['product_name']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'calculate_loyalty_discount',
            'description':'Calculate loyalty discount',
            'parameters': {
                'type': 'object',
                'properties': {
                    'base_price': {'type': 'number'},
                    'yrs_as_customer': {'type': 'integer'}
                },
                'required': ['base_price', 'yrs_as_customer']
            }
        }
    }
]

#Passing the query and tool info to the llm

message=[
    {'role': 'user','content': 'I want to buy an iPhone. Can you check the stock?'}

]

#Calling LLM
response=ollama.chat(
    model='qwen3:4b',
    messages=message,
    tools=tools
)

# # print(response)
# print(response['message'])

#Check if the model asked to use any tool

tool_calls=response['message'].get('tool_calls')

if tool_calls:
    for tool_call in tool_calls:
        tool_name= tool_call['function']['name']
        tool_args=tool_call['function']['arguments']

        #Get the created python function
        function__to_call= available_function[tool_name]

        #Run the function with given arguments
        result=function__to_call(**tool_args)

        #Add the model's tool request to the conversation
        message.append(response['message'])

        #Add the tool's result back to the conversation
        message.append({
            'role': 'tool',
            'content': str(result)
        })

#Ask the model to generate the final answer

final_response=ollama.chat(
    model='qwen3:4b',
    messages=message
)

print(final_response['message']['content'])

















