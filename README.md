# Xpert Forex Trade

A simple PHP MVC starter for a forex trading platform supporting spot and futures trading.

## Features
- User login
- Spot and futures trade placement
- Trade dashboard
- MVC structure (Models, Views, Controllers)
- MySQL database integration

## Project Structure
- `app/Controllers` - Handles user and trade actions
- `app/Models` - Database logic
- `app/Views` - HTML templates
- `config/config.php` - Loads DB settings from `.env`
- `public/index.php` - Front controller and router
- `.env.example` - Sample environment config

## Getting Started
1. Copy `.env.example` to `.env` and fill in your database details.
2. Create the database and tables:
    - `users` (id, username, password, etc.)
    - `trades` (id, user_id, pair, amount, direction, type, created_at)
3. Point your web server to `public/index.php`
4. Start building!

## Security
- Do NOT commit your real `.env` file.
- Add `.env` to `.gitignore`.
- Always validate user input in production!

## Deployment
- Push your code to GitHub: https://github.com/boostlink-creatorh/Xpert-Forex-Trade
- For issues or contributions, open a pull request.
