from pydantic import BaseModel, Field

from app.constants import sample_api_key, sample_subject, sample_message, sample_url, sample_priority, sample_source


class CommonModel(BaseModel):
    api_key: str = Field(example=sample_api_key)
    subject: str = Field(default=sample_subject, example=sample_subject)
    message: str = Field(example=sample_message)
    url: str = Field(default=None, example=sample_url)
    priority: str = Field(default=0, example=sample_priority)
    source: str = Field(default=None, example=sample_source)

    class Config:
        schema_extra = {
            "example": {
                "api_key": sample_api_key,
                "subject": sample_subject,
                "message": sample_message,
                "url": sample_url,
                "priority": sample_priority,
                "source": sample_source,
            }
        }