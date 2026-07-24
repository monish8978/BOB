# Changelog

All notable changes to the BoB Chatbot simulator repository are documented below. This is the first creation of this file, describing both the initial base project architecture and the subsequent update release.

---

## [1.1.0] - 2026-07-13

### Added
- **`setup_env.sh`**: Added environment setup bash script that automatically detects and copies `.env.example` or `env.example` to `.env` if `.env` does not exist.
- **`LIVE_AGENT_ACTION_ID` Configuration**: Exposed the live agent transfer action ID (`9999.5006`) as a configurable variable in `.env`, `.env.example`, and `app/config.py` (`settings.LIVE_AGENT_ACTION_ID`).

### Changed
- **Endpoint Redirection**: Changed chatbot simulation API endpoint path from `/api/simulate` to `/api/bob` across the backend router (`app/api/portal.py`), frontend client (`app/static/js/chat.js`), and project documentation (`README.md`).
- **Optional Request Fields**: Updated the `MessageRequest` validation schema (`app/schemas.py`) so that `sessionid` is optional and defaults to `"1"`. Added corresponding fallback logic in `app/api/portal.py` for request validation.
- **Robust Message Formatting**: Rewrote `formatMarkdown` inside `chat.js` to safely escape unknown HTML elements while preserving and rendering whitelisted bot response elements:
  - Bolds: `<b>` / `<strong>`
  - Line Breaks: `<br>` / `\n`
  - Lists: `<li>` / bullets (`*`, `-`, `•`)
  - Hyperlinks: `<link href="...">` / `<a>`
- **Dynamic Source-Based Layouts**: Integrated channel/client source detection from `extraParms`:
  - When source is `"whatsappchat"`, the live agent connection reply renders both the text instructions and the interactive buttons choices block.
  - When source is `"webchat"`, the response remains cleaner, showing only the instruction block.

---

## [1.0.0] - Initial Project Architecture

This is the initial release of the Bank of Bhutan (BoB) Chatbot Simulator system. The project serves as an interactive simulation dashboard and state machine wrapper for customer support.

### Core Architecture Components
- **FastAPI Web Application**: Integrates REST API routes for simulation routing (`/api/bob`), session management, and log review. Serves static dashboard assets and HTML/CSS web widgets.
- **Finite State Machine Dialog Engine**: Tracks active session conversation states (e.g. `main_menu`, `mbob`, `cards`, `kyc`) in Redis and maps button payloads or input text to configured menu items.
- **Persistent MySQL Database**: Declares schemas for persistent data models (`Ticket` and `MessageLog`) via SQLAlchemy ORM.
- **Celery Task Worker**: Operates asynchronous background workers to queue and process logged CRM support tickets.
- **Redis Cache Storage**: Used as the broker for Celery queues and as a fast state-machine session tracker.
- **AI RAG Fallback Integration**: Interfaces with a Retrieval-Augmented Generation API to fetch automatic context-aware answers to user free-text queries when no static menu match is found.
- **Frontend Dashboard Widget**: A glassmorphism control panel showing a real-time mobile simulation viewport alongside ticket audits and message logs.
