# System Prompts Configuration

This directory contains system prompt configurations for the voice agent.

## Files

- **grace_intake_agent.txt** - Default system prompt for Grace, the intake agent for Mercy House and Sacred Grove facilities

## Usage

The prompts are automatically loaded by `acs_media_handler.py` when a session is created. To modify the agent's behavior:

1. Edit `grace_intake_agent.txt` directly
2. Save your changes
3. Restart the server - the new prompt will be loaded automatically

## Creating Alternative Prompts

To create different prompt configurations:

1. Create a new `.txt` file in this directory (e.g., `grace_spanish.txt`)
2. Copy the content from `grace_intake_agent.txt` as a starting point
3. Modify as needed
4. Update `acs_media_handler.py` to load your prompt:
   ```python
   "instructions": load_system_prompt("grace_spanish.txt"),
   ```

## Best Practices

- **Keep responses concise**: Aim for under 3 sentences for natural conversation flow
- **Use natural language**: Write as you would speak, including conversational phrases
- **Test changes thoroughly**: Small wording changes can significantly impact agent behavior
- **Version control**: This file is tracked in git, so you can see prompt evolution over time

## Prompt Structure

The current prompt includes:

1. **Character definition** - Who Grace is
2. **Personality traits** - How Grace should behave
3. **Conversational guidelines** - Natural speech patterns, disfluencies, tone matching
4. **Capabilities** - What Grace can help with
5. **Data collection** - What information to gather
6. **Edge cases** - Handling silence, unclear input, limitations

## Fallback Behavior

If the prompt file is missing or unreadable, the system falls back to a basic prompt. Check server logs for warnings if the agent behaves unexpectedly.
