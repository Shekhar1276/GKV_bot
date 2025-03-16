# GKV Info Bot - Telegram

## Project Overview

GKV Info Bot is a Telegram bot designed to provide students of Gurukul Kangri Vishwavidyalaya with easy access to academic schedules, events, results, previous year question papers, and other university-related information. The bot integrates with university databases and utilizes web scraping techniques to fetch and deliver up-to-date information.

## Features

- Instant access to academic schedules, results, and notices
- Automatic and manual result downloads
- Access to previous year question papers and syllabus
- Personalized notifications about upcoming academic events
- Secure and efficient information retrieval via web scraping

## System Architecture

The project follows a multi-layered architecture:

1. **User Layer**: Telegram interface for users to interact with the bot.
2. **Backend Logic**: Bot backend developed using Python, managing interactions and requests.
3. **Web Scraper**: Uses Playwright to fetch information from the GKV website.

## Technologies Used

- **Programming Language**: Python 3.7+
- **Frameworks & Libraries**:
  - Python-Telegram-Bot API
  - Playwright (for web scraping)
  - Pytest (for testing)
- **Deployment**:
  - Docker for containerized deployment
  - Telegram Bot API for user interactions

## Installation & Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Shekhar1276/GKV_bot.git
   cd GKV_bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables for the Telegram bot token.
4. Run the bot:
   ```sh
   python main.py
   ```

## Deployment

- The bot runs in a Docker container to ensure an isolated environment.
- Use `docker-compose` to manage multiple containers.
- The scraper runs on a separate server and periodically updates information.

## Testing

Testing involves:

- Functional testing of bot commands (`/start`, `/help`, `/GetResult`, etc.).
- Stress testing for multiple requests.
- Edge case handling.
- Compatibility tests across different platforms.

Run tests using:

```sh
pytest tests/
```

## Future Enhancements

- Automatic result notifications.
- University notices and event updates.
- Integration with other university systems (library, campus maps, etc.).
- Enhanced user experience with AI-powered chat capabilities.

## References

- [Telegram API](https://core.telegram.org/bots/api)
- [Python-Telegram-Bot Documentation](https://python-telegram-bot.readthedocs.io/en/stable/)

## Author

Himanshu Shekhar (CSE, 2020-24)

---

This project aims to enhance the student experience by providing instant access to important university-related information through a simple and efficient Telegram bot.

