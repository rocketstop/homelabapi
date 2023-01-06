from pydantic import Field

from app.constants import sample_uptimerobot_adt, sample_uptimerobot_ade, sample_uptimerobot_adu, sample_uptimerobot_at, \
    sample_uptimerobot_atfn, sample_uptimerobot_mac, sample_uptimerobot_mfn, sample_uptimerobot_mid, \
    sample_uptimerobot_murl, sample_uptimerobot_sed, sample_uptimerobot_sedl


class UptimeRobotModel(CommonModel):
    alertDateTime: str = Field(default=None, example=sample_uptimerobot_adt)
    alertDetails: str = Field(default=None, example=sample_uptimerobot_ade)
    alertDuration: str = Field(default=None, example=sample_uptimerobot_adu)
    alertType: str = Field(default=None, example=sample_uptimerobot_at)
    alertTypeFriendlyName: str = Field(default=None, example=sample_uptimerobot_atfn)
    monitorAlertContacts: str = Field(default=None, example=sample_uptimerobot_mac)
    monitorFriendlyName: str = Field(default=None, example=sample_uptimerobot_mfn)
    monitorID: str = Field(default=None, example=sample_uptimerobot_mid)
    monitorURL: str = Field(default=None, example=sample_uptimerobot_murl)
    sslExpiryDate: str = Field(default=None, example=sample_uptimerobot_sed)
    sslExpiryDaysLeft: str = Field(default=None, example=sample_uptimerobot_sedl)

    class Config:
        schema_extra = dict(
            {
                "example": {
                    **CommonModel.Config.schema_extra["example"],
                    **{"alertDateTime": sample_uptimerobot_adt},
                    **{"alertDetails": sample_uptimerobot_ade},
                    **{"alertDuration": sample_uptimerobot_adu},
                    **{"alertType": sample_uptimerobot_at},
                    **{"alertTypeFriendlyName": sample_uptimerobot_atfn},
                    **{"monitorAlertContacts": sample_uptimerobot_mac},
                    **{"monitorFriendlyName": sample_uptimerobot_mfn},
                    **{"monitorID": sample_uptimerobot_mid},
                    **{"monitorURL": sample_uptimerobot_murl},
                    **{"sslExpiryDate": sample_uptimerobot_sed},
                    **{"sslExpiryDaysLeft": sample_uptimerobot_sedl},
                }
            }
        )
