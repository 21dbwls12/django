from openai import OpenAI

def qna(question) :
   
    client = OpenAI(api_key = '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')

    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": question},
            )
    
    chat = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=messages )
    
    return chat.choices[0].message.content
        
def getImage(question) :
   
    client = OpenAI(api_key = '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')

    # messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    # messages.append(
    #             {"role": "user", "content": question},
    #         )
    
    getImage = client.images.generate(
        model="dall-e-3",
        prompt= question,
        n= 1,
        size= "1024x1024",
        # messages = messages,
    )
    # model="gpt-3.5-turbo", messages=messages )
    
    # if getImage.data[0].url == None :
    #     return None
    # else :
    return getImage.data[0].url
    # return chat.dict()["data"][0]["resource"]
    # return chat.choices[0].message.content