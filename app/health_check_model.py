from .common_model import CommonModel
from pydantic import Field

from app.constants import sample_monit_date, sample_monit_action, sample_monit_description, sample_monit_event, \
    sample_monit_host, sample_monit_process_children, sample_monit_process_cpu_percent, sample_monit_process_pid, \
    sample_monit_process_memory, sample_monit_program_status, sample_monit_service


class MonitModel(CommonModel):
    action: str = Field(default=None, example=sample_monit_action)
    date: str = Field(default=None, example=sample_monit_date)
    description: str = Field(default=None, example=sample_monit_description)
    event: str = Field(default=None, example=sample_monit_event)
    host: str = Field(default=None, example=sample_monit_host)
    process_children: str = Field(default=None, example=sample_monit_process_children)
    process_cpu_percent: str = Field(
        default=None, example=sample_monit_process_cpu_percent
    )
    process_pid: str = Field(default=None, example=sample_monit_process_pid)
    process_memory: str = Field(default=None, example=sample_monit_process_memory)
    program_status: str = Field(default=None, example=sample_monit_program_status)
    service: str = Field(default=None, example=sample_monit_service)

    class Config:
        schema_extra = {
            "example": {
                **CommonModel.Config.schema_extra["example"],
                "action": sample_monit_action,
                "date": sample_monit_date,
                "description": sample_monit_description,
                "event": sample_monit_event,
                "host": sample_monit_host,
                "process_children": sample_monit_process_children,
                "process_cpu_percent": sample_monit_process_cpu_percent,
                "process_pid": sample_monit_process_pid,
                "process_memory": sample_monit_process_memory,
                "program_status": sample_monit_program_status,
                "service": sample_monit_service,
            }
        }