from simple_term_menu import TerminalMenu


def term_men(opts):
    terminal_menu = TerminalMenu(opts)
    menu_entry_index = terminal_menu.show()
    result = opts[menu_entry_index]  # type: ignore
    print(f"You have selected {result}!")  # type: ignore
    return result
