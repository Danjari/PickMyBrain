from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PickMyBrain API",
    description="A fun email analyzer for detecting 'pick your brain' requests",
    version="1.0.0"
)

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint - test that the API is running."""
    return {"message": "PickMyBrain API is running! 🧠"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "PickMyBrain"}

# TODO: Add your endpoints here!
# - POST /analyze-email - Analyze email content
# - GET /phrases - Get current trigger phrases
# - POST /phrases - Add new trigger phrases
# - POST /send-reply - Send auto-reply to email

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 