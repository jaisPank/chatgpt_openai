import openai
class Chatbot:
    def __init__(self):
        openai.api_key= "api-key"

    def get_response(self,input):
        response= openai.Completion.create(
            engine="text-davinci-003",
            prompt=input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__== "__main__":
    chatbot=Chatbot()
    response=chatbot.get_response("Write about Birds.")
    print(response)

