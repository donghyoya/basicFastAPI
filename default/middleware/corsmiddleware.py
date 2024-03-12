from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    origins = [
        "http://localhost:3000",
        "https://www.example.com",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
