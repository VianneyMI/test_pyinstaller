from datetime import date
from typing import List
from pydantic import BaseModel, Field, validator
import pandas as pd


class EmployeeData(BaseModel):
    employee_id: int = Field(..., description="Unique employee identifier")
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    department: str = Field(..., min_length=2, max_length=50)
    salary: float = Field(..., gt=0)
    hire_date: date
    is_active: bool
    skills: List[str] = Field(default_factory=list)

    @validator("salary")
    def validate_salary(cls, v):
        if v < 0:
            raise ValueError("Salary must be positive")
        return round(v, 2)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data before validation"""
    # Create a copy to avoid modifying the original dataframe
    df = df.copy()

    # Convert date strings to datetime objects
    if "hire_date" in df.columns:
        df["hire_date"] = pd.to_datetime(df["hire_date"]).dt.date

    # Convert boolean strings to actual booleans
    if "is_active" in df.columns:
        # First, convert to string and lowercase for consistent processing
        df["is_active"] = df["is_active"].astype(str).str.lower()
        # Map various boolean representations to True/False
        bool_map = {
            "true": True,
            "1": True,
            "yes": True,
            "y": True,
            "false": False,
            "0": False,
            "no": False,
            "n": False,
        }
        df["is_active"] = df["is_active"].map(bool_map)
        # Fill any NaN values with False
        df["is_active"] = df["is_active"].fillna(False)

    # Convert skills string to list if it's a string
    if "skills" in df.columns:
        df["skills"] = df["skills"].apply(
            lambda x: [s.strip() for s in str(x).split(",")] if pd.notna(x) else []
        )

    return df


def validate_dataframe(df: pd.DataFrame) -> List[EmployeeData]:
    """Validate the dataframe against the Pydantic model"""
    df = preprocess_data(df)
    validated_data = []
    errors = []

    for idx, row in df.iterrows():
        try:
            data = EmployeeData(**row.to_dict())
            validated_data.append(data)
        except Exception as e:
            errors.append(f"Row {idx + 1}: {str(e)}")

    if errors:
        raise ValueError("\n".join(errors))

    return validated_data
