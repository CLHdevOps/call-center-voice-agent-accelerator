# Conversation Logs

This directory contains automatically saved conversation logs from voice agent sessions.

## Log Format

Each conversation is saved as a JSON file with the following structure:

```json
{
  "session_id": "unique-session-id",
  "session_start": "2025-11-25T10:30:00",
  "session_duration_seconds": 145.32,
  "total_events": 45,
  "model": "gpt-4o-mini",
  "endpoint": "https://...",
  "conversation": [
    {
      "timestamp": "2025-11-25T10:30:15.123",
      "elapsed_seconds": 15.123,
      "time_since_last_event": 0.850,
      "event_type": "transcript",
      "speaker": "user",
      "text": "Hello, I'm calling about the program",
      "metadata": {}
    },
    ...
  ]
}
```

## Event Types

- **transcript**: User or assistant speech transcription
- **speech_started**: User began speaking (VAD detected)
- **speech_stopped**: User stopped speaking

## Analyzing Conversations

Use the conversation analyzer script to view and analyze logs:

```bash
# Analyze most recent conversation
python conversation_analyzer.py

# Analyze specific log file
python conversation_analyzer.py conversation_logs/conversation_20251125_103000_abc123.json

# List all available logs
python conversation_analyzer.py --list

# Show summary statistics only
python conversation_analyzer.py --summary

# Export clean transcript
python conversation_analyzer.py --export transcript.txt
```

## What to Look For

When reviewing conversations, pay attention to:

1. **Response Times**: How quickly Grace responds after the user stops speaking
   - Target: < 2 seconds average
   - Anything over 5s may feel slow

2. **Pauses**: Significant pauses (>2s) during conversation
   - Natural pauses are OK
   - Frequent long pauses may indicate issues

3. **Turn-taking**: How smoothly the conversation flows
   - Check if Grace interrupts or waits too long
   - Look for overlapping speech patterns

4. **Conversation Flow**: Overall naturalness
   - Is Grace asking appropriate follow-up questions?
   - Is she collecting the required intake information?
   - Does she maintain context throughout the call?

## Privacy Note

These logs contain potentially sensitive information about callers. Handle them according to your organization's privacy and data retention policies.

## Automatic Cleanup

Consider implementing automatic log rotation/cleanup based on your retention requirements. Logs are not automatically deleted.
