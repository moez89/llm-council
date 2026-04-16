@echo off
echo ============================================
echo   LLM Council - Starting...
echo ============================================
echo.

:: Check .env exists
if not exist .env (
    echo ERROR: .env file not found.
    echo Please create a .env file with:
    echo   OPENROUTER_API_KEY=your_key_here
    pause
    exit /b 1
)

echo Starting backend on http://localhost:8001 ...
start "LLM Council - Backend" cmd /k "python -m backend.main"

timeout /t 2 /nobreak >nul

echo Starting frontend on http://localhost:5173 ...
start "LLM Council - Frontend" cmd /k "cd frontend && npm run dev"

timeout /t 3 /nobreak >nul

echo.
echo ============================================
echo   App is running!
echo   Open: http://localhost:5173
echo ============================================
echo.
echo Opening browser...
start http://localhost:5173

echo.
echo Two windows opened (Backend + Frontend).
echo Close them to stop the app.
pause
