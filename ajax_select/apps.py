from django.apps import AppConfig


class AjaxSelectConfig(AppConfig):
    """
    On startup, search for and import any modules called `lookups.py` in all installed apps.
    Your LookupClass subclass may register itself.
    """

    name = 'ajax_select'
    verbose_name = 'Ajax Selects'

    def ready(self):
        from ajax_select.registry import registry
        registry.load_channels()
