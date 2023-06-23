import view
import model
import text


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contact(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contact(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contact(result, text.empty_search(word))
                index = view.input_return(text.change_index)
                new = view.input_contact(text.input_change_contact)
                model.change(new)
                # old_name = model.phone_book[int(index) - 1].get('name')
                # view.print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))
            case 7:
                index = view.input_return(text.remove_index)
                del_cnt = model.remove(index)
                name = del_cnt.get("name")
                view.print_message(text.contact_remove(name))
            case 8:
                view.print_message(text.bay_bay)
                break