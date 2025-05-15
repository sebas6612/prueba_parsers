import json
import logging
from typing import Dict, Any
from pathlib import Path
from src.parsers.zip_parser import ZipFileParser
from src.parsers.xml_parser import XmlToCsvParser


class JobProcessor:
    """Process jobs defined in a JSON configuration file"""

    PARSER_MAPPING = {"unzip": ZipFileParser, "xml_to_csv": XmlToCsvParser}

    def __init__(self, job_file: str) -> None:
        self.job_file = job_file
        self._setup_logging()
        self.logger.info(f"Initializing JobProcessor with job file: {job_file}")
        self.job_definition = self._load_job_file()

    def _setup_logging(self) -> None:
        """Configure logging settings"""
        # Create logs directory if it doesn't exist
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        # Create a logger instance
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create handlers
        file_handler = logging.FileHandler(
            log_dir / "job_processor.log", encoding="utf-8"
        )
        console_handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        log_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(log_format)
        console_handler.setFormatter(log_format)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def _load_job_file(self) -> Dict[str, Any]:
        """Load and parse the JSON job definition file"""
        try:
            with open(self.job_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"Job definition file not found: {self.job_file}")
            raise
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in file: {self.job_file}")
            raise

    def process_jobs(self) -> None:
        """Process all transformations defined in the job file"""
        total_jobs = len(self.job_definition["transformations"])
        self.logger.info(f"Starting to process {total_jobs} transformations")

        for index, transformation in enumerate(
            self.job_definition["transformations"], 1
        ):
            try:
                self._process_transformation(transformation)
                self.logger.info(f"Completed transformation {index}/{total_jobs}")
            except Exception as e:
                self.logger.error(
                    f"Error processing transformation {index}/{total_jobs}: {str(e)}"
                )

        self.logger.info("Finished processing all transformations")

    def _process_transformation(self, transformation: Dict[str, Any]) -> None:
        """Process a single transformation"""
        parser_type = transformation["object"]["parser"]
        origin = transformation["object"]["origin"]
        destiny = transformation["object"]["destiny"]

        if parser_type not in self.PARSER_MAPPING:
            self.logger.warning(
                f"Skipping unknown parser type: {parser_type}. "
                f"Available parsers: {', '.join(self.PARSER_MAPPING.keys())}"
            )
            return

        try:
            parser_class = self.PARSER_MAPPING[parser_type]
            self.logger.info(
                f"Processing {parser_type} parser - "
                f"Origin: {origin}, Destiny: {destiny}"
            )

            parser = parser_class(origin=origin, destiny=destiny)
            parser.parse()

            self.logger.info(f"Successfully processed {parser_type} parser")
        except Exception as e:
            self.logger.error(f"Error while processing {parser_type} parser: {str(e)}")
            raise
