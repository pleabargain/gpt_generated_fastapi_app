# source code
https://github.com/pleabargain/gpt_generated_fastapi_app

# video
https://youtu.be/uN3_lGWU94s

# what is this?
I'm trying to get GPT4 to generate FastAPI and pydantic applications that use OPENAI.

Ironically gpt4 isn't aware of the latest v. of openai and the code keeps defaulting to davinci!

I generated the 'genres' in seconds and that output goes straight to the UI so there is less fussing with the code. That being said, jinja is easy but it's still messy.

# assumptions
A lot of them. I'm no dev. 

That being said, you definitely need to know how to manipulate VS Code and how to be patient with errors!

I keep this readme open while I debug and remember stuff.

1. set up

```
python -m venv venv
```

2. activate
```
.\venv\Scripts\activate
```
3. set up .env

set your API key

4. install requirments
```
pip install -r requirements.txt
```
5. run it
```
uvicorn main:app --reload
```
6. hide env file
```
echo .env >> .gitignore
```

# resources
* https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo

* https://www.echohive.live/

* GPT4

# TODO
So much!

GPT4 can take in a lot of data but it doesn't spit out that much so you have to read the output carefully.

The story output is UGLY. 

And,  I haven't figured out how to get the output as JSON.

* save the ouput to a new file
* display and save the output as JSON
* save the output to a database


