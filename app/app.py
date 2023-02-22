import os
import openai
from dotenv import load_dotenv
import argparse

load_dotenv() #load files from .env file
openai.api_key = os.getenv("OPENAI_APIKEY")



def main():
    print("app is running!")

    #unlike java's public static void main str[] args, python doesn't pick up 
    #commands from the terminal so we have to parse them ourselves using argparse module

    #create parser object
    parser =  argparse.ArgumentParser(description="parses some input as a string")

    #gives direction to the parser 
    #capture everything that comes after i
    #converts it to a string
    #required to have a input
    parser.add_argument('-i', type=str, required=True)

    #parse the args
    args = parser.parse_args()
    input = args.i

    res = generateContent(input)
    print(res)



def generateContent(input : str) -> str:

    prompt = f'generate a upbeat and catchy branding snippet for {input}'
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=24)
    return(getContent(response))


def getContent(response : dict) -> str:

    #get content and strip whitespace
    content = response.get('choices')[0].get('text')
    return(content.strip().strip("\""))



if __name__ == "__main__":
    main()



