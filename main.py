from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

client = OpenAI()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Pydantic models
class Genre(BaseModel):
    name: str

# class StoryParameters(BaseModel):
#     genre: str

class StoryParameters(BaseModel):
    genre: str
    max_tokens: int = 100  # Default value, you can adjust it as needed



# FastAPI application
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_form(request: Request):
    genres = [
        Genre(name="Sci-Fi"), 
        Genre(name="Office Drama"), 
        Genre(name="Rom-Com"),
        Genre(name="Horror"),
        Genre(name="Fantasy"),
        Genre(name="Mystery"),
        Genre(name="Thriller"),
        Genre(name="Superhero"),
        Genre(name="Historical Fiction"),   
        Genre(name="Romance in Paris in the 1920s"),
        Genre(name="Action"),
        Genre(name="Adventure"),
        Genre(name="Biography of a Real Person"),
        Genre(name="Crime"),
        Genre(name="Drama"),
        Genre(name="Historical"),
        Genre(name="Political"),
        Genre(name="Satire"),
        Genre(name="Western"),
        Genre(name="Paranormal"),
        Genre(name="Young Adult"),
        Genre(name="Children"),
        Genre(name="Comedy"),
        Genre(name="Romance"),
        Genre(name="Erotica"),
    ]

    # Sort the genres alphabetically by their names
    sorted_genres = sorted(genres, key=lambda genre: genre.name)

    return templates.TemplateResponse("form.html", {
        "request": request, 
        "genres": sorted_genres
    })

@app.post("/submit_form")
async def form_post(request: Request, genre: str = Form(...)):
    try:
        form_data = StoryParameters(
            genre=genre
        )

        # Constructing the prompt for OpenAI
        prompt = f"Write a story in the genre of {form_data.genre}, with a creative plot and engaging characters."

 

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
                max_tokens=form_data.max_tokens,
                model="gpt-4",
        )

        # Extracting the story text
        # story = response.choices[0].text.strip()
        story = response


    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        story = "An error occurred while generating the story."

    return templates.TemplateResponse("story.html", {
        "request": request, 
        "story": story, 
        "form_data": form_data
    })

