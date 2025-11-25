#!/usr/bin/env python3
"""
Conversation Analyzer - View and analyze voice agent conversations with timing information.

Usage:
    python conversation_analyzer.py                          # Analyze most recent conversation
    python conversation_analyzer.py <log_file.json>          # Analyze specific conversation
    python conversation_analyzer.py --list                   # List all available logs
    python conversation_analyzer.py --summary               # Show quick summary only
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ConversationAnalyzer:
    """Analyzes conversation logs with timing and interaction patterns."""

    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.data: Optional[Dict] = None
        self.load_conversation()

    def load_conversation(self) -> None:
        """Load conversation data from JSON file."""
        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception as e:
            print(f"Error loading conversation log: {e}")
            sys.exit(1)

    def print_header(self) -> None:
        """Print conversation session header."""
        if not self.data:
            return

        print("=" * 80)
        print("CONVERSATION LOG ANALYSIS")
        print("=" * 80)
        print(f"Session ID:    {self.data['session_id']}")
        print(f"Start Time:    {self.data['session_start']}")
        print(f"Duration:      {self.data['session_duration_seconds']:.2f} seconds")
        print(f"Total Events:  {self.data['total_events']}")
        print(f"Model:         {self.data['model']}")
        print("=" * 80)
        print()

    def print_conversation(self) -> None:
        """Print formatted conversation with timing information."""
        if not self.data or "conversation" not in self.data:
            return

        print("CONVERSATION TIMELINE")
        print("-" * 80)

        for event in self.data["conversation"]:
            timestamp = datetime.fromisoformat(event["timestamp"]).strftime("%H:%M:%S")
            elapsed = event["elapsed_seconds"]
            time_since_last = event.get("time_since_last_event")
            speaker = event["speaker"]
            event_type = event["event_type"]
            text = event["text"]

            # Format delay/pause indicator
            delay_indicator = ""
            if time_since_last and time_since_last > 1.0:
                delay_indicator = f" [pause: {time_since_last:.1f}s]"

            # Format based on event type
            if event_type == "transcript":
                speaker_label = "USER" if speaker == "user" else "GRACE"
                print(f"\n[{timestamp}] +{elapsed:.1f}s{delay_indicator}")
                print(f"{speaker_label}: {text}")
            elif event_type == "speech_started":
                print(f"\n[{timestamp}] +{elapsed:.1f}s{delay_indicator}")
                print(f">>> {text} <<<")
            elif event_type == "speech_stopped":
                print(f"[{timestamp}] +{elapsed:.1f}s  >>> {text} <<<")

        print("\n" + "-" * 80)

    def analyze_timing(self) -> Dict:
        """Analyze conversation timing patterns."""
        if not self.data or "conversation" not in self.data:
            return {}

        conversation = self.data["conversation"]
        transcripts = [e for e in conversation if e["event_type"] == "transcript"]
        user_transcripts = [e for e in transcripts if e["speaker"] == "user"]
        assistant_transcripts = [e for e in transcripts if e["speaker"] == "assistant"]

        # Calculate response times (time between user stopping speech and assistant responding)
        response_times = []
        for i, event in enumerate(conversation):
            if event["event_type"] == "speech_stopped" and event["speaker"] == "user":
                # Find next assistant transcript
                for j in range(i + 1, len(conversation)):
                    if (conversation[j]["event_type"] == "transcript" and
                            conversation[j]["speaker"] == "assistant"):
                        response_time = (conversation[j]["elapsed_seconds"] -
                                         event["elapsed_seconds"])
                        response_times.append(response_time)
                        break

        # Calculate pauses
        all_delays = [e.get("time_since_last_event", 0) for e in conversation
                      if e.get("time_since_last_event")]
        significant_pauses = [d for d in all_delays if d > 2.0]

        return {
            "total_user_turns": len(user_transcripts),
            "total_assistant_turns": len(assistant_transcripts),
            "avg_response_time": sum(response_times) / len(response_times) if response_times else 0,
            "min_response_time": min(response_times) if response_times else 0,
            "max_response_time": max(response_times) if response_times else 0,
            "significant_pauses_count": len(significant_pauses),
            "longest_pause": max(significant_pauses) if significant_pauses else 0
        }

    def print_analysis(self) -> None:
        """Print conversation analysis and statistics."""
        stats = self.analyze_timing()

        print("\nCONVERSATION ANALYSIS")
        print("-" * 80)
        print(f"User turns:              {stats['total_user_turns']}")
        print(f"Assistant turns:         {stats['total_assistant_turns']}")
        print(f"\nResponse Times:")
        print(f"  Average:               {stats['avg_response_time']:.2f}s")
        print(f"  Fastest:               {stats['min_response_time']:.2f}s")
        print(f"  Slowest:               {stats['max_response_time']:.2f}s")
        print(f"\nPauses (>2s):            {stats['significant_pauses_count']}")
        print(f"Longest pause:           {stats['longest_pause']:.2f}s")
        print("-" * 80)

    def export_transcript(self, output_path: Path) -> None:
        """Export clean transcript without timing information."""
        if not self.data or "conversation" not in self.data:
            return

        transcripts = [e for e in self.data["conversation"]
                       if e["event_type"] == "transcript"]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"Conversation Transcript\n")
            f.write(f"Session: {self.data['session_id']}\n")
            f.write(f"Date: {self.data['session_start']}\n")
            f.write(f"Duration: {self.data['session_duration_seconds']:.2f}s\n")
            f.write("=" * 80 + "\n\n")

            for event in transcripts:
                speaker = "USER" if event["speaker"] == "user" else "GRACE"
                f.write(f"{speaker}: {event['text']}\n\n")

        print(f"\nTranscript exported to: {output_path}")


def find_latest_log(logs_dir: Path) -> Optional[Path]:
    """Find the most recent conversation log file."""
    if not logs_dir.exists():
        return None

    log_files = sorted(logs_dir.glob("conversation_*.json"), reverse=True)
    return log_files[0] if log_files else None


def list_logs(logs_dir: Path) -> None:
    """List all available conversation logs."""
    if not logs_dir.exists():
        print("No conversation logs directory found.")
        return

    log_files = sorted(logs_dir.glob("conversation_*.json"), reverse=True)

    if not log_files:
        print("No conversation logs found.")
        return

    print("\nAvailable Conversation Logs:")
    print("-" * 80)

    for log_file in log_files:
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            session_start = datetime.fromisoformat(data["session_start"]).strftime("%Y-%m-%d %H:%M:%S")
            duration = data["session_duration_seconds"]
            events = data["total_events"]

            print(f"{log_file.name}")
            print(f"  Date: {session_start} | Duration: {duration:.1f}s | Events: {events}")
        except Exception:
            print(f"{log_file.name} (error reading file)")

    print("-" * 80)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze voice agent conversation logs with timing information."
    )
    parser.add_argument(
        "log_file",
        nargs="?",
        help="Path to conversation log JSON file (defaults to most recent)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available conversation logs"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show summary statistics only"
    )
    parser.add_argument(
        "--export",
        metavar="OUTPUT",
        help="Export clean transcript to text file"
    )

    args = parser.parse_args()

    # Find logs directory
    script_dir = Path(__file__).parent
    logs_dir = script_dir / "conversation_logs"

    # Handle --list option
    if args.list:
        list_logs(logs_dir)
        return

    # Determine which log file to analyze
    if args.log_file:
        log_path = Path(args.log_file)
        if not log_path.exists():
            print(f"Error: Log file not found: {log_path}")
            sys.exit(1)
    else:
        log_path = find_latest_log(logs_dir)
        if not log_path:
            print("No conversation logs found.")
            print(f"Looking in: {logs_dir.absolute()}")
            sys.exit(1)
        print(f"Analyzing most recent log: {log_path.name}\n")

    # Analyze conversation
    analyzer = ConversationAnalyzer(log_path)
    analyzer.print_header()

    if args.summary:
        analyzer.print_analysis()
    else:
        analyzer.print_conversation()
        analyzer.print_analysis()

    # Export transcript if requested
    if args.export:
        output_path = Path(args.export)
        analyzer.export_transcript(output_path)


if __name__ == "__main__":
    main()
