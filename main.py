import plugins


def main() -> int:
    plugin_list = plugins.get_plugins()
    if len(plugin_list) < 1:
        print("No plugins found. put plugins (.py file) in /plugins.")
        return 1
    print('plugins:')
    for i in range(len(plugin_list)):
        print(f'\t{i}. {plugin_list[i]}')
    selected = input('select plugin(number or name): ')
    if selected in plugin_list:
        plugin = plugins.get_plugin(selected)
    elif selected.isdigit() and int(selected) < len(plugin_list):
        plugin = plugins.get_plugin(plugin_list[int(selected)])
    else:
        print('plugin not found')
        return 1

    print(f'plugin selected: {selected}')
    plugin.execute()
    return 0


if __name__ == '__main__':
    exit(main())
