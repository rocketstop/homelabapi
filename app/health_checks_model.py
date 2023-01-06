from pydantic import Field

from app.constants import sample_healthchecks_name, sample_healthchecks_status, sample_healthchecks_tags, \
    sample_healthchecks_time, sample_healthchecks_uuid


class HealthChecksModel(CommonModel):
    name: str = Field(default=None, example=sample_healthchecks_name)
    status: str = Field(default=None, example=sample_healthchecks_status)
    tags: str = Field(default=None, example=sample_healthchecks_tags)
    time: str = Field(default=None, example=sample_healthchecks_time)
    uuid: str = Field(default=None, example=sample_healthchecks_uuid)

    class Config:
        schema_extra = dict(
            {
                "example": {
                    **CommonModel.Config.schema_extra["example"],
                    **{"name": sample_healthchecks_name},
                    **{"status": sample_healthchecks_status},
                    **{"tags": sample_healthchecks_tags},
                    **{"time": sample_healthchecks_time},
                    **{"uuid": sample_healthchecks_uuid},
                }
            }
        )
