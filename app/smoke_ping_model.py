from pydantic import Field

from app.constants import sample_smokeping_alertname, sample_smokeping_hostname, sample_smokeping_losspattern, \
    sample_smokeping_target, sample_smokeping_rtt


class SmokePingModel(CommonModel):
    alertname: str = Field(default=None, example=sample_smokeping_alertname)
    hostname: str = Field(default=None, example=sample_smokeping_hostname)
    losspattern: str = Field(default=None, example=sample_smokeping_losspattern)
    rtt: str = Field(default=None, example=sample_smokeping_rtt)
    target: str = Field(default=None, example=sample_smokeping_target)

    class Config:
        schema_extra = dict(
            {
                "example": {
                    **CommonModel.Config.schema_extra["example"],
                    **{"alertname": sample_smokeping_alertname},
                    **{"hostname": sample_smokeping_hostname},
                    **{"losspattern": sample_smokeping_losspattern},
                    **{"rtt": sample_smokeping_rtt},
                    **{"target": sample_smokeping_target},
                }
            }
        )
