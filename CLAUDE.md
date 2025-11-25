# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **Call Center Voice Agent Accelerator** built with Azure Voice Live API and Azure Communication Services (ACS). It provides real-time speech-to-speech voice agents for call center scenarios with two client modes: web browser (for testing) and ACS phone calls (for production).

## Technology Stack

- **Backend**: Python 3.9+ with Quart (async Flask-like framework)
- **Package Manager**: UV (fast Python dependency management via `pyproject.toml`)
- **Infrastructure**: Azure Bicep templates for IaC
- **Deployment**: Azure Developer CLI (`azd`)
- **Key Azure Services**:
  - Azure Voice Live API (Speech-to-speech with integrated ASR, LLM, TTS)
  - Azure Communication Services (telephony/call automation)
  - Azure Container Apps (hosting)
  - Azure Container Registry
  - Azure Key Vault (stores ACS connection string)

## Development Commands

### Local Development (server/ directory)

```bash
# Run the server locally
uv run server.py

# Access web client at http://127.0.0.1:8000
```

### Docker Development

```bash
# Build image
docker build -t voiceagent .

# Run with environment variables
docker run --env-file .env -p 8000:8000 -it voiceagent
```

### Deployment

```bash
# Login to Azure
azd auth login

# Deploy all resources (initial + updates)
azd up

# Deploy code changes only
azd deploy

# Clean up all resources
azd down
```

### Testing with ACS Phone Client (Local)

Use Azure DevTunnels to expose local server for webhook testing:

```bash
devtunnel login
devtunnel create --allow-anonymous
devtunnel port create -p 8000
devtunnel host
```

## Architecture

### Core Application Structure

```
server/
├── server.py                    # Main Quart application with routes
├── app/
│   └── handler/
│       ├── acs_event_handler.py # Processes ACS incoming calls and callbacks
│       └── acs_media_handler.py # Manages audio streaming to Voice Live API
└── static/                      # Web client HTML/JS
```

### Request Flow

1. **Web Client Mode**: Browser → `/web/ws` WebSocket → `ACSMediaHandler` → Voice Live API
2. **ACS Phone Mode**: Phone Call → ACS IncomingCall event → `/acs/incomingcall` → Answer call with media streaming → `/acs/ws` WebSocket → `ACSMediaHandler` → Voice Live API

### Key Handlers

- **AcsEventHandler** (`acs_event_handler.py`): Handles EventGrid subscription validation and incoming call events. Answers calls with `MediaStreamingOptions` configured for bidirectional audio.
- **ACSMediaHandler** (`acs_media_handler.py`): Establishes WebSocket connection to Voice Live API, manages audio queues, and handles bidirectional audio streaming. Uses managed identity or API key authentication.

### Infrastructure (infra/)

Bicep modules provision:
- User-assigned managed identity (for Key Vault and AI services access)
- AI Services (Voice Live API endpoint)
- Communication Services (telephony)
- Container Apps + Container Registry
- Key Vault (stores ACS connection string as secret)
- Monitoring (Log Analytics, Application Insights)

The main deployment is subscription-scoped (`infra/main.bicep`). Note: Limited to `eastus2` and `swedencentral` regions due to Voice Live API availability.

## Environment Configuration

Create `.env` file in `server/` directory based on `.env-sample.txt`:

```
AZURE_VOICE_LIVE_API_KEY=<AI Foundry resource key>
AZURE_VOICE_LIVE_ENDPOINT=<AI Foundry resource endpoint>
VOICE_LIVE_MODEL=gpt-4o-mini
ACS_CONNECTION_STRING=<Communication Services connection string>
ACS_DEV_TUNNEL=<Optional: DevTunnel URL for local ACS testing>
```

When deployed to Azure, the container app uses:
- Managed Identity for Voice Live API authentication
- Key Vault secret reference for ACS connection string

## Voice Live API Configuration

Session configuration is defined in [acs_media_handler.py:68](server/app/handler/acs_media_handler.py#L68):
- **Turn Detection**: Azure Semantic VAD with end-of-utterance detection
- **Audio Processing**: Deep noise suppression and server echo cancellation
- **Voice**: Configurable Azure Neural TTS voice (default: en-US-Emma2:DragonHDLatestNeural)
- **Instructions**: Loaded dynamically from [server/prompts/grace_intake_agent.txt](server/prompts/grace_intake_agent.txt)

### System Prompt Configuration

System prompts are now externalized for easy editing without code changes:

- **Location**: [server/prompts/grace_intake_agent.txt](server/prompts/grace_intake_agent.txt)
- **Editing**: Directly edit the text file and restart the server
- **Creating Variants**: Copy the file and modify the prompt loader in `session_config()`
- **Documentation**: See [server/prompts/README.md](server/prompts/README.md) for guidance

The current prompt configures Grace as a professional intake receptionist for Mercy House and Sacred Grove facilities.

## Post-Deployment Setup

After `azd up`:
1. Navigate to the Container App URL to test the web client
2. For phone testing:
   - Create Event Grid subscription for IncomingCall events pointing to `https://<container-app-url>/acs/incomingcall`
   - Provision a phone number for the ACS resource
   - Call the number to test the voice agent

## Conversation Logging and Analysis

The system automatically logs all conversations with detailed timing information for analysis and quality assurance.

### Automatic Logging

Every session is automatically saved to [server/conversation_logs/](server/conversation_logs/) as a JSON file containing:
- Full conversation transcript (user and assistant)
- Precise timestamps for each event
- Time delays/pauses between utterances
- Speech detection events (started/stopped)
- Session metadata (duration, model, endpoint)

### Analyzing Conversations

Use the conversation analyzer tool to review and analyze logged conversations:

```bash
# View most recent conversation with timing analysis
python server/conversation_analyzer.py

# Analyze specific conversation log
python server/conversation_analyzer.py server/conversation_logs/conversation_20251125_103000_abc123.json

# List all available conversation logs
python server/conversation_analyzer.py --list

# Export clean transcript to text file
python server/conversation_analyzer.py --export transcript.txt
```

### Key Metrics

The analyzer provides:
- **Response Times**: How quickly Grace responds after user stops speaking
- **Turn-taking Analysis**: User and assistant turn counts
- **Pause Detection**: Identifies significant pauses (>2s) in conversation
- **Conversation Flow**: Timeline view showing exact timing of all events

### Privacy and Data Retention

Conversation logs may contain sensitive caller information (names, phone numbers, personal situations). Handle according to your organization's privacy policies:
- Logs are saved locally and NOT automatically sent anywhere
- Implement log rotation/cleanup based on your retention requirements
- Log files are gitignored by default (`.gitignore` excludes `*.json` files in conversation_logs/)

See [server/conversation_logs/README.md](server/conversation_logs/README.md) for detailed documentation.

## Important Notes

- **Security**: ACS connection string is stored in Key Vault. Container app retrieves it via secret reference.
- **Authentication**: Production deployments use managed identity for Voice Live API. Local development uses API key.
- **Region Constraints**: Voice Live API is only available in specific regions (swedencentral strongly recommended).
- **WebSocket Endpoints**: `/web/ws` for browser clients (raw audio), `/acs/ws` for ACS calls (PCM 24kHz mono).
