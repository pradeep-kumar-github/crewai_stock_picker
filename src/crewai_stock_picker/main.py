#!/usr/bin/env python
import sys
import warnings

from crewai_stock_picker.crew import CrewaiStockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'sector': 'Technology',
    }

    try:
        result = CrewaiStockPicker().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)

if __name__ == "__main__":
        run()