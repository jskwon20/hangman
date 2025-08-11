import random
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()

# Word list
words = [
    {'word': 'apple', 'hint': '과일'},
    {'word': 'house', 'hint': '건물'},
    {'word': 'water', 'hint': '액체'},
    {'word': 'music', 'hint': '소리'},
    {'word': 'happy', 'hint': '감정'},
    {'word': 'computer', 'hint': '전자기기'},
    {'word': 'book', 'hint': '독서'},
    {'word': 'school', 'hint': '교육 기관'},
    {'word': 'guitar', 'hint': '악기'},
    {'word': 'pizza', 'hint': '음식'}
]

# Game state (in-memory, for simplicity)
game_state = {}

class Guess(BaseModel):
    letter: str

def new_game():
    """Starts a new game by selecting a word and resetting the state."""
    word_data = random.choice(words)
    game_state['word'] = word_data['word']
    game_state['hint'] = word_data['hint']
    game_state['guessed_letters'] = []
    game_state['remaining_attempts'] = 6
    game_state['word_display'] = ['_' for _ in game_state['word']]

# API Endpoints
@app.post("/api/game/new")
async def start_new_game():
    new_game()
    return {
        "word_length": len(game_state['word']),
        "remaining_attempts": game_state['remaining_attempts'],
        "word_display": game_state['word_display']
    }

@app.post("/api/game/guess")
async def make_guess(guess: Guess):
    letter = guess.letter.lower()

    if not letter.isalpha() or len(letter) != 1:
        raise HTTPException(status_code=400, detail="Invalid guess. Please provide a single letter.")

    if letter in game_state['guessed_letters']:
        raise HTTPException(status_code=400, detail="You have already guessed this letter.")

    game_state['guessed_letters'].append(letter)

    if letter in game_state['word']:
        for i, char in enumerate(game_state['word']):
            if char == letter:
                game_state['word_display'][i] = letter
        correct_guess = True
    else:
        game_state['remaining_attempts'] -= 1
        correct_guess = False

    game_over = game_state['remaining_attempts'] <= 0 or '_' not in game_state['word_display']
    
    return {
        "correct_guess": correct_guess,
        "word_display": game_state['word_display'],
        "remaining_attempts": game_state['remaining_attempts'],
        "guessed_letters": game_state['guessed_letters'],
        "game_over": game_over,
        "word": game_state['word'] if game_over else None
    }

@app.get("/api/game/hint")
async def get_hint():
    return {"hint": game_state.get('hint', 'No game in progress.')}

# Static files and main page serving
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("hangman.html")

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    # To prevent API calls from being caught here
    if full_path.startswith("api/"):
        return JSONResponse(status_code=404, content={"detail": "Not Found"})
    return FileResponse("hangman.html")

# Initialize a game on startup
@app.on_event("startup")
async def startup_event():
    new_game()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
