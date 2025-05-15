from src.utils.job_processor import JobProcessor


def main() -> None:
    """
    Initializes a JobProcessor with the specified job definition file and processes the jobs.

    This function creates an instance of the JobProcessor class using the "job_definition.json" file
    and calls its process_jobs method to execute the defined jobs.
    """
    processor = JobProcessor("job_definition.json")
    processor.process_jobs()


if __name__ == "__main__":
    main()
