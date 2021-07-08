from extras.plugins import PluginMenuItem

devLable = " (dev) "

menu_items = (
    PluginMenuItem(
        link='plugins:phonebox_plugin:list_view',
        link_text='Numbers' + devLable,
        buttons=()
    ),
    PluginMenuItem(
        link='plugins:phonebox_plugin:range_list_view',
        link_text='Ranges' + devLable,
        buttons=()
    ),
)
