#entity is used to define the return type of the function
# @dataclass decorator is used as it  means that once an instance of the data class is created, its fields cannot be modified.
# as configuration should not be changed once defined so we use @dataclass as it helps to preserve the fields without modifying them.
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) 
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path