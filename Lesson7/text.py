class Text:
    def __init__(self, text=" "):
        self.text = text
    

    def add_text(self, text_to_add):
        '''
        Params:
            text_to_add -> string
        Purpose:
            adds text at the end of an already existing string of text
        Return:
            a string of the new text
        '''
        if isinstance(text_to_add, str) or isinstance(text_to_add, Text):
            self.text += f" {text_to_add}"
        else:
            raise TypeError("Please type a string if you are adding text!!")
        return self.get_text_as_string()
    

    def delete_text(self, text_to_delete, text_to_add=""):
        """
        Purpose:
            searches an existing string, if the string that is passed this function is existent within the current text, that portion of text is removed.
        
        Keyword arguments:
            text_to_delete -> string
                -text to be deleted from the base string

        Return:
            ex. "Hello" -> Text.delete_text("lo") -> "Hel"
            returns the new string
        """
        if isinstance(text_to_delete, str) and isinstance(text_to_add, str):
            self.text = str(self.text).replace(f"{text_to_delete}", text_to_add)
        else:
            raise TypeError("Please type a string if you are deleting text!!")
        return self.print_text()
        
    
    def replace_text(self, text_to_replace, text_to_replace_with):
        """
        Purpose:
            leverages delete_text method to replace the text that gets deleted, with text_to_replace_with
        
        Keyword arguments:
            text_to_replace -> string
                -text to be removed from the existing string
            
            text_to_replace_with -> string
                -text to replace the text that was removed from the existing string
        Return:
            see above section delete_text -> 'Return'
        """
        
        self.delete_text(text_to_delete=text_to_replace, text_to_add=text_to_replace_with)

    
    def print_text(self):
        return print(self.text)
    

    def get_text_as_string(self):
        return str(self.text)
