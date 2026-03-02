# Gemini GroupMe Bot

A Python bot hosted on Vercel that connects Gemini AI to a GroupMe chat.

## Features
- **Prefix Trigger:** Responds only to messages starting with `^`. This can be customized in the code to any character of your choosing.
- **AI Powered:** Uses `gemini-2.0-flash` for fast responses.
- **Serverless:** Runs on Vercel's free tier with no server.

## Setup

### 1. Environment Variables
You will need to set these in your Vercel Dashboard:
- `GEMINI_API_KEY`: Get this from [Google AI Studio](https://aistudio.google.com/).
- `GROUP_ME_BOT_ID`: Get this from [GroupMe Dev Portal](https://dev.groupme.com/).

### 2. Deployment
1. Push this folder to a GitHub repository.
2. Connect the repository to **Vercel**.
3. Set the Framework Preset to **Other**.
4. Add your Environment Variables and click **Deploy**.

## Usage
In your GroupMe chat, type:
`^What are some cool facts about space?`