from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from config.database import shutdown_db, startup_db
from routers.users import router_usuario as user_router
from routers.game import router_game as game_router
from routers.feedback import router_feedback as feedback_router
from routers.categoria import router_categoria as categoria_router


app = FastAPI(title='BITTALES PAINEL ADMINISTRATIVO')

app.add_event_handler(event_type='startup', func=startup_db)
app.add_event_handler(event_type='shutdown', func=shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def status():
    return {
        'status': 'ok',
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

app.include_router(user_router)
app.include_router(game_router)
app.include_router(feedback_router)
app.include_router(categoria_router)

