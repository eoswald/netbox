import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from netbox.tables import BaseTable

__all__ = (
    'CertifiedPluginTable',
)


class CertifiedPluginTable(BaseTable):
    version = tables.Column(
        verbose_name=_('Version')
    )
    last_updated = tables.Column(
        accessor=tables.A('date'),
        verbose_name=_('Last Updated')
    )
    min_version = tables.Column(
        accessor=tables.A('netbox_min_version'),
        verbose_name=_('Minimum NetBox Version')
    )
    max_version = tables.Column(
        accessor=tables.A('netbox_max_version'),
        verbose_name=_('Maximum NetBox Version')
    )

    class Meta(BaseTable.Meta):
        empty_text = _('No plugin data found')
        fields = (
            'version', 'last_updated', 'min_version', 'max_version',
        )
        default_columns = (
            'version', 'last_updated', 'min_version', 'max_version',
        )