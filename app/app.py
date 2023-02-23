import os
import openai
from dotenv import load_dotenv
import argparse


load_dotenv() #load files from .env file
openai.api_key = os.getenv("OPENAI_APIKEY")



def main():
    parser =  argparse.ArgumentParser(description="parses some input as a string")
    parser.add_argument('-i', type=str, required=True)
    args = parser.parse_args()
    input = args.i

    if validateInput(input):
        generateContent(input)
        generateKeywords(input)
    else:
        print("your input is too long! must be under 30 characters")



def generateContent(input : str) -> str:
    prompt = f'generate a upbeat and catchy branding snippet for {input}'
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=32)
    print(getContent(response))


def generateKeywords(input: str):
    prompt = f'generate related branding keywords for {input} in a string format and in lowercase'
    response = openai.Completion.create(
    engine="text-davinci-003", prompt=prompt, max_tokens=40)
    print(parseKeywords(response))



def getContent(response : dict) -> str:
    #get content and strip whitespace
    content = response.get('choices')[0].get('text')
    content = content.strip().strip("\"")
    punc = {"!", ".", "?"}
    i = len(content) - 1
    while i> 0:
        if content[i] in punc:
            break
        i -= 1
    
    #sentence might be cut off due to token limit, so return the full sentences
    return content[:i + 1]
        


def parseKeywords(response: dict):
    content = response.get('choices')[0].get('text')
    content = content.strip().strip("\"")
    keywords = content.split(",")
    for x in range(len(keywords)):
        keywords[x] = keywords[x].strip()

    #last word might be cut off due to token limit so omit last word for consistency
    return keywords[:-1]


#person using the app could intentionally enter something bad to burn our openai credits
def validateInput(input: str) -> bool:
    return len(input) <= 30
        




if __name__ == "__main__":
    main()



